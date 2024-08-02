Q:
     To accept aan amount in rupees and calculate and display the number of currency notes for each denomination 1000,500,200,100,50,20,10,5,2,1,such that the total  number of currency notes will be at minimum ,Also ouput the total number of currency notes.

  Here's the code:
      amt=int(input("enter the amount"))
temp=amt
n1000=int(amt/1000)
amt=amt%1000
n500=int(amt/500)
amt=amt%500
n200=int(amt/200)
amt=amt%200
n100=int(amt/100)
amt=amt%100
n50=int(amt/50)
amt=amt%50
n20=int(amt/20)
amt=amt%20
n10=int(amt/10)
amt=amt%10
n5=int(amt/5)
amt=amt%5
n2=int(amt/2)
n1=amt%2
total=n1000+n500+n100+n50+n200+n20+n10+n5+n2+n1
print (f"Total currency note and coins is {total}")
print(f"Rs {temp} contain {n1000} 1000 rupees notes")
print(f"Rs {temp} contain {n500} 500 rupees notes")
print(f"Rs {temp} contain {n200} 200 rupees notes")
print(f"Rs {temp} contain {n100} 100 rupees notes")
print(f"Rs {temp} contain {n50} 50 rupees notes")
print(f"Rs {temp} contain {n20} 20 rupees notes")
print(f"Rs {temp} contain {n10} 10 rupees notes")
print(f"Rs {temp} contain {n5} 5 rupees notes")
print(f"Rs {temp} contain {n2} 2 rupees coin")
print(f"Rs {temp} contain {n1} 1 rupees notes")
