from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial
from Gui_detailcar import Detail
from Gui_avalible import GetAvailableCarGUI

class CarCatalogTK:
    
    def __init__(self,token):
        self.__car_catalog = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12) 
        self.__token = token
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.__token})
        self.user = json.loads(r.text)
        print(self.user['_contact_type'])
        print(self.user['_contact_name'])
        
        #setting 
        self.__car_catalog.title("PeakyBlindestShop")
        self.__car_catalog.geometry("800x800")
        self.__car_catalog.resizable(width=False, height=False)
        
        #value
        self.__car_count = 0
        self.__list_car_to_show =[]
        self.__row_base = 130
        self.__bgcolor = "#242424"
        self.__txtcolor = "white"
        #menu
        self.__main_menu = Menu()
        self.__hello = Menu()
        self.__owner = Menu()
        self.__user = Menu()
        self.__hello.add_command(label="View Profile",command=self.view_profile)
        self.__hello.add_command(label="Edit_Profile",command=self.edit_profile)
        self.__hello.add_command(label="Watch_Favourite",command=self.watch_favourite)
        self.__hello.add_command(label="Watch_History",command=self.watch_history)#ใส่history---------------------
        self.__owner.add_command(label="Add Car",command=self.add_car)
        self.__main_menu.add_cascade(label="Setting",menu=self.__hello)
        self.__main_menu.add_cascade(label="Owner",menu=self.__owner)
        self.__main_menu.add_cascade(label="Your Account : "+self.user['_contact_name'],menu=self.__user)
        self.__car_catalog.config(menu=self.__main_menu)

        #interface
        Label(text="PeakyBlindestShop", font=self.__title_font).pack()
        Button(text='Find Avalible', font=self.__normal_font,command=self.find_avalible,
                   fg='#000000', bg="#40e0d0", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor).place(x=90,y=60)
        Button(text='Search By Brand', font=self.__normal_font,
                   fg='#000000', bg="#40e0d0", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor).place(x=300,y=60)
        Button(text='Search By Model', font=self.__normal_font,
                   fg='#000000', bg="#40e0d0", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor).place(x=540,y=60)
        self.show_car()
        
        
        
        if self.__car_count % 4 == 0:   
            for i in range(0,self.__car_count,4):
                for j in range(4):
                    Label(text='Brand :'+self.__list_car_to_show[i+j]['car_brand'], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
                    Label(text='Model :'+self.__list_car_to_show[i+j]['car_model'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
                    Label(text='Price :'+str(self.__list_car_to_show[i+j]['car_amount']), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
                    Label(text='Plate :'+self.__list_car_to_show[i+j]['car_plate_number'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+90)
                    Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j]["car_plate_number"])),fg=self.__txtcolor, 
                           bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*j, y=self.__row_base+125)
                self.__row_base +=185

        else: 
            num = self.__car_count%4
            for i in range(0,self.__car_count-4,4):
                for j in range(4):
                    Label(text='Brand :'+self.__list_car_to_show[i+j]['car_brand'], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
                    Label(text='Model :'+self.__list_car_to_show[i+j]['car_model'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
                    Label(text='Price :'+str(self.__list_car_to_show[i+j]['car_amount']), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
                    Label(text='Plate :'+self.__list_car_to_show[i+j]['car_plate_number'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+90)
                    Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j]["car_plate_number"])),fg=self.__txtcolor, 
                           bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*j, y=self.__row_base+125)
                self.__row_base +=185
            for k in range(num):
                    Label(text='Brand :'+self.__list_car_to_show[i+j+k+1]['car_brand'], font=self.__normal_font).place(x=50+175*k,y=self.__row_base)
                    Label(text='Model :'+self.__list_car_to_show[i+j+k+1]['car_model'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+30)
                    Label(text='Price :'+str(self.__list_car_to_show[i+j+k+1]['car_amount']), font=self.__normal_font).place(x=50+175*k, y=self.__row_base+60)
                    Label(text='Plate :'+self.__list_car_to_show[i+j+k+1]['car_plate_number'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+90)
                    Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j+k+1]["car_plate_number"])),fg=self.__txtcolor, 
                           bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*k, y=self.__row_base+125)
            
            
        
        
        self.__car_catalog.mainloop()
        
        
        
    def show_car(self):
        res = requests.get('http://127.0.0.1:8000/cars')
        all_cata = json.loads(res.text)["catalog"]
        self.__car_count = len(all_cata)
        print(len(all_cata))
        for i in all_cata:
            self.__list_car_to_show.append(i)
        print("")
        
    #menu function    
    def view_profile(self):
        self.__car_catalog.destroy()
        View_Profile(self.__token)
        
    def edit_profile(self):
        self.__car_catalog.destroy()
        Edit_Profile(self.__token)
        
    def watch_favourite(self):
        self.__car_catalog.destroy()
        Watch_favourite(self.__token)
        
    def watch_history(self):
        self.__car_catalog.destroy()
        Watch_history(self.__token)
        
    #button function
    def more_detail(self,plate):
        self.__car_catalog.destroy()
        Detail(plate,self.__token)
        
    def find_avalible(self):
        self.__car_catalog.destroy()
        GetAvailableCarGUI(self.__token)
        
        
    #owner menu   
    def add_car(self):
        self.__car_catalog.destroy()
        AddCar(self.__token)      
        
