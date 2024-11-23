# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0

fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count +1
        start_pos = line.find(":") + 1
        num_str = line[start_pos:].strip()
        num_float = float(num_str)
        total += num_float
if count > 0:
    average = total / count
    print ("Average spam confidence:",average)