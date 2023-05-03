from Car import *
from datetime import *
from fastapi import FastAPI
from dto import *
import random
from Contact import*
from CreditInfo import*
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
               "petch1",
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

#         "car": "ABZW-999",
#   "start_date": "11-6-2018",
#   "start_time": "9:00",
#   "end_date": "12-6-2018",
#   "end_time": "9:59"
# HOME
@app.get("/")
async def home():
    return {"Future_Car"}
#เคลีย GUI
#Login
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    status_user= sym.check_user(form_data.username,form_data.password)
    if not status_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = sym.get_user(form_data.username)
    return {"access_token": user.get_username(), "token_type": "bearer"}

#เคลีย GUI
#Register
@app.post("/registeration")
async def registeration(data:Registeration):
    if data.contact_type == "Owner":
        sym.add_user(Owner(data.contact_name,
                        data.contact_username, 
                        data.contact_phone_num, 
                        data.contact_password, 
                        data.contact_email))
        return {"message": "Register Success"}
    elif data.contact_type == "Renter":
        sym.add_user(Renter(data.contact_name,
                        data.contact_username, 
                        data.contact_phone_num, 
                        data.contact_password, 
                        data.contact_email))
        return {"message": "Register Success"}


@app.get("/users/me")
async def read_users_me(current_user = Depends(sym.get_current_user)):
    return current_user

#Modify Contact
#เคลีย GUI
@app.put("/users/me/modify")
async def edit_profile(data:EditProfileDTO,current_user= Depends(sym.get_current_user)):
    current_user.edit_profile(data.new_phone_num ,data.new_password , data.new_email )
    return {"status":"Success"}

#Cars
#เคลีย GUI
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
#เเก้เเล้ว
@app.post("/book_car",tags = ["Booking"])
async def booking_car(data: BookingDTO,current_user = Depends(sym.get_current_user)):
    current_user.set_booking(testalog.book_car(data.car_plate,data.start_date,data.start_time,data.end_date,data.end_time))#setter
    if current_user.get_booking() != None:
        return {"status": "Booking Success"}
    else:
        return {"status": "Fail"}

@app.post("/add_rating" ,tags=["Cars"])
async def add_rating(data:AddRateDTO):
    cars=testalog.find_car_by_plate(data.car_plate)
    cars.add_rating(Rating(data.score,data.comment))
    return {"status":"Add Success"}

#FavouriteCar
#เเก้
@app.post("/add_favourite",tags = ["Favourite"])
async def add_favourite(data:FavouriteDTO,current_user= Depends(sym.get_current_user)):
    if current_user.get_type() == "Owner":
        return {"message": "Fail"}
    elif current_user.get_type() == "Renter":
        car_fav = testalog.find_car_by_plate(data.car_plate)
        current_user.add_fav_car(car_fav)
        return {"status":"Success"}
#เคลีย GUI
@app.get("/watch_favourite",tags = ["Favourite"])
async def watch_favourite(current_user= Depends(sym.get_current_user)):
    return current_user.watch_fav_car()

@app.get("/watch_history",tags = ["History"])
async def watch_history(current_user= Depends(sym.get_current_user)):
    return current_user.watch_history()

@app.post("/Payment",tags =["Payment"])
#ไม่เก็บ
async def make_payment(data:CreditCardDTO,current_user = Depends(sym.get_current_user)):
    rental_price = current_user.get_booking().get_price()
    rental_booking = current_user.get_booking()
    credit_info = CreditInfo(data.card_number,data.exprie_card,data.security_number)
    payment = Payment(rental_price,credit_info)
    status = sym.make_payment(payment)
    if status == "Payment success" :
        current_user.get_booking().get_car().add_interval(current_user.get_booking().get_interval())
        current_user.add_history(rental_booking)
        current_user.set_booking(None)
    return {"status" : status}

@app.get("/find Car",tags = ["Find Car"])
async def find_car(plate:str):
    car = testalog.find_car_by_plate(plate)   
    return car


@app.delete("/Cancel Booking",tags =["Booking"])
#ไม่เก็บ
async def cancel_booking(current_user = Depends(sym.get_current_user)):
    current_user.cancel_booking()
    if current_user.get_booking() == None :
        return {"status":"Success"}
    else:
        return {"status":"Fail"}



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





