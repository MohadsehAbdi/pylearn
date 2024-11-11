n = int(input("enter a number:"))

a = 0
b = 1

count = 0

if n < 0:
    print("inncorrect number")

if n == 0:
    print()

if n > 0:
    print(a, end=",")
    count += 1

while count < n:
    print(b, end=",")
    count += 1
    next_number = a + b 
    a = b 
    b = next_number