'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
nums = range(1, 1000000)
gen = (x for x in nums if x % 1111 == 0)
for i in gen:
    print(i // 1111)