#Addcar--------------------------------------------------      
class AddCar:
    def __init__(self, token):
        self.__add_car = Tk()
        # font
        self.title_font = Font(family="Kanit", weight="bold", size=20)
        self.normal_font = Font(family="Kanit", weight="normal", size=16)
        self.text_font = Font(family="Kanit", weight="normal", size=12)
        self.__token = token
        # font
        self.__add_car.title("Add Car")
        self.__add_car.geometry("400x750")
        self.__add_car.resizable(width=False, height=False)

        Label(text="Add Car", font=self.title_font).pack(anchor="center")

        # Car Brand
        Label(text="Car Brand:", font=self.normal_font).place(x=20, y=50)
        self.brand_entry = Entry(self.__add_car, font=self.text_font)
        self.brand_entry.place(x=160, y=50)

        # Car Model
        Label(text="Car Model:", font=self.normal_font).place(x=20, y=100)
        self.model_entry = Entry(self.__add_car, font=self.text_font)
        self.model_entry.place(x=160, y=100)

        # Fuel Type
        Label(text="Fuel Type:", font=self.normal_font).place(x=20, y=150)
        self.fuel_type_entry = Entry(self.__add_car, font=self.text_font)
        self.fuel_type_entry.place(x=160, y=150)

        # Fuel Used
        Label(text="Fuel Used:", font=self.normal_font).place(x=20, y=200)
        self.fuel_used_entry = Entry(self.__add_car, font=self.text_font)
        self.fuel_used_entry.place(x=160, y=200)

        # Car Feature
        Label(text="Car Feature:", font=self.normal_font).place(x=20, y=250)
        self.feature_entry = Entry(self.__add_car, font=self.text_font)
        self.feature_entry.place(x=160, y=250)

        # Car Door
        Label(text="Car Door:", font=self.normal_font).place(x=20, y=300)
        self.door_entry = Entry(self.__add_car, font=self.text_font)
        self.door_entry.place(x=160, y=300)

        # Car Insurance
        Label(text="Car Insurance:", font=self.normal_font).place(x=20, y=350)
        self.insurance_entry = Entry(self.__add_car, font=self.text_font)
        self.insurance_entry.place(x=160, y=350)

        # Car Seat
        Label(text="Car Seat:", font=self.normal_font).place(x=20, y=400)
        self.seat_entry = Entry(self.__add_car, font=self.text_font)
        self.seat_entry.place(x=160, y=400)

        # Car Amount
        Label(text="Car Amount:", font=self.normal_font).place(x=20, y=450)
        self.amount_entry = Entry(self.__add_car, font=self.text_font)
        self.amount_entry.place(x=160, y=450)

        # Car About
        Label(text="Car About:", font=self.normal_font).place(x=20, y=500)
        self.about_entry = Entry(self.__add_car, font=self.text_font)
        self.about_entry.place(x=160, y=500)

        # Car Plate Number
        Label(text="Plate Number:", font=self.normal_font).place(x=20, y=550)
        self.plate_entry = Entry(self.__add_car, font=self.text_font)
        self.plate_entry.place(x=160, y=550)

        Button(text="Confirm Add Car", font=self.normal_font, command=self.add_car).place(x=100, y=635)
        Button(text="Back", font=self.normal_font, command=self.back).place(x=300, y=635)
        self.__add_car.mainloop()
        
    def back(self):
        self.__add_car.destroy()
        CarCatalogTK(self.__token)
    
    def add_car(self):
        data = {
                        "car_brand": self.brand_entry.get(),
                        "car_model": self.model_entry.get(),
                        "fuel_type": self.fuel_type_entry.get(),
                        "fuel_used": self.fuel_used_entry.get(),
                        "car_feature": self.feature_entry .get(),
                        "car_door": self.door_entry.get(),
                        "car_insurance": self.insurance_entry.get(),
                        "car_seat": self.seat_entry.get(),
                        "car_amount": int(self.amount_entry.get()),
                        "car_about": self.about_entry.get(),
                        "car_plate_number": self.plate_entry.get()
                    }
        r = requests.post('http://127.0.0.1:8000/add_car', json=data,headers={'Authorization': "Bearer " + self.__token})
        if json.loads(r.text)["status"] == "Add Success":
            tkinter.messagebox.showinfo(title="Success", message="Add Car Success!!!!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Add Car Fail!!!")
                    
