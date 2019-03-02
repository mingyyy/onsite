'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''


class Point:
    """Represents a point in 2-D space, an ordinate system
    defines x as the variable in x-axis
    y as the variable in y-axis
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        if (self.x, self.y) == (0,0):
            return "A point in origin."
        elif self.x > 0 and self.y > 0:
            return f"A point in quadrant 1, with the coordinate ({self.x}, {self.y})."
        elif self.x > 0 > self.y:
            return f"A point in quadrant 4, with the coordinate ({self.x}, {self.y})."
        elif self.x < 0 < self.y:
            return f"A point in quadrant 2, with the coordinate ({self.x}, {self.y})."
        elif self.x < 0 and self.y < 0:
            return f"A point in quadrant 3, with the coordinate ({self.x}, {self.y})."

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def line(self, other):
        if self.x == other.x:
            s = "vertical line"
        elif self.y == other.x:
            s = "horizontal line"
        elif (self.y < other.y and self.x < other.x) or (other.y < self.y and other.x < self.x):
            s = "0 - 90 degree line"
        else:
            s = "90 - 180 degree line"
        return s


# Point(x, y)
p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(-1, -1)
p4 = Point(-5, 6)

print(p1, p2, p3)

print(p1.distance(p2))
print(p1.distance(p3))
print(p2.distance(p2))
print(p3.distance(p2))

print(p1.line(p2))
print(p2.line(p4))

class Rectangle:
    '''
    four corners of the rectangle are defined as c1, c2, c3, c4, where c1 = left down
    c2 = left up, c3 = right up, c4 = right down
    c is the center point
    '''
    def __init__(self, width, length, leftdown=[0,0]):
        self.width = width
        self.length = length
        self.leftdown = leftdown

    def area(self):
        return self.width * self.length

    def circumference(self):
        return 2*(self.width+self.length)

    def find_center(self, v_h = True):
        if v_h is False:
            x = Point(self.leftdown[0] + self.length/2, self.leftdown[1] + self.width/2)
        else:
            x = Point(self.leftdown[0] + self.width/2, self.leftdown[1] + self.length/2)
        return x


r = Rectangle(2, 3, [0,0])
print(r.find_center())
