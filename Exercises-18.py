Q:
   Write a python program in which the user enters either'A','B' or 'C' .If 'A' is entered, the program should display the word 'Apple';if 'B' is entered , it display 'Banana'; and if;'C' is entered ,it display 'coconut'


Here's the code:

    list=['a','A','b','B','c','C']
a=input("enter the A,B,C")
while (a not in  list):
   a=input("invalid input.Enter the A,B or C ")
if(a=='a' or a=='A'):
    print("Apple")
if(a=='b' or a=='B'):
    print("Banana")
if(a=='c'or a=='C'):
    print("Coconut")    