#View Profile---------------------------------------------------------------------------                   
class View_Profile:
    def __init__(self,token):
        self.__view_profile = Tk()
        self.__token = token
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        self.__view_profile.title("Your Profile")
        self.__view_profile.geometry("400x300")
        self.__view_profile.resizable(width=False, height=False)
        Label(text="Your Profile", font=self.__title_font).pack()
        
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.__token})
        self.user = json.loads(r.text)
        self.name =(self.user["_contact_name"])
        self.username =(self.user["_contact_username"])
        self.phone =(self.user["_contact_phone_num"])
        self.password =(self.user["_contact_password"])
        self.email =(self.user["_contact_email"])
        self.type =(self.user["_contact_type"])
        
        Label(text=f"Your name is {self.name}", font=self.__normal_font).place(x=10, y=43)
        Label(text=f"Your username is {self.username}", font=self.__normal_font).place(x=10, y=80)
        Label(text=f"Your phone-number is {self.phone}", font=self.__normal_font).place(x=10, y=120)
        Label(text=f"Your password is {self.password}", font=self.__normal_font).place(x=10, y=160)
        Label(text=f"Your email is {self.email}", font=self.__normal_font).place(x=10, y=200)
        Label(text=f"Your type is {self.type}", font=self.__normal_font).place(x=10, y=240)
        
        Button(text="Back", font=self.__normal_font, command=self.back_catalog).place(x=300, y=230)
        
        self.__view_profile.mainloop()  
        
    def back_catalog(self):
        self.__view_profile.destroy()
        CarCatalogTK(self.__token)
        
