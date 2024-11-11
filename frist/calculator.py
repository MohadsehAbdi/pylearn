
import math
#ورودی ها
#input
a = int(input())
b = int(input())
operator = input()

#پردازش
#process

if operator == "+":
    result = a + b 
elif operator == "-":
    result = a - b 
elif operator == "*":
    result = a * b 
elif operator == "/":
    if b != 0:
         result = a / b
    else:
        result = "cannot divide by zero" 
elif operator == "^":
   # result = a ** b
   result = math.pow(a , b)
elif operator == "kmm":
    result = math.lcm(a , b)
else:
    result = "this operator not supported😐"
#خروجی
#out put
print(result)
 