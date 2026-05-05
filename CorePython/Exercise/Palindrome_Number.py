number = 151
n = number
sum = 0
r = 0

while n > 0:
    r = n % 10
    sum = ( sum * 10 ) + r
    n = n // 10

if sum == number:
    print("palindrome number", number)
else:
    print("not palindrome")