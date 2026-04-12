#!/usr/bin/env python3
"""
日志分析脚本 - 分析Web服务器访问日志（combined格式）
功能：
1. 统计每个IP的请求次数
2. 统计HTTP状态码分布
3. 找出请求最多的10个URL
4. 检测可能的扫描行为（请求大量不同URL的IP）
"""

import re
import sys
import argparse
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

# Apache/Nginx combined log 格式的正则表达式
# 示例行：127.0.0.1 - - [10/May/2025:13:55:36 +0800] "GET /index.html HTTP/1.1" 200 2326
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>.*?)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

def parse_log_line(line: str) -> Dict[str, str]:
    """解析一行日志，返回字段字典，失败返回None"""
    match = LOG_PATTERN.match(line.strip())
    if match:
        return match.groupdict()
    return None

def analyze_log(log_file: str) -> None:
    """读取日志文件并执行分析"""
    ip_counter = Counter()
    status_counter = Counter()
    url_counter = Counter()
    ip_url_map = defaultdict(set)  # 记录每个IP访问过的不同URL集合，用于检测扫描

    total_lines = 0
    parse_errors = 0

    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                total_lines += 1
                parsed = parse_log_line(line)
                if not parsed:
                    parse_errors += 1
                    continue

                ip = parsed['ip']
                status = parsed['status']
                url = parsed['url']

                ip_counter[ip] += 1
                status_counter[status] += 1
                url_counter[url] += 1
                ip_url_map[ip].add(url)

    except FileNotFoundError:
        print(f"错误：文件 {log_file} 不存在")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        sys.exit(1)

    # 输出分析结果
    print("=" * 60)
    print(f"日志文件分析报告：{log_file}")
    print(f"总行数：{total_lines}，解析失败行数：{parse_errors}")
    print("=" * 60)

    # 1. IP访问次数排行（前10）
    print("\n【IP访问次数 Top 10】")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip:20} -> {count:8} 次")

    # 2. HTTP状态码分布
    print("\n【HTTP状态码分布】")
    for code, count in sorted(status_counter.items()):
        print(f"{code}: {count}")

    # 3. 请求最多的URL（前10）
    print("\n【请求最多的URL Top 10】")
    for url, count in url_counter.most_common(10):
        print(f"{url[:50]:50} -> {count:8} 次")

    # 4. 可疑扫描行为：请求不同URL数量超过阈值的IP（阈值默认30）
    threshold = 30
    suspicious = {ip: len(urls) for ip, urls in ip_url_map.items() if len(urls) > threshold}
    if suspicious:
        print(f"\n【可能存在的扫描行为】（单个IP请求不同URL数 > {threshold}）")
        for ip, url_count in sorted(suspicious.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip:20} -> 请求了 {url_count} 个不同的URL")
    else:
        print(f"\n未发现明显的扫描行为（阈值：{threshold}个不同URL）")

def main():
    parser = argparse.ArgumentParser(description="分析Web服务器combined格式访问日志")
    parser.add_argument("logfile", help="日志文件路径")
    parser.add_argument("--threshold", type=int, default=30, help="扫描检测阈值（不同URL数量），默认30")
    args = parser.parse_args()

    analyze_log(args.logfile)

if __name__ == "__main__":
    main()