#Edit Profile---------------------------------------------------------------------------
class Edit_Profile:
    def __init__(self,token):
        self.__edit_profile = Tk()
        self.__token = token
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        self.__edit_profile.title("Add_favourite")
        self.__edit_profile.geometry("400x250")
        self.__edit_profile.resizable(width=False, height=False)

        Label(text="Edit Profile", font=self.__title_font).pack(anchor="center")
        Label(text="Phone_num:", font=self.__normal_font).place(x=20, y=50)
        self.phone_number_entry = Entry(self.__edit_profile, font=self.__text_font)
        self.phone_number_entry.place(x=150, y=50)
        
        Label(text="Password:", font=self.__normal_font).place(x=20, y=100)
        self.password_entry = Entry(self.__edit_profile, font=self.__text_font)
        self.password_entry.place(x=150, y=100)
        
        Label(text="Email:", font=self.__normal_font).place(x=20, y=150)
        self.email_entry = Entry(self.__edit_profile, font=self.__text_font)
        self.email_entry.place(x=150, y=150)
        Button(text="Confirm Edit", font=self.__normal_font, command=self.modify).place(x=100, y=185)
        Button(text="Back", font=self.__normal_font, command=self.back_catalog).place(x=300, y=185)
        
        self.__edit_profile.mainloop()
        
    def back_catalog(self):
        self.__edit_profile.destroy()
        CarCatalogTK(self.__token)
        
    def modify(self):
        url = 'http://127.0.0.1:8000/users/me/modify'
        data = {
                    "new_phone_num": str(self.phone_number_entry.get()),
                    "new_password": str(self.password_entry.get()),
                    "new_email": str(self.email_entry.get())
                }
        r = requests.put(url, json = data,headers={'Authorization': "Bearer "+self.__token})
        if json.loads(r.text)["status"] == "Success":
            tkinter.messagebox.showinfo(title="Success", message="Edit Success!!!!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Edit Fail!!!")
    
            
                    
