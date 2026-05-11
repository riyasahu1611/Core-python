import datetime

dob = datetime.date(2004, 11, 30)
today = datetime.date.today()

age = today.year - dob.year
dayname= dob.strftime("%A")

print("My age is:", age)
print("Birth Day is:", dayname)
