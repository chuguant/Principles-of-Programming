# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt
import copy

class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y
            
    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        if sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)\
           + sqrt((point_2.x - point_3.x)**2 + (point_2.y - point_3.y)**2)\
           <= sqrt((point_1.x - point_3.x)**2 + (point_1.y - point_3.y)**2)\
           or sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)\
           + sqrt((point_1.x - point_3.x)**2 + (point_1.y - point_3.y)**2)\
           <= sqrt((point_2.x - point_3.x)**2 + (point_2.y - point_3.y)**2)\
           or sqrt((point_2.x - point_3.x)**2 + (point_2.y - point_3.y)**2)\
           + sqrt((point_1.x - point_3.x)**2 + (point_1.y - point_3.y)**2)\
           <= sqrt((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2):
            raise TriangleError('Incorrect input, triangle not created.')
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        # Replace pass above with your code

    def change_point_or_points(self, *, point_1 = None, point_2 = None, point_3 = None):
        if point_1 is not None:
            point_1_copy = copy.deepcopy(self.point_1)
            self.point_1 = point_1
            if Triangle.triangle_exist(self) == False:
                self.point_1 = point_1_copy
                print('Incorrect input, triangle not modified.')
        if point_2 is not None:
            point_2_copy = copy.deepcopy(self.point_2)
            self.point_2 = point_2
            if Triangle.triangle_exist(self) == False:
                self.point_2 = point_2_copy
                print('Incorrect input, triangle not modified.')
        if point_3 is not None:
            point_3_copy = copy.deepcopy(self.point_3)
            self.point_3 = point_3
            if Triangle.triangle_exist(self) == False:
                self.point_3 = point_3_copy
                print('Incorrect input, triangle not modified.')
        # Replace pass above with your code

    # Possibly define other methods
    def count_area(self):
        return 0.5 * abs(self.point_1.x * (self.point_2.y - self.point_3.y) +\
                         self.point_2.x * (self.point_3.y - self.point_1.y) +\
                         self.point_3.x * (self.point_1.y - self.point_2.y))

    def count_perimeter(self):
        return sqrt((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2) + \
               sqrt((self.point_2.x - self.point_3.x)**2 + (self.point_2.y - self.point_3.y)**2) + \
               sqrt((self.point_1.x - self.point_3.x)**2 + (self.point_1.y - self.point_3.y)**2)

    def triangle_exist(self):
        if sqrt((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2)\
           + sqrt((self.point_2.x - self.point_3.x)**2 + (self.point_2.y - self.point_3.y)**2)\
           <= sqrt((self.point_1.x - self.point_3.x)**2 + (self.point_1.y - self.point_3.y)**2)\
           or sqrt((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2)\
           + sqrt((self.point_1.x - self.point_3.x)**2 + (self.point_1.y - self.point_3.y)**2)\
           <= sqrt((self.point_2.x - self.point_3.x)**2 + (self.point_2.y - self.point_3.y)**2)\
           or sqrt((self.point_2.x - self.point_3.x)**2 + (self.point_2.y - self.point_3.y)**2)\
           + sqrt((self.point_1.x - self.point_3.x)**2 + (self.point_1.y - self.point_3.y)**2)\
           <= sqrt((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2):
            return False
        else:
            return True
    area = property(count_area)
    perimeter = property(count_perimeter)



