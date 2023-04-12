from Contact import Renter
from Favourite import FavouriteCar
from Car import Car


petch = Renter("petch",
               "petchza555",
               "0930036621",
               "Inwpetchza",
               "petchza@gmail.com")

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

petch_fav = FavouriteCar()
petch.add_fav_car(cara,petch_fav)
petch.add_fav_car(carb,petch_fav)
petch.watch_fav_car(petch_fav)
