import math

import plane
import plane_equation
from coordinate import Coordinate
from plane import Plane
from tunnel import Tunnel

if __name__ == '__main__':
    plane_1 = Plane()
    plane_1.add_structure_from_excel('data/plane1.xlsx')

    plane_2 = Plane()
    plane_2.add_structure_from_excel('data/plane2.xlsx')

    avg_structure = plane_1.get_avg_structure()
    avg_structure = plane_2.get_avg_structure()

    plane_1_direction = plane_1.get_direction()
    plane_2_direction = plane_2.get_direction()

    plane_1_equation = plane_1_direction.get_plane_equation()
    plane_2_equation = plane_2_direction.get_plane_equation()

    ## TODO : Nanti diganti sama inputan luar
    plane_1.set_weakness(400, 0, 20)
    plane_2.set_weakness(-400, 0, 20)

    plane_1_equation.set_d(plane_equation.find_d(plane_1_equation, plane_1.get_weakness()))
    plane_2_equation.set_d(plane_equation.find_d(plane_2_equation, plane_2.get_weakness()))

    print(plane_1_equation)
    print(plane_2_equation)

    print('no. 3')

    intersection_point = plane_equation.get_interection_point(plane_2_equation, plane_2_equation)
    print(intersection_point)

    print('no. 4')

    ## TODO : Ntar dirubah input
    first = Coordinate(424.3, 0, 10)
    second = Coordinate(-424.3, 0, 10)

    tunnel = Tunnel(first, second)
