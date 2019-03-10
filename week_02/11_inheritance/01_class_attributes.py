'''
Flush out the classes below with the following:
    - Add inheritance so that Class1 is inherited by Class2 and Class2 is inherited by Class3.
    - Follow the directions in each class to complete the functionality.
'''
from datetime import date as d


# define an __init__() method that sets an attribute x
class CodingnomadsStaff:
    '''
    :param max_size is the max number of students allowed in a class
    :param start_date is default as today
    :param length is the length of the course
    :param topic is what the class talks about
    '''
    instructors = ["martin", "roi", "caden"]

    def __init__(self, topic, max_size=12, start_date=d.today(), length=90):
        self.max_size = max_size
        self.start_date = start_date
        self.length = length
        self.topic = topic

    def __str__(self):
        return f"Codingnomads has {len(self.instructors)} instructors. \nAnd there is a {self.topic} class starting {self.start_date} " \
            f"which takes no more than {self.max_size} students."


class Instructor(CodingnomadsStaff):

    # define an __init__() method that sets an attribute y and calls the __init__() method of its parent
    def __init__(self, topic, name, nationality, diet="tempeh"):
        super().__init__( topic)
        self.name = name
        self.nationality = nationality
        self.diet = diet

    def __str__(self):
        return f"{self.name} is a {self.topic} instructor, working with Codingnomads and eating {self.diet} only."


class Java(Instructor):

    # define an __init__() method that sets an attribute z and calls the __init__() method of its parent
    def __init__(self,topic, name, nationality, *args): # lecture = True, homework = True, test=False
        super().__init__(topic, name, nationality)
        self.args = args

    def __str__(self):
        #l = [str(i).capitalize() for i in self.args]
        return f"{self.name} from {self.nationality} has the following task for {self.topic}:{self.args}."


# create an object of each class and print each of its attributes
python = CodingnomadsStaff("Python")
print(python)

martin = Instructor("SQL", "Mr. Martin", "Austrian")
print(martin)

daily = Java("Java", "Roi", "Spain", "code review",'lecture',"exams")
print(daily)
