
class Signup_Login:
    def __init__(self, _username_member, _password_member):
        self._username_member = _username_member
        self._password_member = _password_member

class Contact:
    def __init__(self, _contact_name, _contact_id, _contact_phonenumber, _contact_password, _contact_email, _contact_about, _driver_license_status, _contact_age_check):
        self._contact_name = _contact_name
        self._contact_id = _contact_id
        self._contact_phonenumber = _contact_phonenumber
        self._contact_password = _contact_password
        self._contact_email = _contact_email
        self._contact_about = _contact_about
        self._driver_license_status = _driver_license_status 
        self._contact_age_check = _contact_age_check
        
class Owner:
    def __init__(self, _owner_contact, _owner_review, _owner_photo, _owner_details):
        self._owner_contact = _owner_contact
        self._owner_review = _owner_review
        self._owner_photo = _owner_photo
        self._owner_details = _owner_details

class Renter:
    def __init__(self, _renter_contact, _renter_review, _renter_photo, _renter_details):
        self._renter_contact = _renter_contact
        self._renter_review = _renter_review
        self._rernter_photo = _renter_photo
        self._renter_details = _renter_details

class BookingInfo:
    def init(self, _car_detail, _expire_day):
        self._car_detail = _car_detail
        self._expire_day = _expire_day

class Booking:
    def init(self, _list_location, _amount, _day_start, _day_end):
        self._amount = _amount
        self._day_start = _day_start
        self._day_end = _day_end

class BookHistory:
     def init(self,_booked_car):
        self._booked_car = _booked_car

class CarDetails:
    def __init__(self, _fuel_type, _fuel_used, _car_feature, _car_door, _car_insurance, _car_seat, _car_amount, _car_description, _car_photo, _car_plate_number):
        self._fuel_type = _fuel_type
        self._fuel_used = _fuel_used
        self._car_feature = _car_feature
        self._car_door = _car_door
        self._car_insurance = _car_insurance
        self._car_seat = _car_seat
        self._car_amount = _car_amount
        self._car_description = _car_description
        self._car_photo = _car_photo
        self._car_plate_number = _car_plate_number

class CarCatalog:
    def __init__(self, _car_brand, _model_detail):
        self._car_brand = _car_brand
        self._model_detail = _model_detail

class Payment:
    def __init__(self, _payment_status, _transaction_id, _amount):
        self._payment_status = _payment_status
        self._transaction_id = _transaction_id
        self._amount = _amount

class CreditInfo:
    def __init__(self, _name_on_card, _expire_date, _card_number, _security_credit, _card_address):
        self._name_on_card = _name_on_card
        self._expire_date = _expire_date 
        self._card_number = _card_number
        self._security_credit = _security_credit
        self._card_address = _card_address

class CarAvailable:
    def __init__(self, _date_available, _car_available_status, _car_status):
        self._date_avaliable = _date_available
        self._car_available_status = _car_available_status
        self._car_status = _car_status