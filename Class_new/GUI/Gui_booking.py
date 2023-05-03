from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial
from Gui_payment import Payment

class bookingGUI:
    
    def __init__(self,plate,token):

        self.__booking = Tk()
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__booking.title("Booking")
        self.__booking.geometry("450x350")
        self.__booking.resizable(width=False, height=False)
        
        #setting
        self.__token = token
        self.__plate = plate
        
        Label(text="Booking", font=self.__title_font).pack()
        Label(text="Start_date :", font=self.__normal_font).place(x=10, y=50)
        self.__sd_entry = Entry(self.__booking, font=self.__normal_font)
        self.__sd_entry.place(x=140, y=50)
        
        Label(text="Start_time :", font=self.__normal_font).place(x=10, y=100)
        self.__st_entry = Entry(self.__booking, font=self.__normal_font)
        self.__st_entry.place(x=140, y=100)
        
        Label(text="End_date :", font=self.__normal_font).place(x=10, y=150)
        self.__ed_entry = Entry(self.__booking, font=self.__normal_font)
        self.__ed_entry.place(x=140, y=150)
        
        Label(text="End_time :", font=self.__normal_font).place(x=10, y=200)
        self.__et_entry = Entry(self.__booking, font=self.__normal_font)
        self.__et_entry.place(x=140, y=200)
        
        Button(text="Confirm Booking", font=self.__normal_font, command = self.booking).place(x=50, y=250)
        
        Button(text="Go to payment", font=self.__normal_font, command = self.payment).place(x=230, y=250)
        self.__booking.mainloop()
    
    
    
    def booking(self):
        url = 'http://127.0.0.1:8000/book_car'
        data = {
                    "car_plate": self.__plate,
                    "start_date": self.__sd_entry.get(),
                    "start_time": self.__st_entry.get(),
                    "end_date": self.__ed_entry.get(),
                    "end_time": self.__et_entry.get()
                }
        r = requests.post(url, json = data,headers={'Authorization': "Bearer "+self.__token})
        status =json.loads(r.text)
        print(status)
        if status["status"] == 'Booking Success':
            tkinter.messagebox.showinfo(title="Success", message="Booking Success!!!!")       
        else:
            tkinter.messagebox.showinfo(title="Error", message="Booking Fail")    
            
    
    def payment(self):
        self.__booking.destroy()
        Payment(self.__plate,self.__token)
        
        
        
     
        
    
    