import copy
import math
from statistics import mean

from coordinate import Coordinate
from linear_structure import LinearStructure
from plane_structure import PlaneStructure
from read_excel import ReadExcel


def _get_avg_structure(structures):
    sum_strike = 0
    sum_dip = 0

    sum_plunge = 0
    sum_trend = 0

    for structure in structures:
        plane = structure.plane
        linear = structure.linear

        sum_strike += plane.strike
        sum_dip += plane.dip

        sum_plunge += linear.plunge
        sum_trend += linear.trend

    avg_strike = sum_strike / len(structures)
    avg_dip = sum_dip / len(structures)
    avg_plane = PlaneStructure(avg_strike, avg_dip)

    avg_plunge = sum_plunge / len(structures)
    avg_trend = sum_trend / len(structures)
    avg_linear = LinearStructure(avg_plunge, avg_trend)

    return Structure(avg_plane, avg_linear)


class Structure:

    def __init__(self, plane, linear):
        self.plane = plane
        self.linear = linear


class Plane:

    def __init__(self):
        self._structure = []
        self._avg_structure = Structure(None, None)
        self._weakness = Coordinate(None, None, None)
        self.tersingkap = None

    def add_structure_from_excel(self, loc, sheet):
        read_excel = ReadExcel(loc)

        read_excel.set_sheet(sheet)

        num_orientations = int(read_excel.cell_value(2, 1))

        start_row = 4
        for idx in range(num_orientations):
            row = start_row + idx

            strike_col = 0
            dip_col = 1
            strike = read_excel.cell_value(row, strike_col)
            dip = read_excel.cell_value(row, dip_col)

            plane_structure = PlaneStructure(strike, dip)
            linear_structure = plane_structure.get_linear_structure()

            self._structure.append(Structure(plane_structure, linear_structure))

        self._avg_structure = copy.deepcopy(_get_avg_structure(self._structure))

    def add_tersingkap_from_excel(self, loc, sheet):

        read_excel = ReadExcel(loc)

        read_excel.set_sheet(sheet)

        x = read_excel.cell_value(2,4)
        y = read_excel.cell_value(3,4)
        z = read_excel.cell_value(4,4)

        self.tersingkap = Coordinate(x, y, z)

    def get_avg_structure(self):
        return copy.deepcopy(self._avg_structure)

    def get_direction(self) -> Coordinate:
        trend = self._avg_structure.get_linear().get_trend()
        plunge = self._avg_structure.get_linear().get_plunge()

        north = math.cos(trend) * math.cos(plunge)
        east = math.sin(trend) * math.cos(plunge)
        down = math.sin(plunge)

        direction = Coordinate(east, north, -down)

        return copy.deepcopy(direction)

    def set_weakness(self, x, y, z):
        self._weakness = Coordinate(x, y, z)

    def get_weakness(self):
        return copy.deepcopy(self._weakness)
