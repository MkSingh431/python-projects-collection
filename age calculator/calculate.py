from datetime import datetime, date

def calculate_age(birth_date, current_date):
    age_years = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age_years -= 1
    
    age_months = (current_date.year - birth_date.year) * 12 + current_date.month - birth_date.month
    if current_date.day < birth_date.day:
        age_months -= 1
    
    age_days = (current_date - birth_date).days
    
    return age_years, age_months, age_days

name = input("Please enter your name: ")
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))

birth_date = date(birth_year, birth_month, birth_day)
current_date = date.today()

years, months, days = calculate_age(birth_date, current_date)

print(f"\n\t{name}'s age is {years} years or {months} months or {days} days")
