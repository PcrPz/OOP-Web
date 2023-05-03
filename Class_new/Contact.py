from CarCatalog import CarCatalog
from CreditInfo import CreditInfo
import datetime
from Car import*
class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email,contact_type):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_password = contact_password
        self._contact_phone_num = contact_phone_num
        self._contact_email = contact_email
        self._contact_type = contact_type
        
    def get_name(self):
        return self._contact_name
    
    def get_username(self):
        return self._contact_username
    
    def get_phone_num(self):
        return self._contact_phone_num
    
    def get_password(self):
        return self._contact_password
    
    def get_email(self):
        return self._contact_email
    
    def get_type(self):
        return self._contact_type
    
    def edit_profile(self,new_phone_num,new_password,new_email):
        if isinstance(new_phone_num, str):
            self._contact_phone_num = new_phone_num
        if isinstance(new_password, str):
            self._contact_password = new_password
        if isinstance(new_email, str):
            self._contact_email = new_email   
                
class Owner(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email,contact_type ="Owner")          
           
        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email,contact_type ="Renter")
        self.__list_favour = []
        self.__list_history = []
        self.__booking = None
        
    def set_booking(self,booking):
        self.__booking = booking
        
    def get_booking(self):
        return self.__booking
        
    def add_fav_car(self,car):
        self.__list_favour.append(car)
    def watch_fav_car(self):
        return {"FavouriteCar":[{"brand":car.get_car_brand(),
                        "model":car.get_car_model(),
                        "price":car.get_car_amount(),}
                       for car in self.__list_favour]}
        
    def watch_history(self):
        return {"HistoryCar":[{"brand":history.get_price(),
                        "model":history.get_car_model(),
                        "price":history.get_car_amount(),}
                       for history in self.__list_history]}  
            #โชว์ค่า fav car ออกมา
    def add_history(self,booking):
        self.__list_history.append(booking)
    #credit methods
    def add_credit_info(self, creditInfo:CreditInfo):
        self._credit_card = creditInfo
    
    def cancel_booking (self):
        self.__booking = None
            
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