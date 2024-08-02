Q:
     To accept and add up  five amounts and display the result to the nearest amount in rupees.
Here's the code:
     import math
amt1=float(input("enter the first amount"))
amt2=float(input("enter the second amount"))
amt3=float(input("enter the 3rd number"))
amt4=float(input("enter the 4th number"))
amt5=float(input("enter the 5th number"))
sum=amt1+amt2+amt3+amt4+amt5
temp=sum+0.5
print(f"{amt1},{amt2},{amt3},{amt4},{amt5} is ={sum}")
print(f"Rs {sum} can be rounded as Rs {math.floor(sum)}")
