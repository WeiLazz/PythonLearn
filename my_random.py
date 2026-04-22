import random

print(random.random())          # 0.374...
print(random.randint(1, 10))    # 随机整数 1~10

colors = ['红', '绿', '蓝']
print(random.choice(colors))    # 随机颜色

cards = ['A', '2', '3', 'K']
random.shuffle(cards)
print(cards)                    # 顺序被打乱

lotto = random.sample(range(1, 50), 6)
print(lotto)                    # 随机抽6个不同数字
