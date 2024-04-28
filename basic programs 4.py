Write a  Python program that prints the calendar for a given month and year.


  # Import the 'calendar' module
import calendar

# Prompt the user to input the year and month
year = int(input("Input the year : "))
month = int(input("Input the month : "))

# Print the calendar for the specified year and month
print(calendar.month(year, month))
