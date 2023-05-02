from tkinter import *
from tkinter.font import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import requests
import json
from Gui_login import LoginGUI


class RegisterGUI:
    def __init__(self):
        self.__register = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        #setting 
        self.__register.title("Register")
        self.__register.geometry("350x300")
        self.__register.resizable(width=False, height=False)
        #interface
        Label(text="Register", font=self.__title_font).pack()
        Label(text="Username :", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = Entry(self.__register, font=self.__text_font)
        self.__username_entry.place(x=140, y=55)

        Label(text="Password :", font=self.__normal_font).place(x=25, y=80)
        self.__password_entry = Entry(self.__register, font=self.__text_font)
        self.__password_entry.place(x=140, y=85)

        Label(text="Email :", font=self.__normal_font).place(x=25, y=110)
        self.__email_entry = Entry(self.__register, font=self.__text_font)
        self.__email_entry.place(x=140, y=115)

        Label(text="Phone-num :", font=self.__normal_font).place(x=25, y=140)
        self.__phonenum_entry = Entry(self.__register, font=self.__text_font)
        self.__phonenum_entry.place(x=140, y=145)

        Label(text="Name :", font=self.__normal_font).place(x=25, y=170)
        self.__name_entry = Entry(self.__register, font=self.__text_font)
        self.__name_entry.place(x=140, y=175)

        Label(text="Role :", font=self.__normal_font).place(x=25, y=200)
        n = tk.StringVar()
        self.__roleChoose = ttk.Combobox(self.__register, width=10, textvariable=n)
        self.__roleChoose['values'] = ('Renter', 'Owner')
        self.__roleChoose.place(x=140, y=210)
        self.__roleChoose.current()


        Button(text="Confirm Register", font=self.__normal_font, command=self.register).place(x=10, y=240)
        Button(text="Go To Login", font=self.__normal_font, command=self.login).place(x=200, y=240)
        self.__register.mainloop()
        
    
    def register(self):

        if self.__username_entry.get() == "" or self.__password_entry.get() == "" or (
                self.__roleChoose.get() not in ['Owner', 'Renter']):
            tkinter.messagebox.showerror(message="Please enter a Username, Password and UserType", title="Error")
        else:
            data = {
                "contact_username": self.__username_entry.get(),
                "contact_password": self.__password_entry.get(),
                "contact_email": self.__email_entry.get(),
                "contact_phone_num": self.__phonenum_entry.get(),
                "contact_name": self.__name_entry.get(),
                "contact_type": self.__roleChoose.get(),
            }
            r = requests.post('http://127.0.0.1:8000/registeration', json=data)
            res = json.loads(r.text)["message"]
            if res == "Register Success":
                tkinter.messagebox.showinfo(title="Success", message="Register Success")
                
            else:
                tkinter.messagebox.showinfo(title="Error", message="Register Fail")
            
            
    def login(self):
        self.__register.destroy()
        LoginGUI()
            
            

RegisterGUI()     
        


    