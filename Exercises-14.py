 Q:
    To compute mean and standard deviation of three number a,b and c.(mean=(a+b+c)/3,and SD=sqrt((a-m)^2+(b-m)^2+(c-m)^2)/3.
here's the code:
import math
a=float(input("enter the first  numbers"))
b=float(input("enter the second numebr"))
c=float(input("enter the third number"))
m=(a+b+c)/3         #m=mean sd=standard deviation
sd=math.sqrt((math.pow((a-m),2)+math.pow((b-m),2)+math.pow((c-m),2))/3)
print(f" average of {a},{b},{c} is {m}")
print(f"standard deviation of {a}, {b},{c}  ,is {sd}")
