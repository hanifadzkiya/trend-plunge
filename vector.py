import copy
import math


def get_normal_vector(linear, tersingkap):
    a = math.sin(linear.trend) * math.cos(linear.plunge)
    b = math.cos(linear.trend) * math.cos(linear.plunge)
    c = -math.sin(linear.plunge)

    d = -(a * tersingkap.x + b * tersingkap.y + c * tersingkap.z)

    return copy.deepcopy(Vector(a, b, c, d))


class Vector:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return 'a : ' + str(self.a) + \
               '\nb : ' + str(self.b) + \
               '\nc : ' + str(self.c) + \
               '\nd : ' + str(self.d)
