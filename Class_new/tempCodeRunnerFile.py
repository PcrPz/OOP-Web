#Booking
@app.post("/get_available_car", tags=["Booking"])
async def get_available_car(data: AvalibleDTO):
    list_car = testalog.find_available_car(data.start_date,data.start_time,data.end_date,data.end_time)
    return list_car

@app.post("/book_car",tags = ["Booking"])
async def booking_car(data: BookingDTO):
    booking =testalog.book_car(data.car,data.start_date,data.start_time,data.end_date,data.end_time)
    show_book = booking.show_booking()
    return show_book