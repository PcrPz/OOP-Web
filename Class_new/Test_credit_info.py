from fastapi import FastAPI
from Contact import Renter,Owner
from CreditCard import CreditInfo

app = FastAPI()
@app.get("/")
def home():
    return {"Hello Future"}
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
petchCard = CreditInfo("17/04/2024","7051124351","437")
petch.add_credit_info(petchCard) 
print(petchCard.expire_card)
petch._credit_card.edit_credit_info("11/04/2025","1534211507","437")
print(petchCard.expire_card)
print(petch._credit_card.expire_card)