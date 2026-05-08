dict = {'name': 'riya', 'age': 24, 'city': 'indore'}

dict.setdefault('salary', 10000)
print(dict)

dict.update({'incentives': 200000})
print(dict)
#
# dict.clear()
# print(dict)
#
# new_dict = dict.copy()
# print("new_dict:", dict)
#
# print(len(dict))
#
# for i in dict.items():
#     print(i, dict)

dict.pop('age')
print(dict)

# dict.popitem()
# print("remove last item from the dict:", dict)
#
# dict.update({'behaviour':'good'})
# print(dict)
#
# dict.setdefault('behaviour','bad')
# print(dict)
#
print(dict.keys())

print(dict.values())

print(dict.get('age'))


