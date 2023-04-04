from Class_new.Contact import Owner
from Class_new.CarCatalog import CarCatalog
from Class_new.Car import Car
future = Owner("futurenaja",
               "futureza567",
               "0930036622",
               "123456789",
               "65010671@gmail.com")
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
        "ABV-444",
        "new com",
        [])
carc = Car("toyota",
           "I8",
           "Engine",
           "200km",
           "200CC",
            "2Door",
        "3year",
        "2seat",
        "3Day-200usd",
        "-",
        "ABV-467",
        "new com",
        [1,2,3,4,5])

testalog = CarCatalog()
future.add_car(cara,testalog)
future.add_car(carb,testalog)
future.add_car(carc,testalog)
testalog.show_catalog()
