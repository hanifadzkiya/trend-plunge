import copy
import math

from linear_structure import LinearStructure


class PlaneStructure:

    def __init__(self, strike, dip) -> None:
        self._strike = strike
        self._dip = dip

    def get_strike(self):
        return self._strike

    def get_dip(self):
        return self._dip

    def get_linear_structure(self):
        plunge = math.radians(90 - self._dip)
        trend = math.radians(self._strike - 90) if(self._strike >= 90) else math.radians(self._strike + 270)

        return copy.deepcopy(LinearStructure(plunge,trend))