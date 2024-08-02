Q:
   To round off a floating-point number to the nearest integer.(Hint:add 0.5 to the number and truncate)


Here's the code


import math
num=float(input("enter the number"))
temp=num+0.5
print(f"{num} can be rounded to {math.floor(temp)}")
