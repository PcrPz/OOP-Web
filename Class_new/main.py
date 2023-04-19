from Car import *
from datetime import *
from fastapi import FastAPI
from dto import *
import random
from Contact import*
from CreditCard import*
from Interval import*
from CarCatalog import*
from Rating import *
from Payment import *
from System import *
app = FastAPI()

bmw =Car("BMW",
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

fer =Car("Ferrari",
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

r35 =Car("Nissan",
          "Gtr",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "ABZW-343")

Nismo = Car("Nismo",
          "R31",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "ABZW-333")

moto = Car("Audi",
          "R8",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "CVZ-786")

kop = Car("BMW",
          "M5",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "DASD-786")

op = Car("BMW",
          "M5",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "SNIS-642")

car7 = Car("Pk",
          "Hua",
          "Engine",
          "200km",
          "200CC",
          "2Door",
          "3year",
          "2seat",
          100,
          "car_about",
          "SSIS-641")

petch = Renter("petch",
               "petch",
               "0930036621",
               "5678",
               "petchza@gmail.com")

future = Owner("futurenaja",
               "future",
               "0930036622",
               "1234",
               "65010671@gmail.com")
sym = System()
testalog = CarCatalog()
testalog.add_car_to_catalog(bmw)
testalog.add_car_to_catalog(fer)
testalog.add_car_to_catalog(r35)
testalog.add_car_to_catalog(moto)
testalog.add_car_to_catalog(kop)
testalog.add_car_to_catalog(op)
testalog.add_car_to_catalog(car7)
bmw.add_interval(Interval("1-6-2018","9:00","10-6-2018","10:00"))
fer.add_interval(Interval("5-6-2018","9:00","10-6-2018","10:00"))
#function  หารถคันนั้น
sym.add_user(future)
sym.add_user(petch)

#function หาuser


#         "car": "ABZW-999",
#   "start_date": "11-6-2018",
#   "start_time": "9:00",
#   "end_date": "12-6-2018",
#   "end_time": "9:59"
# HOME
@app.get("/")
async def home():
    return {"Future_Car"}
#Login
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    status_user= sym.check_user(form_data.username,form_data.password)
    if not status_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = sym.get_user(form_data.username)
    return {"access_token": user._contact_username, "token_type": "bearer"}

#Register
@app.post("/registeration")
async def registeration(data:Registeration):
    sym.add_user(Renter(data.contact_name, data.contact_username, data.contact_phone_num, data.contact_password, data.contact_email))
    return{"status" : "Success"}

@app.get("/users/me")
async def read_users_me(current_user = Depends(sym.get_current_user)):
    return current_user

#Modify Contact
@app.post("/users/me/modify")
async def edit_profile(data:EditProfileDTO,current_user= Depends(sym.get_current_user)):
    current_user.edit_profile(data.new_name,
    data.new_username ,
    data.new_phone_num ,
    data.new_password ,
    data.new_email )
    return {"status":"Success"}
#Cars
@app.get("/cars", tags=["Catalog"])
async def home():
    return {"catalog":[{"car_brand": x.get_car_brand(),
                        "car_model": x.get_car_model(),
                        "car_amount": x.get_car_amount(),
                        "car_plate_number": x.get_car_plate_number(),
                        "car_rating": x.get_rating_score()}
                       for x in testalog._car_lists]}

#Add_book
@app.post("/add_car", tags=["Cars"])
async def add_car_to_catalog(data:AddCarDTO):
    #ดักทะเบียน
    testalog.add_car_to_catalog(Car(
            data.car_brand,
            data.car_model,
            data.fuel_type,
            data.fuel_used,
            data.car_feature,
            data.car_door,
            data.car_insurance,
            data.car_seat,
            data.car_amount,
            data.car_about,
            data.car_plate_number)
    )
    return {"status":"Add Success"}

@app.get("/search/search_car_by_brand", tags=["cars"])
async def search_car_by_brand(name:str):
    search_car = testalog.search_car_by_brand(name)
    return {"search found":[{"car_brand": x.get_car_brand(),
                        "car_model": x.get_car_model(),
                        "car_amount": x.get_car_amount(),
                        "car_plate_number": x.get_car_plate_number(),
                        "car_rating": x.get_rating_score()}
                       for x in search_car]}

@app.get("/search/search_car_by_model", tags=["cars"])
async def search_car_by_model(name:str):
    search_car = testalog.search_car_by_model(name)
    return {"search found":[{"car_brand": x.get_car_brand(),
                        "car_model": x.get_car_model(),
                        "car_amount": x.get_car_amount(),
                        "car_plate_number": x.get_car_plate_number(),
                        "car_rating": x.get_rating_score()}
                       for x in search_car]}

#Booking
@app.post("/get_available_car", tags=["Booking"])
async def get_available_car(data: AvalibleDTO):
    list_car = testalog.find_available_car(data.start_date,data.start_time,data.end_date,data.end_time)
    return list_car

@app.post("/book_car",tags = ["Booking"])
async def booking_car(data: BookingDTO,current_user = Depends(sym.get_current_user)):
    current_user._booking =testalog.book_car(data.car,data.start_date,data.start_time,data.end_date,data.end_time)
    return current_user._booking

@app.post("/add_rating" ,tags=["Cars"])
async def add_rating(data:AddRateDTO):
    cars=testalog.find_car_by_plate(data.car_plate)
    cars.add_rating(Rating(data.score,data.comment))
    return {"status":"Add Success"}

##### CREDIT ###### E D I T I N G
@app.post("/add_credit_info", tags=["CreditCard"])
async def add_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
    current_user.add_credit_info(CreditInfo(data.exprie_card,data.card_number,data.security_credit))
    return current_user._credit_card

@app.post("/edit_credit_info", tags=["CreditCard"])
async def edit_credit_info(data:CreditCard,current_user= Depends(sym.get_current_user)):
    current_user._credit_card.edit_credit_info(data.exprie_card,data.card_number,data.security_credit)
    return current_user._credit_card

#FavouriteCar
@app.post("/add_favourite",tags = ["Favourite"])
async def add_favourite(data:FavouriteDTO,current_user= Depends(sym.get_current_user)):
    car_fav = testalog.find_car_by_plate(data.car)
    current_user.add_fav_car(car_fav)
    return {"status":"Success"}
#เเก้
@app.post("/watch_favourite",tags = ["Favourite"])
async def watch_favourite(current_user= Depends(sym.get_current_user)):
    return current_user.watch_fav_car()

@app.get("/Payment",tags =["Payment"])
async def make_payment(current_user = Depends(sym.get_current_user)):
    status = False
    transaction_id = random.randint(100000000,999999999)
    rental_price = current_user._booking.get_price()
    credit_info = current_user._credit_card
    payment = Payment(rental_price,status,transaction_id,credit_info)
    return payment


# @app.post("/watch ",tags = ["Favourite"])
# async def add_favourite(data:FavouriteDTO):
#     petch.add_fav_car(data.car)
#     return {"status":"Success"}
    
    


#Credit_Card

#Payment


# @app.get("/watch_favourite_car",tags = ["Favourite"])
# async def add_favourite(request:Request):
#     data.username = FavouriteCar
#     petch.add_fav_car(data.car,data.username)
#     return "Add Favourite Successful"

# @app.get("/add_favorite",tags = ["booking"])
# async def

# booking =testalog.book_car("ABZW-999","11-6-2018","9:00","12-6-2018","9:59")
# booking.show_booking()





