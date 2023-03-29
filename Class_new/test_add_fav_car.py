from Class_new.Contact import Renter
from Class_new.Favourite import FavouriteCar
from Class_new.Car import Car

petch = Renter("petch",
               "petchza555",
               "0930036621",
               "Inwpetchza",
               "petchza@gmail.com")

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
           "F12",
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

petch_fav = FavouriteCar([])
petch.add_fav_car(cara,petch_fav)
petch.add_fav_car(carb,petch_fav)
petch.watch_fav_car(petch_fav)
#