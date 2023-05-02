from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from cataloggui import CarCatalogTK

class BookingHistory:
    def __init__(self):
        self.token = ""
        self.__BookingHistory = Tk()
        #font
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=14)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__BookingHistory.title("BookingHistory")
        self.__BookingHistory.geometry("350x350")
        self.__BookingHistory.resizable(width=False, height=False)

        Label(text="BookingHistory", font=self.__header_font).pack(anchor="center") #news
        Label(text="history_car_booking:", font=self.__normal_font).place(x=25, y=50) #direction
        self.__history_car_booking_entry = Entry(self.__BookingHistory, font=self.__txtbox_font)
        self.__history_car_booking_entry.place(x=250, y=50)

        Label(text="history_payment:", font=self.__normal_font).place(x=25, y=80)
        self.__history_payment_entry = Entry(self.__BookingHistory, font=self.__txtbox_font)
        self.__history_payment_entry.place(x=250, y=80)

        Button(text="Add To Booking History", font=self.__normal_font, command=self.BookingHistory).place(x=140, y=120)

        self.__BookingHistory.mainloop()
        
        
   
    def BookingHistory(self):
        url = "http://127.0.0.1:8000/add_booking_history"

        data = {          
                "history_car_booking": str(self.__history_car_booking_entry.get()),
                "history_payment": str(self.__history_payment_entry.get())
        }
        r = requests.post(url, json = data)
        print(json.loads(r.text))
        

            
BookingHistory()