import xlrd

class ReadExcel:

    def __init__(self, loc):

        self._loc = loc
        self._wb = xlrd.open_workbook(self._loc)
        self._sheet = None

    def set_sheet(self, index):
        self._sheet = self._wb.sheet_by_index(index)

    def cell_value(self, i, j):
        return self._sheet.cell_value(i, j)

