from datetime import datetime
from fastapi import FastAPI




app = FastAPI()

# object รถ
class Car:
    def __init__(self, brand, model, fuel_type, fuel_used, feature, door, insurance, seat, amount, description, plate_number, rating_review, price_perday):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.fuel_used = fuel_used
        self.feature = feature
        self.door = door
        self.insurance = insurance
        self.seat = seat
        self.amount = amount
        self.description = description
        self.plate_number = plate_number
        self.rating_review = rating_review
        self.price_perday = price_perday

# Object รายระเอียดของการจอง


class Booking:
    def __init__(self, car, renter_name, renter_phone, rent_start_date, rent_end_date):
        self.car = car
        self.renter_name = renter_name
        self.renter_phone = renter_phone
        self.rent_start_date = datetime.strptime(rent_start_date, '%Y-%m-%d')
        self.rent_end_date = datetime.strptime(rent_end_date, '%Y-%m-%d')

    def calculate_total_price(self):
        return self.car.price_perday * (self.rent_end_date - self.rent_start_date).days

    def __str__(self):
        return f"Booking Details:\n\n{self.car.brand} {self.car.model}\nRenter Name: {self.renter_name}\nRenter Phone: {self.renter_phone}\nRent Start Date: {self.rent_start_date}\nRent End Date: {self.rent_end_date}"

# ส่วนของระบบการเช่ายืมทั้งหมด


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.bookings = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} has been added to the system.")

    def remove_car(self, car):
        self.cars.remove(car)
        print(f"{car.brand} {car.model} has been removed from the system.")

    def check_availability(self, car, start_date, end_date):
        start_date = datetime.strptime(start_date,'%Y-%m-%d')
        end_date = datetime.strptime(end_date,'%Y-%m-%d')
        for booking in self.bookings:
            if booking.car == car:
                if start_date <= booking.rent_start_date <= end_date or start_date <= booking.rent_end_date <= end_date:
                    return False
        return True

    def calculate_price(self,car,rent_start_date,rent_end_date):
        rent_start_date = datetime.strptime(rent_start_date,'%Y-%m-%d')
        rent_end_date = datetime.strptime(rent_end_date,'%Y-%m-%d')
        price_perday = car.price_perday
        rental_days = (rent_end_date - rent_start_date).days
        total_price = price_perday * rental_days
        return total_price
    
system = CarRentalSystem()

@app.get('/')
async def root():
    return {"message": "Welcome to the car rental system."}

@app.post("/cars")
async def add_car(brand, model, fuel_type, fuel_used, feature, door, insurance, seat, amount, description, plate_number, rating_review, price_perday):
    car = Car(brand=brand, model=model, fuel_type=fuel_type, fuel_used=fuel_used, feature=feature, door=door, insurance=insurance, seat=seat, amount=amount, description=description, plate_number=plate_number, rating_review=rating_review, price_perday=price_perday)
    system.add_car(car)
    return {"message": f"{brand} {model} has been added to the system."}

@app.delete('/cars')
async def delete_cars(brand,model):
    for car in system.cars:
        if car.brand == brand and car.model == model:
            system.remove_car(car)
            return {"message":f"{brand}{model} has been removed"}

@app.get('/cars')
async def view_available_cars(start_date, end_date):
    available_cars = []
    for car in system.cars:
        if system.check_availability(car, start_date, end_date):
            available_cars.append(f"{car.brand} {car.model}")
    if available_cars:
        return {"message": "Available cars", "cars": available_cars}
    else:
        return {"message": "No car available"}
    
@app.post('/bookings')
async def make_booking(car_brand, car_model, renter_name, renter_phone, rent_start_date, rent_end_date):
    # ค้นหารถที่ว่างในช่วงเวลานี้
    available_cars = []
    for car in system.cars:
        if system.check_availability(car, rent_start_date, rent_end_date) and car.brand == car_brand and car.model == car_model:
            available_cars.append(car)

    # ตรวจสอบว่ามีรถว่างหรือไม่
    if not available_cars:
        return {"message": "No car available for booking."}

    # ทำการจองรถ
    car = available_cars[0]
    booking = Booking(car=car, renter_name=renter_name, renter_phone=renter_phone, rent_start_date=rent_start_date, rent_end_date=rent_end_date)
    system.bookings.append(booking)

    # คำนวณราคาสุทธิและส่งข้อความการจองกลับ
    total_price = booking.calculate_total_price()
    message = str(booking) + f"\nTotal Price: {total_price} THB"
    return {"message": message}



         







         






