from pydantic import BaseModel

class AvalibleDTO(BaseModel):
    start_date : str
    start_time : str
    end_date : str
    end_time : str
    
class BookingDTO(BaseModel):
    car_plate : str
    start_date : str
    start_time : str
    end_date : str
    end_time : str

class EditProfileDTO(BaseModel):
    new_phone_num :str
    new_password :str
    new_email :str
    
class CreditCardDTO(BaseModel):
    card_number:str
    exprie_card:str
    security_number:str    
    
class FavouriteDTO(BaseModel):
    car_plate : str 
    
class AddRateDTO(BaseModel):
    score : int 
    comment : str
    car_plate : str
class AddCarDTO (BaseModel):
    car_brand : str
    car_model : str
    fuel_type : str
    fuel_used : str
    car_feature : str
    car_door : str
    car_insurance: str
    car_seat : str
    car_amount : int
    car_about: str
    car_plate_number : str
    
class Registeration(BaseModel):
    contact_name : str
    contact_username : str
    contact_phone_num : str
    contact_password : str
    contact_email : str
    contact_type : str

