from Contact import Owner
from Contact import Renter
from Rating import Rating
from CarCatalog import CarCatalog
from Car import Car
future = Owner("futurenaja",
               "futureza567",
               "0930036622",
               "123456789",
               "65010671@gmail.com")
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
        "ABV-467",
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
        "ABV-467",
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
        [])

#testalog = CarCatalog([cara, carb])
#future.add_car(carc,testalog)
#print(testalog)

testReview = (petch._contact_name,
              "good")
testReview2 = (petch._contact_name,
              "good")
cara.add_comment(testReview)
cara.add_comment(testReview2)

print(cara._rating_review)
