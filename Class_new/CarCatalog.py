from Car import Car
from datetime import datetime
from Interval import Interval
from Booking import Booking
class CarCatalog:
    def __init__(self):
        self._car_lists=[]
            
    def show_car(self):
        catalog_list = []
        for car in self._car_lists:
            catalog_list.append(car.__str__())
        return catalog_list
    
    def add_car_to_catalog(self,car):
        self._car_lists.append(car)
        
    def search_car_by_brand(self, search_string):
        self.__list_of_car = []
        for obj in self._car_lists:
            if search_string.lower() in obj.get_car_brand().lower():
                self.__list_of_car.append(obj)
        return self.__list_of_car
    
    def search_car_by_model(self, search_string):
        self.__list_of_car = []
        for obj in self._car_lists:
            if search_string.lower() in obj.get_car_model().lower():
                self.__list_of_car.append(obj)
        return self.__list_of_car
     
    def find_available_car(self, start_date, start_time, end_date, end_time):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_car = []
        for i in self._car_lists:
            if not i.get_status_available():
                continue
            if not i.car_available(date1, date2):
                continue
            available_car.append(i)
        return available_car
    
    def book_car(self,cars,start_date,start_time,end_date,end_time):
        for i in self._car_lists:
            if i.get_car_plate_number()== cars:
                book_car = i
                break
        interval = Interval(start_date,start_time,end_date,end_time)
        booking = Booking(book_car,interval)
        return booking
    
    def find_car_by_plate(self,cars):
        for i in self._car_lists:
            if i.get_car_plate_number() == cars:
                this_car = i
        return this_car
    

            
    