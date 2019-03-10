'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.
'''
# some_file.py
import sys
# sys.path.insert(0, '/Users/Ming/Documents/CodingNomads/python-onsite/week_02/10_classes_objects_methods')


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


class Shepherd(Dog):
    def __init__(self, name, color, age, is_hungry, percent_full, training= True, breed="German Shepherd", origin = "german"):
        super().__init__(name, color, age, is_hungry, percent_full)
        self.training = training
        self.breed = breed
        self.origin = origin

    def sleep(self):
        if self.training is True:
            self.is_hungry = True
            self.percent_full = max(0, self.percent_full-20)
            return f"The {self.breed} is in training and is {self.percent_full}% full!"
        else:
            self.is_hungry = False
            self.percent_full = max(0, self.percent_full-10)
            return f"The {self.breed} is not in training and is {self.percent_full}% full!"

    def eat(self):
        if self.training is True:
            self.is_hungry = False
            self.percent_full = 95
            return f"The {self.breed} is in training and is only {self.percent_full}% full!"
        else:
            self.is_hungry = False
            self.percent_full = 100
            return f"The {self.breed} is not in training and is completely full!"


if __name__ == '__main__':

    # lucy = Dog("Lucy","black and white", 5, False, 80)
    # lucy.sleep()
    # lucy.str()
    # lucy.eat()

    fred = Shepherd("Fred", "Black", "2", False, 50)
    print(fred.sleep())
    print(fred.eat())
    print(fred.color)
