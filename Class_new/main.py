from Car import *
from datetime import *
from fastapi import FastAPI
from dto import *

from Contact import*
from Interval import*
from CarCatalog import*
from Rating import *
from Signup_Login import *
from System import *
from Bookingmanager import *
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
user_sys = SignupLogin()
testalog = CarCatalog()
manager = Bookingmanager()
testalog.add_car_to_catalog(bmw)
testalog.add_car_to_catalog(fer)
testalog.add_car_to_catalog(r35)
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
@app.get("/")
async def root():
    return {"message": "Hello World"}
#signup
@app.post("/signup", tags = ["Signup_Login"])
async def signup(user: User):
    if user_sys.add_user(user):
        return {"message": "Signup successful."}
    else:
        return {"message": "Username already taken."}
#login
@app.post("/login", tags = ["Signup_Login"])
async def login(username: str, password: str):
    if user_sys.is_valid_user(username, password):
        return {"message": "Login successful."}
    else:
        return {"message": "Invalid username or password"}

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

# @app.post(" ")
# async def modify_car_to_catalog(bookname, data:ModifyBookDTO):
#     x = testalog.find_book_by_name(bookname)
#     book.modify_car(data)
#     return {"status":"Success"}

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
async def booking_car(data: BookingDTO):
    booking =testalog.book_car(data.car,data.start_date,data.start_time,data.end_date,data.end_time,data.booked_num)
    manager.add_booking(booking)
    show_book = booking.show_booking()
    return show_book

@app.post("/cancle_booking",tags = ["Booking"])
async def cancle_booking(booked_num):
    for booking in manager.bookings:
        if booking.booked_num == booked_num:
            manager.bookings.remove(booking)
    return f"Cancle booking sucsessful."


@app.post("/add_rating" ,tags=["Cars"])
async def add_rating(data:AddRateDTO):
    cars=testalog.find_car_by_plate(data.car_plate)
    cars.add_rating(Rating(data.score,data.comment))
    return {"status":"Add Success"}

#FavouriteCar
@app.post("/add_favourite",tags = ["Favourite"])
async def add_favourite(data:FavouriteDTO,current_user= Depends(sym.get_current_user)):
    car_fav =testalog.search_car_by_brand(data.car)
    current_user.add_fav_car(car_fav)
    return {"status":"Success"}
#เเก้
@app.post("/watch_favourite",tags = ["Favourite"])
async def watch_favourite(current_user= Depends(sym.get_current_user)):
    show_fav=current_user.watch_fav_car()
    return show_fav



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





