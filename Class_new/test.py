from Car import *
from datetime import *
from Contact import*
from Interval import*
from CarCatalog import*
from Rating import *
# from Favourite import *

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

r35 =Car("Nissan",
          "Gtr",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "ABZW-343")

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
testalog.add_car_to_catalog(bmw)
testalog.add_car_to_catalog(fer)
testalog.add_car_to_catalog(r35)
bmw.add_interval(Interval("1-6-2018","9:00","10-6-2018","10:00"))
fer.add_interval(Interval("5-6-2018","9:00","10-6-2018","10:00"))
test_rating1 = Rating(10,"Noobnam")
test_rating2 = Rating(9,"good")
bmw.add_rating(test_rating1)
bmw.add_rating(test_rating2)
x=testalog.find_car_by_plate("ABZW-343")
x.add_rating(Rating(10,"Good"))
print (r35.get_rating_score())
y=testalog.search_car_by_brand("bmw")
petch.add_fav_car(y)
print(petch.watch_fav_car())



class Inter:
    
    def __init__(self,start_date_str,start_time_str,end_date_str,end_time_str):
        self.__date_start = self.convert_str_to_datetime(start_date_str, start_time_str)
        self.__date_end = self.convert_str_to_datetime(end_date_str, end_time_str)
    
    def convert_str_to_datetime(self, str_date, str_time):
        return datetime.strptime(str_date + " " + str_time, '%d-%m-%Y %H:%M')
    

print(Inter("03-05-2023","9:00","16-05-2023","9:59"))