from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial
from Gui_credit import addcredGUI

class Payment:
    
    def __init__(self,plate,token):
        self.__payment= Tk()
        self.__plate = plate
        self.__token =token
        
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        #setting 
        self.__payment.title("PeakyBlindestShop")
        self.__payment.geometry("450x350")
        self.__payment.resizable(width=False, height=False)
        
        Label(text="Payment", font=self.__title_font).pack()
        
        r = requests.get(f'http://127.0.0.1:8000/find Car?plate={self.__plate}')
        car=json.loads(r.text)
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.__token})
        self.user = json.loads(r.text)
        print(self.user['_Renter__booking']['_Booking__day_start'])
        Label(text="Price: "+str(self.user['_Renter__booking']["_Booking__price"]), font=self.__normal_font ).place(x=10,y=60)
        Label(text="Car Plate: "+self.__plate, font=self.__normal_font ).place(x=10,y=100)
        Label(text="Day Start: "+self.user['_Renter__booking']["_Booking__day_start"], font=self.__normal_font ).place(x=10,y=140)
        Label(text="Day End: "+self.user['_Renter__booking']["_Booking__day_end"], font=self.__normal_font ).place(x=10,y=180)
        Button(text="Cancel Booking", font=self.__normal_font, command = self.cancel).place(x=0, y=250)
        
        Button(text="Make Payment&Add Credit", font=self.__normal_font, command = self.add_credit).place(x=170, y=250)
        self.__payment.mainloop()
        
        
    def cancel(self):
        url = 'http://127.0.0.1:8000/Cancel Booking'
        r = requests.delete(url,headers={'Authorization': "Bearer "+self.__token})
        status =json.loads(r.text)
        print(status)
        if status["status"] == "Success":
            tkinter.messagebox.showinfo(title="Success", message="Cancel Success!!!!")
            self.__payment.destroy()         
        else:
            tkinter.messagebox.showinfo(title="Error", message="Cancel Fail")

            
    
    def add_credit(self):
        self.__payment.destroy()
        addcredGUI(self.__plate,self.__token)
        
        
        