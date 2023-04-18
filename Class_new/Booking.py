import datetime
from Interval import Interval
from Car import Car
class Booking:
    def __init__(self,car:Car,interval:Interval):
        self.__day_range = interval
        self.__day_start = self.__day_range.get_end_time()
        self.__day_end = self.__day_range.get_start_time()
        self.__price = car.get_car_amount() *(self.__day_start - self.__day_end).days
        
    def get_price(self):
        return self.__price
    
 #เเก้คิดเงินหน่อยค้าบ
    def show_booking(self):
        print(self.__day_start)
        print(self.__day_end)
        print(self.__price)

             
    