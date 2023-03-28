import datetime
from CarCatalog import CarCatalog
from Car import Car

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

testalog = CarCatalog([cara, carb])
testalog.checktime_car(datetime.datetime(2018, 6, 3, 0, 0),2)
print(testalog._avalible)
