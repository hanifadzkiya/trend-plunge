import copy
import math

from plane_equation import PlaneEquation


def find_s(first, second):
    return math.sqrt(
        math.pow(second.get_x() - first.get_x(), 2)
        + math.pow(second.get_y() - first.get_y(), 2)
        + math.pow(second.get_z() - first.get_z(), 2)
    )


def get_intersection(vector_1, vector_2, vector_3):
    k = (vector_3.c - vector_3.a / vector_1.a * vector_1.c) / (vector_2.c - vector_2.a / vector_1.a * vector_1.c)
    y = (
                    vector_3.a / vector_1.a * vector_1.d - vector_3.d - k * vector_2.a / vector_1.a * vector_1.d + k * vector_2.d) / (
                    k * vector_2.a / vector_1.a * vector_1.b - k * vector_2.b + vector_3.b - vector_3.a / vector_1.a * vector_1.b)
    z = (
                    vector_2.a / vector_1.a * vector_1.b * y + vector_2.a / vector_1.a * vector_1.d - vector_2.b * y - vector_2.d) / (
                    vector_2.c - vector_2.a / vector_1.a * vector_1.c)
    x = -(vector_1.b * y + vector_1.c * z + vector_1.d) / vector_1.a

    return copy.deepcopy(Coordinate(x, y, z))


class Coordinate:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_plane_equation(self) -> PlaneEquation:
        plane_equation = PlaneEquation()

        plane_equation.set_coef_x(self.x)
        plane_equation.set_coef_y(self.y)
        plane_equation.set_coef_z(self.z)

        return copy.deepcopy(plane_equation)

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
