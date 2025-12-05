import re

filename = input("请输入要处理的文件名: ")

with open(filename, 'r') as f:
    ftext = f.read()

integers = re.findall('[0-9]+', ftext)
print(sum(int(i) for i in integers))