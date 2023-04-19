from tkinter import *
from tkinter.font import *
import requests
import json

class edit_profile:
    def __init__(self):
        self.__ep = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__ep.title("Edit Profile")
        self.__ep.geometry("400x400")
        self.__ep.resizable(width=False, height=False)

        Label(text="Edit", font=self.__header_font).pack(anchor="center")
        Label(text="name:", font=self.__normal_font).place(x=25, y=50)
        self.__name_entry = Entry(self.__ep, font=self.__txtbox_font)
        self.__name_entry.place(x=130, y=50)


        Label(text="username:", font=self.__normal_font).place(x=25, y=80)
        self.__username_entry = Entry(self.__ep, font=self.__txtbox_font)
        self.__username_entry.place(x=130, y=80)


        Label(text="phone number:", font=self.__normal_font).place(x=25, y=110)
        self.__phone_number_entry = Entry(self.__ep, font=self.__txtbox_font)
        self.__phone_number_entry.place(x=130, y=110)


        Label(text="password:", font=self.__normal_font).place(x=25, y=140)
        self.__password_entry = Entry(self.__ep, font=self.__txtbox_font)
        self.__password_entry.place(x=130, y=140)


        Label(text="email:", font=self.__normal_font).place(x=25, y=170)
        self.__email_entry = Entry(self.__ep, font=self.__txtbox_font)
        self.__email_entry.place(x=130, y=170)

        Button(text="Confirm", font=self.__normal_font, command = self.edit_profile_V2).place(x=110, y=200)

        self.__ep.mainloop()

    def edit_profile_V2(self):
        url = "http://127.0.0.1:8000/users/me/modify"
        data = {
                    "new_name": str(self.__name_entry.get()),
                    "new_username": str(self.__username_entry.get()),
                    "new_phone_num": str(self.__phone_number_entry.get()),
                    "new_password":str(self.__password_entry.get()),
                    "new_email": str(self.__email_entry.get())
                }
        r = requests.post(url, json = data)
        print(json.loads(r.text))

edit_profile()


