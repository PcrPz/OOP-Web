from CreditCard import CreditInfo
from Contact import Renter
petch = Renter("petch",
               "petchza555",
               "0930036621",
               "Inwpetchza",
               "petchza@gmail.com")
petch._contact_creditInfo = ["Petch007",
                 "1/11/2566",
                 "11122545162",
                 "911",
                 "card_address1"]
#TestCreditNew = CreditInfo("Zetch007","17/9/2570","16522032165","191","card_address2")


print(petch._contact_creditInfo)
print(type(petch._contact_creditInfo))
petch.modify_creditcard_info(petch._contact_creditInfo,"Zetch007","17/9/2570","16522032165","191","card_address2")
print(petch._contact_creditInfo)
