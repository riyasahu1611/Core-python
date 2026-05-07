# numbers = [100, 10, 11, 5, 13, 17, 88]
# highest = 0
# second_highest = 0
#
# for num in numbers:
#     if num > highest:
#         second_highest = highest
#         highest = num
#
#     elif num > second_highest and num != highest:
#         second_highest = num
#
# print("Highest number is:", highest)
# print("Second highest number is:", second_highest)


numbers = [200, 400, 600, 800, 1000]
highest = 0
second_highest = 0
i = 0

for i in numbers:
    if i > highest:
        second_highest = highest
        highest = i

    elif i > second_highest and i != highest:
        second_highest = i

print("highest number is:", highest)
print("second highest number is:", second_highest)
