list1 = ['a', 100, 'abc', 100.1, True, 4, 4]
list2 = [1, 2, 3, 4, 5]

# print(list2)
# print(type(list2))
#
# print(list1[4])

print(list1[0:3])

print(list1[1:4])

print(list1[2:])

list1.append('python')
print(list1)

list1.insert(0, 'java')
print(list1)

list1.remove(100.10)
print(list1)
#
list2.sort()
print(list2)

list3=list1+list2
print(list3)

list = list1. count('abc')
print(list)

list = list1. index('abc')
print(list)