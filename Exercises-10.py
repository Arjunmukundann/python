Q:
         To round off a floating -pointerto its nearest tenths and hundreds. 

    
    Here's the code:
         number=float(input("enter the number"))
tenth=int((number+5)/10)*10
hundredth=int((number+50)/100)*100
print(f"{tenth}")
print(f"{hundredth}")
