'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.


'''


class Dog:
    def __init__(self, name, color, age, is_hungry=False, percent_full=100):
        """
        This dog class defines some aspects of the dog.
        :param name: the name of the dog in string
        :param color: color of the dog in string
        :param age: a number in years
        :param is_hungry: optional, default as False
        :param percent_full: a number from 0 to 100; optional, default 100.
        """
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = is_hungry
        self.percent_full = percent_full

    def str(self):
        if self.is_hungry:
            s = "hungry"
        else:
            s = "not hungry"
        if self.age > 1:
            return print(f"{self.name} is a {self.age} years old {self.color} dog. "
                     f"It's {s}, {self.percent_full}% full.")
        elif self.age == 1:
            return print(f"{self.name} is a {self.age} year old {self.color} dog. "
                     f"It's {s}, {self.percent_full}% full.")
        else:
            return print(f"{self.name} is a {int(self.age*12)}-month old {self.color} dog. "
                     f"It's {s}, {self.percent_full}% full.")

    def sleep(self):
        self.is_hungry = True
        self.percent_full = 20
        return print(f"The dog is hungry! Only {20}% full!")

    def eat(self):
        self.is_hungry = False
        self.percent_full = 100
        return print(f"The dog is not hungry at all! ")

if __name__ == '__main__':

    lucy = Dog("Lucy","black and white", 5, False, 80)
    lucy.sleep()
    lucy.str()
    lucy.eat()


