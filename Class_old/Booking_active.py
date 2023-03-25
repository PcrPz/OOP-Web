class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email,contact_about):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_password = contact_password
        self._contact_email = contact_email
        self._contact_about = contact_about

        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about)

class Booking:
    def __init__(self):
        self.booking_date=""
        self.booking_car_detail=[]
    def update_booking(self,booking_car_detail,booking_date):
        self.booking_car_detail += booking_car_detail
        self.booking_date += booking_date
        
class CarCatalog:
    def __init__(self):
        self.carlists=[]
    def add_car_list(self,car):
        self.carlists.append(car)

class Choice:
    def __init__(self,date_for_check,plate_number_for_check):
        self.date_for_check = date_for_check
        self.plate_number_for_check = plate_number_for_check
    
    def gotocar(self,date_for_check,plate_number_for_check):
        pass
        

class Car():          
    def __init__(self,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_description,car_photo,car_plate_number,car_brand,rating_review,date_avalible):
        self._fuel_type= fuel_type
        self._fuel_used = fuel_used
        self._car_feature= car_feature
        self._car_door, = car_door,
        self._car_insurance= car_insurance
        self._car_seat = car_seat
        self._car_amount= car_amount
        self._car_description= car_description
        self._car_photo= car_photo
        self._car_plate_number= car_plate_number
        self._car_brand = car_brand
        self._rating_review = rating_review
        self._date_avalible = []
        self._date_avalible.append(date_avalible)
        
    def show(self):
        pass
    
    def check_date(self,date_for_check,plate_number_for_check):
        for i in CarCatalog:
            if i._car_plate_number == plate_number_for_check:
                for j in Car:
                    if j._date_avalible == date_for_check:
                        return False
                    else:
                        return True
            

        

Petch = Renter("petch","petchza555","0930036622","Inwpetchza","petchza@gmail.com","lover")
rent = Car("Bmz","",1,1,1,1,1,1,1,1,'Z4',1,['16-03-47'])
BWMZ20 = CarCatalog.add_car_list(["Z20","popo"],"61-03-47")
print(rent.show())


