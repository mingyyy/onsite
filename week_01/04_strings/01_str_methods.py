'''
There are many string methods available to perform all sorts of tasks.

Experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

Python documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

For this exercise, demonstrate the following string methods below:
- strip
- replace
- find

'''
# strip: taking out things from both sides
# lstrip: from left side only
# rstrip: from right side only

testing = "  what a wonderful day!"
# strip default - space
testing_strip_default = testing.strip()
# strip - characters
testing_strip_char = testing.strip(' w')

print(testing)
print(testing_strip_default)
print(testing_strip_char)

# replace
testing_replace = testing.replace("w", "M")
testing_replace1 = testing.replace("w", "M", 1)
testing_replace_space = testing.replace(" ", "*")

print(testing_replace)
print(testing_replace1)
print(testing_replace_space )

# find: return the location of the first target from left(index)
# rfind: return the location of the first target from right(index)
testing_find = testing.find("w")
testing_find1=testing.rfind("w")
testing_find2 = testing.find("w", 5, 10) # the starting and ending numbers constrains where find works

print(testing_find)
print(testing_find1)
print(testing_find2)