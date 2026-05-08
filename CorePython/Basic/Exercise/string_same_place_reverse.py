name = "Riya Sahu"
words = name.split()  # ['Riya', 'Sahu']

for word in words:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")


# name = "Harshit Sahu"
# words = name.split()
#
# for word in words:
#     reversed_word = ""
#     for char in word:
#         reversed_word = char + reversed_word
#     print(reversed_word, end=" ")

