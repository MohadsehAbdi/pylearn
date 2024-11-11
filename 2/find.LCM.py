a = int(input())
b = int(input())

for i in range(b, a*b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i 
        break

print(lcm)

    
