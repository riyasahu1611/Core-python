from datetime import date,timedelta
CurrentStatus= date.today()
print("Current Date= ",CurrentStatus.day)
print("Current Month = ",CurrentStatus.month)
print("Current Year = ", CurrentStatus.year)
print("Current Day = ", CurrentStatus.day)

tomorrowDate= CurrentStatus+timedelta(days=1)
print("Tomorrow Date is =", tomorrowDate)

aftertomorrow=tomorrowDate+timedelta(days=2)
print("After tomorrow Date = ",aftertomorrow)

previousDate=CurrentStatus-timedelta(days=4)
print("Previous Date = ",previousDate)

print(CurrentStatus.strftime("%d-%m-%y"))

print(previousDate.strftime("%d-%m-%y"))