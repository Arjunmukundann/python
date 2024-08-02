Q:
       To accept the principal amount,rate of interest and number of years and calculate and display the simple and compound interrest .(simple interest=PNR,compound interest=A-P where a=P(1+R)^N)

Here's the code:
       #P-principal amount
#R-rate of interest
 #N-number of years
#S-simple interest
#C-compound interest
import math
P=float(input("enter the principal amount"))
R=float(input("enter the rate of interest"))
R=R/100
N=float(input("enter the number of years"))
s=P*N*R
c=P*math.pow((1+R),N)-P
print(f"simple interest is {s}")
print(f"compound interes is {c}")
