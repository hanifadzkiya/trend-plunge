from read_excel import ReadExcel


class LineEquation:
    def __init__(self, coef_x, coef_y, c):
        self.coef_x = coef_x
        self.coef_y = coef_y
        self.c = c

    def get_y(self, x):
        return (-self.c - self.coef_x * x) / self.coef_y
