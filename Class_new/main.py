from Car import Car
from datetime import *
from fastapi import FastAPI
from dto import *
from Favourite import FavouriteCar
app = FastAPI()

class CarCatalog:
    def __init__(self):
        self._car_lists=[]
            
    def show_car(self):
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
    
    def book_car(self,cars,start_date,start_time,end_date,end_time):
        for i in self._car_lists:
            if i._car_plate_number == cars:
                book_car = i
                break
        interval = Interval(start_date,start_time,end_date,end_time)
        book_car.add_interval(interval)
        booking = Booking(book_car,interval)
        return booking

    
class Car():          
    def __init__(self,car_brand,car_model,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_about,car_plate_number):
        self._car_brand = car_brand
        self._car_model = car_model 
        self._fuel_type= fuel_type
        self._fuel_used = fuel_used
        self._car_feature= car_feature
        self._car_door = car_door
        self._car_insurance= car_insurance
        self._car_seat = car_seat
        self._car_about= car_about
        self._car_amount= car_amount
        self._car_plate_number= car_plate_number
        self._rating_review = []
        self._date_not_avalible = []
        self._status_available = True

    def add_interval(self, interval):
        self._date_not_avalible.append(interval)

    def check_no_overlap(self,start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def car_available(self, datetime1, datetime2):
        for i in self._date_not_avalible:
            if not self.check_no_overlap(i.get_start_time(), i.get_end_time(), datetime1, datetime2):
                return False
        return True
        
    def __str__(self):
        return(f"car_brand : {self._car_brand} model {self._car_model} insurance {self._car_insurance}")
    
class Interval:
    def __init__(self,start_date_str,start_time_str,end_date_str,end_time_str):
        self.__date_start = self.convert_str_to_datetime(start_date_str, start_time_str)
        self.__date_end = self.convert_str_to_datetime(end_date_str, end_time_str)
    
    def convert_str_to_datetime(self, str_date, str_time):
        return datetime.strptime(str_date + " " + str_time, '%d-%m-%Y %H:%M')
    
    def convert_datetime_to_str(self, datetime):
        return datetime.strftime("%m/%d/%Y, %H:%M")
    
    def get_start_time (self):
        return self.__date_start
    
    def get_end_time (self):
        return self.__date_end

class Booking:
    def __init__(self,car:Car,interval:Interval):
        self._day_range = interval
        self._day_start = self._day_range.get_end_time()
        self._day_end = self._day_range.get_start_time()
        self._price = car._car_amount *(self._day_start - self._day_end).days
        
    def show_booking(self):
        print(self._day_start)
        print(self._day_end)
        print(self._price)
        
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
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)
    def add_fav_car(self,car,car_favourite:FavouriteCar):
        car_favourite._car_favourite_list.append(car)
    def watch_fav_car(self,car_favourite:FavouriteCar):
        for car in car_favourite._car_favourite_list:
            print(car._car_brand)
            print(car._car_model)
            print(car._date_not_avalible)
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
    def search_car(self,):
        pass


bmw =Car("BMW",
          "I8",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "ABZW-908")

fer =Car("Ferrari",
          "F1",
          "Engine",
          "200km",
          "300CC",
          "4Door",
          "3year",
          "2seat",
          200,
          "car_about",
          "ABZW-999")

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

testalog = CarCatalog()
future.add_car(bmw,testalog)
future.add_car(fer,testalog)
bmw.add_interval(Interval("1-6-2018","9:00","10-6-2018","10:00"))
fer.add_interval(Interval("5-6-2018","9:00","10-6-2018","10:00"))
#         "car": "ABZW-999",
#   "start_date": "11-6-2018",
#   "start_time": "9:00",
#   "end_date": "12-6-2018",
#   "end_time": "9:59"
@app.post("/get_available_car", tags=["booking"])
async def get_available_car(data: AvalibleDTO):
    list_car = testalog.find_available_car(data.start_date,data.start_time,data.end_date,data.end_time)
    return list_car

@app.post("/book_car",tags = ["booking"])
async def get_available_car(data: BookingDTO):
    status = testalog.book_car(data.car,data.start_date,data.start_time,data.end_date,data.end_time)
    return status.show_booking()


