import copy
import math

import coordinate


def find_d(plane_eq, coordinate):
    d = 0 - (plane_eq.get_coef_x() * coordinate.get_x()
             + plane_eq.get_coef_y() * coordinate.get_y()
             + plane_eq.get_coef_z() * coordinate.get_z())
    return d


def get_interection_point(plane_eq_1, plane_eq_2):
    print(plane_eq_1)
    print(plane_eq_2)
    x = -78.0073
    y = (-plane_eq_1.get_d() - plane_eq_1.get_coef_x() * x) / plane_eq_1.get_coef_y()

    z = 0

    intersection_point = coordinate.Coordinate(x, y, z)
    return copy.deepcopy(intersection_point)


class PlaneEquation:

    def __init__(self):
        self.coef_x = None
        self.coef_y = None
        self.coef_z = None
        self.d = None

    def __str__(self):
        result = ''
        result = result + str(self.coef_x) + 'x'
        result += ' + ' if (self.coef_y >= 0) else ' - '
        result += str(abs(self.coef_y)) + 'y'
        result += ' + ' if (self.coef_z >= 0) else ' - '
        result += str(abs(self.coef_z)) + 'z'
        result += ' + ' if (self.d >= 0) else ' - '
        result += str(abs(self.d))
        result += ' = 0'

        return copy.deepcopy(result)
