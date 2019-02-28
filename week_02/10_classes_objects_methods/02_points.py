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
            return "A point in quadrant 1."
        elif self.x > 0 and self.y < 0:
            return "A point in quadrant 4."
        elif self.x < 0 and self.y > 0:
            return "A point in quadrant 2."
        elif self.x < 0 and self.y < 0:
            return "A point in quadrant 3."

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return ((self.x, self.y) <= (other.x, other.y))

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
