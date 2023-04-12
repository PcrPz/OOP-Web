from fastapi import FastAPI
from Contact import Renter,Owner

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

future.edit_profile("futuredekwen","future1219","0860200333","093xzxzxxz","pachara@gmail.com")
petch.edit_profile("petchdekkak","petch1219","132132135","ddasdsasa","petchnaja@gmail.com")
# print(future._contact_name)
# print(future._contact_username)
# print(future._contact_phone_num)
# print(future._contact_password)
# print(future._contact_email)
# print(petch._contact_name)
# print(petch._contact_username)
# print(petch._contact_phone_num)
# print(petch._contact_password)
# print(petch._contact_email)