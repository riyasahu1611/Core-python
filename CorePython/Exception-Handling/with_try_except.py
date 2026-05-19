print("before")

a = 30
b = 0

print("mid")

try:
    c = a / b
    print("Division:", c)
except ZeroDivisionError as e:
    print("Exception:", e)

print("After")
