import datetime
from Interval import Interval
from Car import Car
class Booking:
    def __init__(self,car:Car,interval:Interval):
        self.__day_interval = interval
        self.__car = car
        self.__day_start = self.__day_interval.get_end_time()#day_start    
        self.__day_end = self.__day_interval.get_start_time()#day_end
        self.__price = self.__car.get_car_amount() *(self.__day_start - self.__day_end).days
    
    def get_car(self):
        return self.__car
    
    def get_price (self):
        return self.__price
    
    def get_interval(self):
        return self.__day_interval
        
 #เเก้คิดเงินหน่อยค้าบ
    def show_booking(self):
        print(self.__day_start)
        print(self.__day_end)
        print(self.__price)


             
    