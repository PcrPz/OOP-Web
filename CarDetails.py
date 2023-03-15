class CarDetails:
    
    def __init__(self,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_description,car_photo,car_plate_number,car_brand,rating_review):
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
    
class CarStat(CarDetails):
    def __init__(self, fuel_type, fuel_used, car_feature, car_door, car_insurance, car_seat, car_amount, car_description, car_photo, car_plate_number,date_avalible,car_available_status,car_status):
        super().__init__(fuel_type, fuel_used, car_feature, car_door, car_insurance, car_seat, car_amount, car_description, car_photo, car_plate_number)
        self.__date_avalible = date_avalible
        self.__car_available_status = car_available_status
        self.__car_status = car_status
        
