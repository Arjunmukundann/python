Find Maximum of two numbers


def max(num1,num2):
    if num1>num2:
        print(num1,"is greater than",num2)
    elif num1==num2:
        print(num1,",",num2,"are equal")
    else:
        print(num2,"is greater than",num1)
        return max
num1=int(input("enter your first number")) 
num2=int(input("enter your second number"))
max(num1,num2)
