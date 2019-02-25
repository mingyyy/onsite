'''
Write the necessary code to display the follow message to the console
Challenge: write code to duplicate the "co-" part
instead of writing it 3 times.

Time for co-co-co-ding.

'''
# method 1
print("Time for " + 'co-'*3 + "ding")

# method 2
# x = ""
# for i in range(3):
#     x = x + 'co-'
# print("Time for " + x + "ding")
# print(f"Time for {x}ding")
#
# a = 'coding'
# b = str(a[-4:])
#
# print(b)

# command + /

'''
lower case
uppercase
title-case: capital each word
capitalize: capital first word
split
'''
# my_string = "  hELLo there   "
# # lower
# print(my_string.lower())
# # upper
# print(my_string.upper())
# # title
# print(my_string.title())
# # capital
# print(my_string.capitalize())
# # trim the string
# print(my_string.strip())
# print(my_string.strip('e'))
# print(my_string.rstrip())


c = "-"
print("Time for "+ c.join(["co","co","co"])+ "-ding")

# breaking into new line
print("hello\nthere")
# introduce space between words = 1
print(len("\t"))
print("hello\tthere")
