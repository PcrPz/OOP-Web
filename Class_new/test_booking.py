import datetime
from CarCatalog import CarCatalog
from Car import Car
from Contact import Renter
from Booking import Booking

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
        [datetime.datetime(2018, 6, 1, 0, 0), datetime.datetime(2018, 6, 2, 0, 0), 
         datetime.datetime(2018, 6, 5, 0, 0), datetime.datetime(2018, 6, 6, 0, 0),
         datetime.datetime(2018, 6, 7, 0, 0),datetime.datetime(2018, 6, 8, 0, 0), 
         datetime.datetime(2018, 6, 9, 0, 0), datetime.datetime(2018, 6, 10, 0, 0)])

carb = Car("Bmw",
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
        [datetime.datetime(2018, 6, 1, 0, 0), datetime.datetime(2018, 6, 2, 0, 0), 
         datetime.datetime(2018, 6, 3, 0, 0), datetime.datetime(2018, 6, 4, 0, 0),
         datetime.datetime(2018, 6, 7, 0, 0),datetime.datetime(2018, 6, 8, 0, 0), 
         datetime.datetime(2018, 6, 9, 0, 0), datetime.datetime(2018, 6, 10, 0, 0)])
petch = Renter("petch",
               "petchza555",
               "0930036621",
               "Inwpetchza",
               "petchza@gmail.com")

petch.add_time(datetime.datetime(2018, 6, 3, 0, 0),2)
testalog = CarCatalog([cara, carb])
testalog.checktime_car(petch._time_start,petch._amount)
print(testalog._avalible)
petch.select_car(cara)
print(petch._choose_car)
bookpetch=Booking(petch._choose_car._car_amount,petch._time_start,petch._amount)
print(bookpetch._price)
print(bookpetch._day_start)
print(bookpetch._day_end)

