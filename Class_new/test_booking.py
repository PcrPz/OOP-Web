import datetime
from CarCatalog import CarCatalog
from Car import Car
from Contact import Renter
from Booking import Booking
from Interval import Interval
from Class_new.Contact import Owner
cara =Car("BMW",
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

carb =Car("Ferrari",
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
#petch.add_time(datetime.datetime(2018, 6, 3, 10, 0),2)
testalog = CarCatalog()
future.add_car(cara,testalog)
future.add_car(carb,testalog)
cara.add_interval(Interval("1-6-2018","9:00","10-6-2018","10:00"))
carb.add_interval(Interval("5-6-2018","9:00","10-6-2018","10:00"))
for i in cara._date_not_avalible: 
    print(i.get_start_time())
    print(i.get_end_time())
print(testalog.find_available_car("11-6-2018","9:00","12-6-2018","9:59"))
# petchbooking=Booking(carb,Interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 10, 10, 0)))
# petchbooking.show_booking()





