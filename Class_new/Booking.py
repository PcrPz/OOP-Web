import datetime
from Interval import Interval
from Car import Car
class Booking:
    def __init__(self,car:Car,interval:Interval,booked_number):
        self.__day_range = interval
        self.__day_start = self.__day_range.get_end_time()
        self.__day_end = self.__day_range.get_start_time()
        self.__price = car.get_car_amount() *(self.__day_start - self.__day_end).days
        self.__booked_number = booked_number
        
    def get_price(self):
        return self.__price
    
 #เเก้คิดเงินหน่อยค้าบ
    def show_booking(self):
        print(self.__day_start)
        print(self.__day_end)
        print(self.__price)
        print(self.__booked_number)

    # def set_booked_num(self,booked_num):
    #     self.__booked_num = booked_num

    def get_booked_number(self):
        return self.__booked_number


             
    