largest = None
smallest = None

while True:
    numstr = input("Enter a number: ")
    if numstr == "done":
        break
    try:
        num = int(numstr)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print ("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)