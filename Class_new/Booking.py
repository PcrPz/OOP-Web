import datetime
from Favourite import FavouriteCar
from Interval import Interval
from Car import Car
class Booking:
    def __init__(self,car:Car,interval:Interval):
        self._day_range = interval
        self._day_start = self._day_range.get_end_time()
        self._day_end = self._day_range.get_start_time()
        self._price = car._car_amount *(self._day_start - self._day_end).days
        
 #เเก้คิดเงินหน่อยค้าบ
    def show_booking(self):
        print(self._day_start)
        print(self._day_end)
        print(self._price)
             
    