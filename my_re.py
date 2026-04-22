import re

text = "张三的电话是 13812345678，李四的电话是 13987654321"

# 提取所有手机号（简单11位数字）
phones = re.findall(r'\d{11}', text)
print(phones)  # ['13812345678', '13987654321']

# 搜索第一个手机号
match = re.search(r'(\d{11})', text)
if match:
    print(match.group(1))  # 13812345678

# 替换手机号中间四位为****
masked = re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', text)
print(masked)  # 张三的电话是 138****5678，李四的电话是 139****4321

# 预编译 + 匹配邮箱
email_pattern = re.compile(r'\w+@\w+\.\w+')
emails = email_pattern.findall("联系: admin@example.com, support@test.org")
print(emails)
