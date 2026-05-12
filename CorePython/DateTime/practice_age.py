# import datetime
#
# dob = datetime.date(2004, 11, 30)
# today = datetime.date.today()
#
# age = today.year - dob.year
# dayname= dob.strftime("%A")
#
# print("My age is:", age)
# print("Birth Day is:", dayname)


import datetime

dob = datetime.date(2000, 11, 16)
today = datetime.date.today()

age = today.year - dob.year
dayname = dob.strftime("%A")

print("My age is:", age)
print("My birth day is:", dayname)



import datetime

dob = datetime.date(2000, 11, 16)
today = datetime.date.today()

age = today.year - dob.year
dayname = dob.strftime("%A")

print(age)
print(dayname)
