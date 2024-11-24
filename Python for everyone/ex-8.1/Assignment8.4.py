fname = input("Enter file name: ")
fh = open(fname)
word_list = []
for line in fh:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)
word_list.sort()
print(word_list)