#Watch Fav---------------------------------------------------------------------------      
class Watch_favourite:
    def __init__(self,token):
        self.__watch_fav = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        self.__watch_fav.title("Watch Favourite")
        self.__watch_fav.geometry("800x800")
        self.__watch_fav.resizable(width=False, height=False)
        
        #value
        self.__token = token
        self.__car_count = 0
        self.__list_car_to_show =[]
        self.__row_base = 75
        
        Label(text="Favourite List", font=self.__title_font).pack()
        self.show_car()

    
        if self.__car_count % 4 == 0:
            for i in range(0,self.__car_count,4):
                for j in range(4):
                    Label(text='Brands :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
                    Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
                    Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
                self.__row_base +=120

        else: 
            num = self.__car_count%4
            get_i = 0
            get_j = 0
            for i in range(0,self.__car_count-4,4):
                get_i = i
                for j in range(4):
                    get_j = j
                    Label(text='Brand :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
                    Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
                    Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
                self.__row_base +=120
            for k in range(num):
                Label(text='Brand :'+self.__list_car_to_show[get_i+get_j+k]['brand'], font=self.__normal_font).place(x=50+175*k,y=self.__row_base)
                Label(text='Model :'+self.__list_car_to_show[get_i+get_j+k]['model'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+30)
                Label(text='Price :'+str(self.__list_car_to_show[get_i+get_j+k]['price']), font=self.__normal_font).place(x=50+175*k, y=self.__row_base+60)
            
            
        Button(text="Back", font=self.__normal_font, command=self.back_catalog).place(x=700, y=10)
        self.__watch_fav.mainloop()
        
    def back_catalog(self):
        self.__watch_fav.destroy()
        CarCatalogTK(self.__token)
          
        
    def show_car(self):
        r = requests.get('http://127.0.0.1:8000/watch_favourite',headers={'Authorization': "Bearer "+self.__token})
        res = json.loads(r.text)["FavouriteCar"]
        self.__car_count = len(res)
        for car in res:
            self.__list_car_to_show.append(car)
            
class Watch_history:
    def __init__(self,token):
        self.__watch_his = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        self.__watch_his.title("Watch History")
        self.__watch_his.geometry("800x800")
        self.__watch_his.resizable(width=False, height=False)
        
        #value
        self.__token = token
        self.__car_count = 0
        self.__list_car_to_show =[]
        self.__row_base = 75
        
        Label(text="History List", font=self.__title_font).pack()
        self.show_car()

    
        # if self.__car_count % 4 == 0:
        #     for i in range(0,self.__car_count,4):
        #         for j in range(4):
        #             Label(text='Brands :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
        #             Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
        #             Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
        #         self.__row_base +=120

        # else: 
        #     num = self.__car_count%4
        #     get_i = 0
        #     get_j = 0
        #     for i in range(0,self.__car_count-4,4):
        #         get_i = i
        #         for j in range(4):
        #             get_j = j
        #             Label(text='Brand :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
        #             Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
        #             Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
        #         self.__row_base +=120
        #     for k in range(num):
        #         Label(text='Brand :'+self.__list_car_to_show[get_i+get_j+k]['brand'], font=self.__normal_font).place(x=50+175*k,y=self.__row_base)
        #         Label(text='Model :'+self.__list_car_to_show[get_i+get_j+k]['model'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+30)
        #         Label(text='Price :'+str(self.__list_car_to_show[get_i+get_j+k]['price']), font=self.__normal_font).place(x=50+175*k, y=self.__row_base+60)
            
            
        Button(text="Back", font=self.__normal_font, command=self.back_catalog).place(x=700, y=10)
        self.__watch_his.mainloop()
        
    def back_catalog(self):
        self.__watch_his.destroy()
        CarCatalogTK(self.__token)
          
        
    def show_car(self):
        r = requests.get('http://localhost:8000/watch_history',headers={'Authorization': "Bearer "+self.__token})
        res = json.loads(r.text)
        # self.__car_count = len(res)
        # for car in res:
        #     self.__list_car_to_show.append(car)
            

            
# class Watch_history:
#     def __init__(self,token):
#         self.__watch_hist = Tk()
#         #font
#         self.__title_font = Font(family="Kanit", weight="bold", size=20)
#         self.__normal_font = Font(family="Kanit", weight="normal", size=16)
#         self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
#         self.__watch_hist.title("Watch Favourite")
#         self.__watch_hist.geometry("800x800")
#         self.__watch_hist.resizable(width=False, height=False)
        
#         #setting
#         self.__token = token
#         self.__car_count = 0
#         self.__list_car_to_show =[]
#         self.__row_base = 75
        
#         Label(text="Favourite List", font=self.__title_font).pack()
#         self.show_car()

    
#         if self.__car_count % 4 == 0:
#             for i in range(0,self.__car_count,4):
#                 for j in range(4):
#                     Label(text='Brands :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
#                     Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
#                     Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
#                 self.__row_base +=120

#         else: 
#             num = self.__car_count%4
#             get_i = 0
#             get_j = 0
#             for i in range(0,self.__car_count-4,4):
#                 get_i = i
#                 for j in range(4):
#                     get_j = j
#                     Label(text='Brand :'+self.__list_car_to_show[i+j]["brand"], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
#                     Label(text='Model :'+self.__list_car_to_show[i+j]["model"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
#                     Label(text='Price :'+str(self.__list_car_to_show[i+j]["price"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
#                 self.__row_base +=120
#             for k in range(num):
#                 Label(text='Brand :'+self.__list_car_to_show[get_i+get_j+k]['brand'], font=self.__normal_font).place(x=50+175*k,y=self.__row_base)
#                 Label(text='Model :'+self.__list_car_to_show[get_i+get_j+k]['model'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+30)
#                 Label(text='Price :'+str(self.__list_car_to_show[get_i+get_j+k]['price']), font=self.__normal_font).place(x=50+175*k, y=self.__row_base+60)
            
            
#         Button(text="Back", font=self.__normal_font, command=self.back_catalog).place(x=700, y=10)
#         self.__watch_hist.mainloop()
        
#     def back_catalog(self):
#         self.__watch_hist.destroy()
#         CarCatalogTK(self.__token)
    
#     def show_car(self):
#         r = requests.get('http://127.0.0.1:8000/watch_favourite',headers={'Authorization': "Bearer "+self.__token})
#         res = json.loads(r.text)["FavouriteCar"]
#         self.__car_count = len(res)
#         for car in res:
#             self.__list_car_to_show.append(car)       
          
            


    
        

            