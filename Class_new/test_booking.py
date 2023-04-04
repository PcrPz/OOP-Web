import datetime
from CarCatalog import CarCatalog
from Car import Car
from Contact import Renter
from Booking import Booking
from Interval import Interval
from Class_new.Contact import Owner

cara = Car("Bmw",
           "I8",
           "Engine",
           "200km",
           "200CC",
            "2Door",
        "3year",
        "2seat",
        "3Day-200usd",
        "-",
        "ABV-555",
        [],
        [])

carb = Car("Ferrari",
           "I8",
           "Engine",
           "200km",
           "200CC",
            "2Door",
        "3year",
        "2seat",
        "3Day-200usd",
        "-",
        "ABV-555",
        [],
        [])
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
start_date= "19-6-2023"
start_time=  "12:30"
testalog = CarCatalog()
future.add_car(cara,testalog)
future.add_car(carb,testalog)
cara.add_interval(Interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
carb.add_interval(Interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
for i in cara._date_not_avalible: 
    print(i.get_start_time())
    print(i.get_end_time())
print(testalog.find_available_car("8-6-2018","0:00","9-6-2018","0:00"))

#testalog.checktime_car(petch._time_start,petch._amount)
#print(testalog._avalible)
# petch.select_car(cara)
# print(petch._choose_car)
# bookpetch=Booking(petch._choose_car._car_amount,petch._time_start,petch._amount)
# print(bookpetch._price)
# print(bookpetch._day_start)
# print(bookpetch._day_end)



