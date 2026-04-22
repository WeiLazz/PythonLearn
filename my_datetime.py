
from datetime import datetime, date, time, timedelta

# 获取当前时间
now = datetime.now()
print(f"当前: {now}")

# 日期运算
tomorrow = now + timedelta(days=1)
print(f"明天: {tomorrow.date()}")

# 格式化输出
print(now.strftime("%Y-%m-%d and  %H:%M:%S"))   # 2025-05-10 and 14:30:00
print(now.strftime("%A"))                  # 星期几

# 字符串转 datetime
date_str = "2025-12-25 10:30:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt.month)  # 12
