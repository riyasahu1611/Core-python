import datetime

dob = datetime.date(2000, 11, 16)
today = datetime.date.today()

age = today.year - dob.year
dayName = dob.strftime("%A")

print(" My  age is :- ", age)
print("Dob Day is: ",dayName)
