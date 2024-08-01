Q:
     To convert a given number of days to a measure of time given in years,weeks and days.for example 375 is equals to 1 year,1 week,3 days
 
Here's the code
    days=int(input("enter the days"))
temp=days
year=int(days/365)
days=days%365
week=int(days/7)
day=days%7


print(f"{temp} is equal to {year} year ,{week} week ,{day} days")
