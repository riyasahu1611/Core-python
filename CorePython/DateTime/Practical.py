from datetime import *

# x = date.today()
# next_month = x
# for i in range(1,13):
#     next_month = next_month + timedelta(days=30)
#     print("Month = ",i,"Date = ",next_month)

x= date.today()
next_month= x
for i in range(1,13):
    next_month = next_month + timedelta(days=1)
    print("Month = ", i, "Date = ",next_month)