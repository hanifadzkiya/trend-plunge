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
        self._coef_x = None
        self._coef_y = None
        self._coef_z = None
        self._d = None

    def get_coef_x(self):
        return self._coef_x

    def get_coef_y(self):
        return self._coef_y

    def get_coef_z(self):
        return self._coef_z

    def get_d(self):
        return self._d

    def set_coef_x(self, coef_x):
        self._coef_x = coef_x

    def set_coef_y(self, coef_y):
        self._coef_y = coef_y

    def set_coef_z(self, coef_z):
        self._coef_z = coef_z

    def set_d(self, d):
        self._d = d

    def __str__(self):
        result = ''
        result = result + str(self._coef_x) + 'x'
        result += ' + ' if (self._coef_y >= 0) else ' - '
        result += str(abs(self._coef_y)) + 'y'
        result += ' + ' if (self._coef_z >= 0) else ' - '
        result += str(abs(self._coef_z)) + 'z'
        result += ' + ' if (self._d >= 0) else ' - '
        result += str(abs(self._d))
        result += ' = 0'

        return copy.deepcopy(result)
