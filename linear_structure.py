class LinearStructure:

    def __init__(self, plunge, trend):
        self.plunge = plunge
        self.trend = trend

    def __str__(self) -> str:
        return 'Plunge : ' + str(self.plunge) + \
               '\nTrend : ' + str(self.trend)
