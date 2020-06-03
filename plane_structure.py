import copy
import math

from linear_structure import LinearStructure


class PlaneStructure:

    def __init__(self, strike, dip) -> None:
        self.strike = strike
        self.dip = dip

    def get_linear_structure(self):
        plunge = math.radians(90 - self.dip)
        trend = math.radians(self.strike - 90) if(self.strike >= 90) else math.radians(self.strike + 270)

        return copy.deepcopy(LinearStructure(plunge,trend))