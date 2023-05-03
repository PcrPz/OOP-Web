from Rating import Rating
class Car():          
    def __init__(self,car_brand,car_model,fuel_type,fuel_used,car_feature,car_door,car_insurance,car_seat,car_amount,car_about,car_plate_number):
        self.__car_brand = car_brand
        self.__car_model = car_model 
        self.__fuel_type= fuel_type
        self.__fuel_used = fuel_used
        self.__car_feature= car_feature
        self.__car_door = car_door
        self.__car_insurance= car_insurance
        self.__car_seat = car_seat
        self.__car_about= car_about
        self.__car_amount= car_amount
        self.__car_plate_number= car_plate_number
        self.__rating = []
        self.__date_not_avalible = []
        self.__status_available = True
        self.__rating_score = 0

    def get_car_brand(self):
        return self.__car_brand
    
    def get_car_model(self):
        return self.__car_model
    
    def get_car_date_not_avalible(self):
        return self.__date_not_avalible

    def get_status_available(self):
        return self.__status_available
    
    def get_car_plate_number(self):
        return self.__car_plate_number
    
    def get_car_amount(self):
        return self.__car_amount
    
    def get_rating (self):
        return self.__rating
    
    def get_rating_score(self):
        return  self.__rating_score
    
    def add_rating(self, rating:Rating):
        self.__rating.append(rating)
        self.__rating_score = sum([i.get_rating_review () for i in self.__rating])/len(self.__rating)
        
    def add_interval(self,interval):
        self.__date_not_avalible.append(interval)

    def check_no_overlap(self,start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def car_available(self, datetime1, datetime2):
        for i in self.__date_not_avalible:
            if not self.check_no_overlap(i.get_start_time(), i.get_end_time(), datetime1, datetime2):
                return False
        return True
        
    def __str__(self):
        return(f"car_brand : {self.__car_brand} model : {self.__car_model} insurance : {self.__car_plate_number}")
