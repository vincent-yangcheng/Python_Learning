hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Pay Rate:")
r = float(rate)
if hrs < 40:
    pay = hrs * rate
else :
    pay = hrs * rate * 1.5
print (pay)