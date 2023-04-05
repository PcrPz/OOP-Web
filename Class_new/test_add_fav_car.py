from Contact import Renter
from Favourite import FavouriteCar
from Car import Car
from Rating import Rating

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
RatingByPetch = Rating("petch",
                       "Good")
petch_fav = FavouriteCar([])
petch.add_fav_car(cara,petch_fav)
petch.add_fav_car(carb,petch_fav)
petch.watch_fav_car(petch_fav)

petch.add_comment(RatingByPetch,cara)
#
