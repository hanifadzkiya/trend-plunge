import copy


class Tunnel:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def get_first(self):
        return copy.deepcopy(self._first)

    def get_second(self):
        return copy.deepcopy(self._second)
