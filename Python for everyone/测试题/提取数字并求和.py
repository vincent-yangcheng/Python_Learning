#这个问题的基本思路是读取文件，使用以下方法查找整数 re.findall()，查找 '[0-9]+' 的正则表达式，然后将提取的字符串转换为整数并对整数求和。
import re
import sys

def sum_integers_in_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        integers = re.findall('[0-9]+', text)
        return sum(int(i) for i in integers)


def main():
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        # 获取用户输入的文件名
        filename = input("请输入要处理的文件名: ")
    
    try:
        # 调用函数计算数字之和
        total = sum_integers_in_file(filename)
        print(f"文件中所有整数的和为: {total}")
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{filename}'")
    except PermissionError:
        print(f"错误: 没有权限访问文件 '{filename}'")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")


if __name__ == "__main__":
    main()
