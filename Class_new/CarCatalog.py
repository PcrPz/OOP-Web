from Car import Car
import datetime
class CarCatalog:
    def __init__(self,car_list:list):
        self._car_lists=car_list
        self._check = True
    
    def checktime_car(self,start,amount):
        self._avalible = []
        for i in self._car_lists:
            for j in range(amount):
                date = start + datetime.timedelta(days=j)
                if date in i._date_not_avalible:
                    self._check= False
                    break
            if self._check == True :
                self._avalible.append(i)
            self._check =True
            
    