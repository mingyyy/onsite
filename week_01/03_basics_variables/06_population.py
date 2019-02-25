'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

# 120 = 6 * 20 = 12 * 10 = 40 * 3
# + 20 - 10 + 3

pop_now = 380123456
sec_per_yr = 60 * 60 * 24 * 365
pop_3yr = pop_now + (sec_per_yr / 120) * (120/6 - 120/12 + 120/40) * 3

print(format(pop_3yr,"," ))

