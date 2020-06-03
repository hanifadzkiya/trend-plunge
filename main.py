import math

import coordinate
import plane
import plane_equation
import vector
from coordinate import Coordinate
from line_equation import LineEquation
from plane import Plane
from read_excel import ReadExcel
from tunnel import Tunnel


def get_intersection_normal_vector_with_tunnel(vector_1, vector_2, roof_coor):
    e1 = vector_1.c * roof_coor.z + vector_1.d
    e2 = vector_2.c * roof_coor.z + vector_2.d

    y = (vector_2.a / vector_1.a * e1 - e2) / (vector_2.b - vector_2.a / vector_1.a * vector_1.b)
    x = (-vector_1.b * y - e1) / vector_1.a
    z = roof_coor.z

    return Coordinate(x, y, z)


def is_inside(coor, y_atas, y_bawah):
    return True if (((coor.y < y_atas) or (coor.y == y_atas)) and ((coor.y > y_bawah) or (coor.y == y_bawah))) \
        else False


def can_landslide_occure(is_inside_1, is_inside_2, is_inside_3):
    cnt_inside = 1 if is_inside_1 else 0
    cnt_inside += 1 if is_inside_2 else 0
    cnt_inside += 1 if is_inside_3 else 0

    return cnt_inside >= 2


if __name__ == '__main__':
    # Read Input
    plane_1 = Plane()
    plane_1.add_structure_from_excel('data/alldata.xlsx', 1)

    plane_2 = Plane()
    plane_2.add_structure_from_excel('data/alldata.xlsx', 2)

    plane_3 = Plane()
    plane_3.add_structure_from_excel('data/alldata.xlsx', 3)

    # Get Trend and Plunge
    avg_trend_plung_1 = plane_1.get_avg_structure().linear
    avg_trend_plung_2 = plane_2.get_avg_structure().linear
    avg_trend_plung_3 = plane_3.get_avg_structure().linear

    print('Trend Plunge Plane 1 : ')
    print(avg_trend_plung_1)
    print('Trend Plunge Plane 2 : ')
    print(avg_trend_plung_2)
    print('Trend Plunge Plane 3 : ')
    print(avg_trend_plung_3)

    # Get Tersingkap
    plane_1.add_tersingkap_from_excel('data/alldata.xlsx', 1)
    plane_2.add_tersingkap_from_excel('data/alldata.xlsx', 2)
    plane_3.add_tersingkap_from_excel('data/alldata.xlsx', 3)

    # get vector normal
    normal_vector_plane_1 = vector.get_normal_vector(avg_trend_plung_1, plane_1.tersingkap)
    normal_vector_plane_2 = vector.get_normal_vector(avg_trend_plung_2, plane_2.tersingkap)
    normal_vector_plane_3 = vector.get_normal_vector(avg_trend_plung_3, plane_3.tersingkap)

    print('---------------------------------')
    print('Normal Vector Plane 1 : ')
    print(normal_vector_plane_1)
    print('Normal Vector Plane 2 : ')
    print(normal_vector_plane_2)
    print('Normal Vector Plane 3 : ')
    print(normal_vector_plane_3)

    # Get Coordinat Intersection
    intersection_coordinate = coordinate.get_intersection(normal_vector_plane_1, normal_vector_plane_2,
                                                          normal_vector_plane_3)

    # Intersection Plane 1 Plane 2 Plane 3 dengan tunnel
    # TODO: Nama variabel ngga jelas
    read_excel = ReadExcel('data/alldata.xlsx')
    read_excel.set_sheet(5)
    roof_tunnel_coordinate = Coordinate(None, None, None)
    roof_tunnel_coordinate.z = read_excel.cell_value(1, 1)

    intersection_1_2_tunnel = get_intersection_normal_vector_with_tunnel(normal_vector_plane_1, normal_vector_plane_2,
                                                                         roof_tunnel_coordinate)
    intersection_1_3_tunnel = get_intersection_normal_vector_with_tunnel(normal_vector_plane_1, normal_vector_plane_3,
                                                                         roof_tunnel_coordinate)
    intersection_2_3_tunnel = get_intersection_normal_vector_with_tunnel(normal_vector_plane_2, normal_vector_plane_3,
                                                                         roof_tunnel_coordinate)

    # Read Line Equation from excel
    read_excel = ReadExcel('data/alldata.xlsx')
    read_excel.set_sheet(4)

    left_equation = LineEquation(read_excel.cell_value(2, 1), read_excel.cell_value(3, 1), read_excel.cell_value(4, 1))
    right_equation = LineEquation(read_excel.cell_value(2, 4), read_excel.cell_value(3, 4), read_excel.cell_value(4, 4))

    y_atas_1_2 = left_equation.get_y(intersection_1_2_tunnel.x)
    y_bawah_1_2 = right_equation.get_y(intersection_1_2_tunnel.x)
    y_atas_1_3 = left_equation.get_y(intersection_1_3_tunnel.x)
    y_bawah_1_3 = right_equation.get_y(intersection_1_3_tunnel.x)
    y_atas_2_3 = left_equation.get_y(intersection_2_3_tunnel.x)
    y_bawah_2_3 = right_equation.get_y(intersection_2_3_tunnel.x)

    is_inside_1_2 = is_inside(intersection_1_2_tunnel, y_atas_1_2, y_bawah_1_2)
    is_inside_1_3 = is_inside(intersection_1_3_tunnel, y_atas_1_3, y_bawah_1_3)
    is_inside_2_3 = is_inside(intersection_2_3_tunnel, y_atas_2_3, y_bawah_2_3)

    is_can_landslide = can_landslide_occure(is_inside_1_2, is_inside_1_3, is_inside_2_3)

    print('Dapat Terjadi Longsoran') if is_can_landslide else print('Tidak dapat terjadi longsoran')
    # avg_structure = plane_1.get_avg_structure()
    # avg_structure = plane_2.get_avg_structure()
    #
    # plane_1_direction = plane_1.get_direction()
    # plane_2_direction = plane_2.get_direction()
    #
    # plane_1_equation = plane_1_direction.get_plane_equation()
    # plane_2_equation = plane_2_direction.get_plane_equation()
    #
    # ## TODO : Nanti diganti sama inputan luar
    # plane_1.set_weakness(400, 0, 20)
    # plane_2.set_weakness(-400, 0, 20)
    #
    # plane_1_equation.set_d(plane_equation.find_d(plane_1_equation, plane_1.get_weakness()))
    # plane_2_equation.set_d(plane_equation.find_d(plane_2_equation, plane_2.get_weakness()))
    #
    # print(plane_1_equation)
    # print(plane_2_equation)
    #
    # print('no. 3')
    #
    # intersection_point = plane_equation.get_interection_point(plane_2_equation, plane_2_equation)
    # print(intersection_point)
    #
    # print('no. 4')
    #
    # ## TODO : Ntar dirubah input
    # first = Coordinate(424.3, 0, 10)
    # second = Coordinate(-424.3, 0, 10)
    #
    # tunnel = Tunnel(first, second)
