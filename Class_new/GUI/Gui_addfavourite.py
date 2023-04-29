from tkinter import *
from tkinter.font import *
import json
import requests

class AddFavourite:
    def __init__(self,token):
        self.__add_favourite = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        self.__add_favourite.title("Add_favourite")
        self.__add_favourite.geometry("400x400")
        self.__add_favourite.resizable(width=False, height=False)

        Label(text="Add Favourite", font=self.__title_font).pack(anchor="center")
        Label(text="expire_card:", font=self.__normal_font).place(x=25, y=50)
        self.name_entry = Entry(self.__add_favourite, font=self.__text_font)
        self.name_entry.place(x=130, y=50)


        Label(text="card_number:", font=self.normal_font).place(x=25, y=80)
        self.username_entry = Entry(self.ep, font=self.txtbox_font)
        self.username_entry.place(x=130, y=120)


        Label(text="security_credit:", font=self.normal_font).place(x=25, y=110)
        self.phone_number_entry = Entry(self.ep, font=self.txtbox_font)
        self.phone_number_entry.place(x=130, y=190)

        Button(text="Confirm", font=self.normal_font, command = self.edit_profile_V2).place(x=110, y=200)

        self.ep.mainloop()

    def add_credit(self):
        url = "http://127.0.0.1:8000/add_credit_info"
        data = {
                    "new_name": str(self.name_entry.get()),
                    "new_username": str(self.username_entry.get()),
                    "new_phone_num": str(self.phone_number_entry.get()),
                    "new_password":str(self.password_entry.get()),
                    "new_email": str(self.email_entry.get())
                }
        r = requests.post(url, json = data)
        print(json.loads(r.text))

add_credit()
        
        