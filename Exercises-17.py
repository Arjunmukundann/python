Q:
   To input 3 numbers and to  display the biggest and smallest  among them.
Here's the code:
 n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the 3rd number"))
big=n1
small=n1
if(big<n2):
    big=n2
if big<n3:
    big=n3;
if (small>n2):
    small=n2
if (small>n3):
    small=n3        

print(big,"is the biggest among ",n1,n2,n3)        
print(small,"is the smallest among ",n1,n2,n3)    
