class Car():          
    def __init__(self,car_brand,car_model,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_about,car_plate_number,rating_review,date_not_avalible):
        self._car_brand = car_brand
        self._car_model = car_model 
        self._fuel_type= fuel_type
        self._fuel_used = fuel_used
        self._car_feature= car_feature
        self._car_door = car_door
        self._car_insurance= car_insurance
        self._car_seat = car_seat
        self._car_amount= car_amount
        self._car_about= car_about
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
    