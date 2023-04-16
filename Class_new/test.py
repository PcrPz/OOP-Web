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
print(testalog.search_car_by_brand("BMW"))