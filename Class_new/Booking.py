import datetime
class Booking:
    def __init__(self,price,day_start,range):
        self._price = price
        self._day_start = day_start
        self._day_end = day_start + datetime.timedelta(range-1)