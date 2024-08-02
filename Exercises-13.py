Q:
    To accept a four digit number and display the sum of its individual digits.


Here's the code:
     
number=int(input("enter the 4 digit number"))
temp=number
n1=int(number/1000)
number=number%1000
n2=int(number/100)
number=number%100
n3=int(number/10)
n4=number%10
sum=n1+n2+n3+n4
print(f"sum of the individual digits of {temp} is {sum}" )
