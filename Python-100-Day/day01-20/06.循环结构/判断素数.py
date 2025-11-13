"""
输入一个大于1的正整数判断它是不是素数

Version: 1.0
Author: Ethan
"""


Num = int(input('请输入一个大于1的正整数: '))
end = int(Num ** 0.5)
for i in range(2, end + 1):
    if Num % i == 0:
        print(f'{Num}不是素数')
        break
else:
    print(f'{Num}是素数')
