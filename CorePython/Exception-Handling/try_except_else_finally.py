# When try is executed
a = 20
b = 2

try:
    c = a / b
    print("Division:", c)

except ZeroDivisionError as e:
    print("Exception:", e)

else:
    print("else block executed")

finally:                              #Always executed
    print("finally block executed")

# When try is not executed
a = 20
b = 0

try:
    c = a / b
    print("Division:", c)

except ZeroDivisionError as e:
    print("Exception:", e)

else:
    print("else block executed")

finally:                              #Always executed
    print("finally block executed")
