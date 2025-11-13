"""
输入半径计算圆的周长和面积

Version: 1.2
Author: Ethan
"""
import math
from re import T

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.4f}')  # 输出：perimeter = 34.56
print(f'{area = :.4f}')       # 输出：area = 95.035
