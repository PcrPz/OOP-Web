from CarCatalog import CarCatalog
from CreditCard import CreditInfo
import datetime
from Car import*
class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email,contact_type):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_password = contact_password
        self._contact_email = contact_email
        self._contact_type = contact_type
        
class Owner(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email,contact_type ="Owner")          
    def edit_profile(self,new_name,new_username,new_phone_num,new_password,new_email):
        if isinstance(new_name, str):
            self._contact_name = new_name
        if isinstance(new_username, str):
            self._contact_username = new_username
        if isinstance(new_phone_num, str):
            self._contact_phone_num = new_phone_num
        if isinstance(new_password, str):
            self._contact_password = new_password
        if isinstance(new_email, str):
            self._contact_email = new_email
        
        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email,contact_type ="Renter")
        self._list_favour = []
        self._credit_card = None
        self._list_history = []
        self._booking = None

    def add_fav_car(self,car):
        self._list_favour.append(car)
    def watch_fav_car(self):
        return {"FavouriteCar":[{"brand":car.get_car_brand(),
                        "model":car.get_car_model(),
                        "price":car.get_car_amount(),}
                       for car in self._list_favour]}
            #โชว์ค่า fav car ออกมา
    def edit_profile(self,new_name,new_username,new_phone_num,new_password,new_email):
        if isinstance(new_name, str):
            self._contact_name = new_name
        if isinstance(new_username, str):
            self._contact_username = new_username
        if isinstance(new_phone_num, str):
            self._contact_phone_num = new_phone_num
        if isinstance(new_password, str):
            self._contact_password = new_password
        if isinstance(new_email, str):
            self._contact_email = new_email
    
    #credit methods
    def add_credit_info(self, creditInfo:CreditInfo):
        self._credit_card = creditInfo
 
            
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