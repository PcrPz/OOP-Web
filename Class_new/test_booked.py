from datetime import datetime
import random
#object รถ
class Car:
    def __init__(self, brand, model, fuel_type, fuel_used, feature, door, insurance, seat, amount, description, plate_number, rating_review,price_perday):
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

#เก็บรายระเอียดของการจอง 
class Booking:
    def __init__(self, car, renter_name, renter_phone, rent_start_date, rent_end_date,rental_price,booked_number):
        self.__car = car
        self.__renter_name = renter_name
        self.__renter_phone = renter_phone
        self.__rent_start_date = rent_start_date
        self.__rent_end_date = rent_end_date
        self.__rental_price = rental_price
        self.__booked_number = booked_number

    def get_car(self):
        return self.__car

    def get_renter_name(self):
        return self.__renter_name
    
    def get_renter_phone(self):
        return self.__renter_phone
    
    def get_rent_start_date(self):
        return self.__rent_start_date
    
    def get_rent_end_date(self):
        return self.__rent_end_date
    
    def get_rental_price(self):
        return self.__rental_price
    
    def get_booked_number(self):
        return self.__booked_number
        
    def __str__(self):
        return f"Booking Details:\n\n{self.car.brand} {self.car.model}\nRenter Name: {self.renter_name}\nRenter Phone: {self.renter_phone}\nRent Start Date: {self.rent_start_date}\nRent End Date: {self.rent_end_date}"
#ส่วนของระบบการเช่ายืมทั้งหมด
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.bookings = []
        self.booked_sequence = 0
        self.rental_price = 0

#เพิ่มรถ
    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.brand} {car.model} has been added to the system.")

#ลบรถ  
    def remove_car(self, car):
        self.cars.remove(car)
        print(f"{car.brand} {car.model} has been removed from the system.")

#ดูรถที่อยู่ในระบบทั้งหมด
    def view_cars(self):
        print("List of cars in the system:")
        for car in self.cars:
            print(f"{car.brand} {car.model}")

#ดูรถที่ว่าง ณ ช่วงเวลาหนึ่ง         
    def view_available_cars(self, start_date, end_date):
        print(f"Available cars between {start_date} and {end_date}:")
        #เช็ครถเเต่ละคนในช่วงเวลาที่ผู้เช่าต้องการจะเช่า
        for car in self.cars:
            if self.check_availability(car, start_date, end_date):
                print(f"{car.brand} {car.model}")
            else:
                print("No car available")
#ตัวเช็คว่ารถว่างไหม
    def check_availability(self, car, start_date, end_date):
        start_date = datetime.strptime(start_date,'%Y-%m-%d')
        end_date = datetime.strptime(end_date,'%Y-%m-%d')
        #ไล่ดูในลิสของ Bookings
        for booking in self.bookings:
            if booking.get_car() == car:
                #rent_start/end_date คือ วันที่จะจอง 
                if start_date <= booking.get_rent_start_date() <= end_date or start_date <= booking.get_rent_end_date() <= end_date:
                    return False
        return True
#ทำการจอง    
    def make_booking(self, car, renter_name, renter_phone, rent_start_date, rent_end_date):
        if self.check_availability(car, rent_start_date, rent_end_date):
            rent_start_date = datetime.strptime(rent_start_date,'%Y-%m-%d')
            rent_end_date = datetime.strptime(rent_end_date,'%Y-%m-%d')
            price_perday = car.price_perday
            rental_days = (rent_end_date - rent_start_date).days
            self.rental_price = price_perday * rental_days
            self.booked_sequence += 1
            new_booking = Booking(car, renter_name, renter_phone, rent_start_date, rent_end_date,self.rental_price,self.booked_sequence)
            self.bookings.append(new_booking)
            print("Booking confirmed!\n")
            print(f"Car: {car.brand}")
            print(f"Car: {car.model}")
            print(f"Renter name: {new_booking.get_renter_name()}")
            print(f"Renter phone: {new_booking.get_renter_phone()}")
            print(f"Rent start date: {new_booking.get_rent_start_date()}")
            print(f"Rent end date: {new_booking.get_rent_end_date()}")
            print(f"Total rental price: {new_booking.get_rental_price()}")
            print(f"Booked number:{new_booking.get_booked_number()}")
        else:
            print("This car is not available during the requested rental period.")

    def cancle_booking(self,booked_number):
        for booking in self.bookings:
            if booked_number == booking.get_booked_number():
                self.bookings.remove(booking)
                print(f"Booking with booked number {booked_number} has been cancelled.")
                return
        print(f"No booking found with booked number {booked_number}.")

    # def calculate_price(self,car,rent_start_date,rent_end_date):
    #     # rent_start_date = datetime.strptime(rent_start_date,'%Y-%m-%d')
    #     # rent_end_date = datetime.strptime(rent_end_date,'%Y-%m-%d')
    #     price_perday = car.price_perday
    #     rental_days = (rent_end_date - rent_start_date).days
    #     total_price = price_perday * rental_days
    #     return total_price
    
system = CarRentalSystem()
car1 = Car("Bmw","x8","benzene","4hr/L","good",4,True,4,2,"good","we1234",4.56,1000)
car2 = Car("ferrari","f40","benzene","4hr/L","good",4,True,4,2,"good","wx1324",4.1,2000)
car3 = Car("Porche","carrella","benzene","4hr/L","good",4,True,4,2,"good","ae1421",5,2500)

system.add_car(car1)
system.add_car(car2)
system.add_car(car3)

# system.view_available_cars("2023-04-07","2023-04-09")

system.make_booking(car1,"Watsaphon","0636015917","2023-04-08","2023-04-12")