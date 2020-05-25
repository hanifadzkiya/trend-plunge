import copy
import math

from plane_equation import PlaneEquation


def find_s(first, second):
    return math.sqrt(
        math.pow(second.get_x() - first.get_x(), 2)
        + math.pow(second.get_y() - first.get_y(), 2)
        + math.pow(second.get_z() - first.get_z(), 2)
    )


class Coordinate:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def get_plane_equation(self) -> PlaneEquation:
        plane_equation = PlaneEquation()

        plane_equation.set_coef_x(self._x)
        plane_equation.set_coef_y(self._y)
        plane_equation.set_coef_z(self._z)

        return copy.deepcopy(plane_equation)

    def __str__(self) -> str:
        return '(' + str(self._x) + ', ' + str(self._y) + ', ' + str(self._z) + ')'
