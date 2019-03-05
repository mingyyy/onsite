'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

'''
1. function calculate the area of a circle(radius) => output the area as a number up to 2 decimal.
2. 
test case 1: radius = negative number, return: warning and error message "can't be negative"
test case 2: radius = string, return: error message "can only be positive number!"
test case 3: radius = symbols, return: error message "can only be positive number!"
test case 4: radius = 5.34, return: 89.58
test case 5: radius = 2.4333, return 18.60
'''

'''
1. function take in an absolute file name and returns if the file is duplicated in your computer.
If you have a duplication, return True; otherwise, False
2. 
test case 1: give a relative file name/misspelled file name/extra spaces, return: warning message telling you "File can't be find, check the path."
test case 2: give a file name in a restricted folder, return: permission error telling you to check permissions.
test case 3: give an empty string/numbers, return: wrong input error messages prompt you re-enter a valid path.
test case 4: enter a valid absolute file name which has no duplicates, return: False
test case 5: enter a valid absolute file name which has just one duplicate, return: True
test case 6: enter a valid absolute file name which has just many duplicates, return: True
'''