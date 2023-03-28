from CarCatalog import CarCatalog
from Favourite import FavouriteCar
import datetime
class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_password = contact_password
        self._contact_email = contact_email
        
class Owner(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)
    def add_car(self,car,car_catalog:CarCatalog):
        car_catalog._car_lists.append(car)
        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)
    def add_fav_car(self,car,car_favourite:FavouriteCar):
        car_favourite._car_favourite_list.append(car)
    def watch_fav_car(self,car_favourite:FavouriteCar):
        for car in car_favourite._car_favourite_list:
            print(car._car_brand)
            print(car._car_model)
            print(car._date_avalible)
    def add_time(self,time_start,amount):
        self.time_start = time_start
        self.amount = amount
        #เเอดเวลาเข้ามา
    def select_car(self,car):
        pass
        #เลือกรถส่งไปที่ booking
petch = Renter("petch",
               "petchza555",
               "0930036621",
               "Inwpetchza",
               "petchza@gmail.com")

future = Owner("futurenaja",
               "futureza567",
               "0930036622",
               "123456789",
               "65010671@gmail.com")