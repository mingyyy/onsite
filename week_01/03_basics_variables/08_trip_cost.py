'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
try:
    distance = int(input("Please enter the miles of your drive:"))
    MPG = int(input("Please enter the Mile per Gallon of your card:"))
    Price = int(input("Please enter the price per gallon of fuel:"))
except ValueError as err:
    print("Sorry... you need to enter it again. ", err)

cost = (distance / MPG) * Price

print(f"The total cost of the trip is {cost}.")
