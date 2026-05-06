"6.Find whether a given year is a leap year or not."
# -------- INPUT DATE --------
day = int(input("Enter day: "))
month = input("Enter month name (e.g., February): ")
year = int(input("Enter year: "))
# -------- BASIC VALIDATION --------
if day <= 0 or year <= 0:
    print("Day and Year must be positive numbers.")
else:
    # -------- CHECK LEAP YEAR --------
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        print(year, "is a Leap Year.")
    else:
        leap = False
        print(year, "is NOT a Leap Year.")
    # -------- DAYS IN MONTH --------
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        days_in_month = 31
    elif month == "April" or month == "June" or month == "September" or month == "November":
        days_in_month = 30
    elif month == "February":
        if leap:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        print("Invalid month name.")
        days_in_month = 0
    # -------- DATE VALIDATION --------
    if days_in_month != 0:
        if day > days_in_month:
            print("Invalid date for", month)
        else:
            print("Days in", month, "=", days_in_month)
            # -------- COUNT NEXT 700 DAYS --------
            future_year = year
            days_left = 700
            while days_left > 0:
                if (future_year % 4 == 0 and future_year % 100 != 0) or (future_year % 400 == 0):
                    year_days = 366
                else:
                    year_days = 365

                if days_left >= year_days:
                    days_left = days_left - year_days
                    future_year = future_year + 1
                else:
                    break

            print("After 700 days, the year will be:", future_year)

            # Check leap for future year
            if (future_year % 4 == 0 and future_year % 100 != 0) or (future_year % 400 == 0):
                print(future_year, "is a Leap Year.")
            else:
                print(future_year, "is NOT a Leap Year.") 