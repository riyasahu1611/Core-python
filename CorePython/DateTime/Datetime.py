import datetime
x= datetime.datetime.now()
print(x.strftime("%B"))

x = datetime.date(2000, 11, 16)
print(x)

print(x.year)
print(x.month)
print(x.day)

print(x.strftime("%y-%m-%d"))

print(x.strftime("%B"))

print(x.strftime("%A"))