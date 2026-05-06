n = 8
count = 0

for i in range (2, n):
    if n % i == 0:
        count += 1

if count > 0:
    print ("not prime number")
else:
    print("prime number")