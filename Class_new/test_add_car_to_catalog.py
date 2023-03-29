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
        [],
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
        [],
        [1,2,3,4,5])

testalog = CarCatalog([cara, carb])
future.add_car(carc,testalog)

print(testalog._car_lists)
