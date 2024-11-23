# 提示用户输入文件名
file_name = input("Please enter the file name: ")

# 用于记录符合条件的行数，初始化为0
count = 0
# 用于累加提取出的浮点数的值，初始化为0
total = 0

try:
    # 打开用户输入的文件，以只读模式('r')打开
    with open(file_name, 'r') as file:
        # 遍历文件中的每一行
        for line in file:
            # 如果该行以 "X-DSPAM-Confidence:" 开头，说明是我们要处理的行
            if line.startswith("X-DSPAM-Confidence:"):
                # 符合条件的行数加1
                count += 1
                # 找到冒号（":"）在该行中的位置，再加1，得到浮点数开始的位置
                start_pos = line.find(":") + 1
                # 使用字符串切片从刚才找到的位置开始提取出数字字符串
                num_str = line[start_pos:].strip()
                # 将提取出的数字字符串转换为浮点数
                num_float = float(num_str)
                # 将转换后的浮点数累加到total中
                total += num_float

    # 如果找到了符合条件的行（count大于0）
    if count > 0:
        # 计算平均 spam confidence值，即总和除以行数
        average = total / count
        print(f"Average spam confidence: {average}")
    else:
        print("No lines with X-DSPAM-Confidence were found.")

# 如果文件未找到，捕获FileNotFoundError异常并打印相应提示信息
except FileNotFoundError:
    print(f"Sorry, the file '{file_name}' was not found.")