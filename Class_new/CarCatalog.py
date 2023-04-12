from Car import Car
from datetime import datetime
class CarCatalog:
    def __init__(self):
        self._car_lists=[]
            
    def get_all_car_detail(self):
        catalog_list = []
        for car in self._car_lists:
            catalog_list.append(car.__str__())
        return catalog_list
     
    def find_available_car(self, start_date, start_time, end_date, end_time):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_car = []
        for i in self._car_lists:
            if not i._status_available:
                continue
            if not i.car_available(date1, date2):
                continue
            available_car.append(i)
        return available_car
    

    
    # def check_no_overlab(start_time1,end_time1,start_time2,end_time2):
    #     if start_time1 > end_time2 or start_time2> end_time1:
    #         return True
    #     else:
    #         return False
        
    # def car_available(self,datetime1,datetime2):
    #     for i in self._car_lists:
    #         for j in i._date_not_avalible:
    #             if not self.check_no_overlap(datetime1,datetime2):
    #                 return False
    #         return True
        
    #     def is_available(self):
    #     return self.__is_available
        
            
    