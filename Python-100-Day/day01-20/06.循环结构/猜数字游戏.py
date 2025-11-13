import random

answer = random.randint(1, 101)
num = int(input('请输入一个1到100之间的整数: '))
while num != answer:
    if num > answer:
        print('你猜的数字大了')
    else:
        print('你猜的数字小了')
    num = int(input('请输入一个1到100之间的整数: '))
print('恭喜你猜对了')
