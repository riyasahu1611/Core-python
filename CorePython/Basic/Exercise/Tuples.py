t1 = (30, 50, 70, 30, 90)
t2 = (1, 2, 3, 3, 4, 5, 6)

print(tuple(t1))

print(max(t1))
print(max(t2))
print(len(t2))

t3 = t1 + t2
print(t3)

t3 = t1.index(70)
print("70 lies on position:", t3)

t3 = t1.count(30)
print("count is:", t3)

t3= len(t2)
print("len is:", t3)