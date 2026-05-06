"7.Write a program which takes any date as input and display next date of the calendar."
print("Press Enter to use default date (20/9/2005)")

day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")

day = int(day or 20)
month = int(month or 9)
year = int(year or 2005)

# Step 1: Check Leap Year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

# Step 2: Days in month
if month == 2:
    if leap:
        max_days = 29
    else:
        max_days = 28
elif month in (4, 6, 9, 11):
    max_days = 30
else:
    max_days = 31

# Step 3: Find Next Date
day += 1

if day > max_days:
    day = 1
    month += 1

    if month > 12:
        month = 1
        year += 1

print("Next Date is:")
print("Day =", day)
print("Month =", month)
print("Year =", year)



