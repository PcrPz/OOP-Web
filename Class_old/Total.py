class SignUpLogin:
    def __init__(self,username_member,password_member):
        self.__username_member = username_member
        self.__password_member = password_member
    def register():
        pass    
    def check_login():
        pass
class Contact:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_password,contact_email,contact_about,driver_license_status,contact_age_check):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_password = contact_password
        self._contact_email = contact_email
        self._contact_about = contact_about
        self._driver_license_status = driver_license_status
        self._contact_age_check= contact_age_check
    def edit_info():
        pass    
class Owner(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check,car_detail):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check)
        self.__car_detail = car_detail
    def add_car_details():
        pass
        
class Renter(Contact):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email, contact_about, driver_license_status, contact_age_check)
    def confirm_booking():
        pass
    def set_date_car():
        pass
class CarCatalog:
    def __init__(self,car_brand,model_detail):
        self.__car_brand = car_brand
        self.__model_detail = model_detail
    def update_car():
        pass
        
class CarDetails:
    def __init__(self,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_description,car_photo,car_plate_number,car_brand,rating_review):
        self.__fuel_type= fuel_type
        self.__fuel_used = fuel_used
        self.__car_feature= car_feature
        self.__car_door, = car_door,
        self.__car_insurance= car_insurance
        self.__car_seat = car_seat
        self.__car_amount= car_amount
        self.__car_description= car_description
        self.__car_photo= car_photo
        self.__car_plate_number= car_plate_number
        self.__car_brand = car_brand
        self.__rating_review = rating_review
    def add_car_detail():
        pass
    
class CarStat(CarDetails):
    def __init__(self, fuel_type, fuel_used, car_feature, car_door, car_insurance, car_seat, car_amount, car_description, car_photo, car_plate_number,date_avalible,car_available_status,car_status):
        super().__init__(fuel_type, fuel_used, car_feature, car_door, car_insurance, car_seat, car_amount, car_description, car_photo, car_plate_number)
        self.__date_avalible = date_avalible
        self.__car_available_status = car_available_status
        self.__car_status = car_status
    def check_car_available():
        pass

class Booking:
    def __init__(self,list_location,amount,day_start,day_end,car_detail):
        self.__list_location = list_location
        self.__amount = amount
        self.__day_start = day_start
        self.__day_end = day_end
        self.__car_detail = car_detail
    def update_booking():
        pass

class Payment:
    def __init__(self,payment_status,transaction_id,amount,card_info):
        self.__payment_status = payment_status
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__card_info = card_info
    def payment_perform():
        pass
    def update_payment():
        pass
    
class CreditInfo:
    def __init__(self,name_on_card,expire_card,card_number,security_credit,card_address):
        self.__name_on_card = name_on_card
        self.__expire_card = expire_card
        self.__card_number = card_number
        self.__security_credit = security_credit
        self.__card_address = card_address
    def fill_credit_info():
        pass

