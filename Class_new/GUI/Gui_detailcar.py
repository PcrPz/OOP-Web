from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial

class Detail:
    
    def __init__(self,plate,token):
        self.__detail = Tk()
        self.__plate = plate
        self.__token =token
        
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        
        #setting 
        self.__detail.title("PeakyBlindestShop")
        self.__detail.geometry("400x400")
        self.__detail.resizable(width=False, height=False)
        self.__bgcolor = "#242424"
        self.__txtcolor = "white"
        
        Label(text="CAR PLATE : "+self.__plate, font=self.__title_font).pack()
        
        r = requests.get(f'http://127.0.0.1:8000/find Car?plate={self.__plate}')
        car=json.loads(r.text)
        Label(text="Car Brand: "+car["_Car__car_brand"], font=self.__normal_font ).place(x=10,y=60)
        Label(text="Car Model: "+car["_Car__car_model"], font=self.__normal_font ).place(x=10,y=100)
        Label(text="Car Type: "+car["_Car__fuel_type"], font=self.__normal_font ).place(x=10,y=140)
        Label(text="Car Insurance: "+car["_Car__car_insurance"], font=self.__normal_font ).place(x=10,y=180)
        Label(text="Car Seat: "+car["_Car__car_seat"], font=self.__normal_font ).place(x=10,y=220)
        Label(text="Car Amount: "+str(car["_Car__car_amount"])+" per Day", font=self.__normal_font ).place(x=10,y=260)
        Label(text="Car Rating: "+str(car["_Car__rating_score"]), font=self.__normal_font ).place(x=10,y=300)
        
        Button(text='Add Favourite', font=self.__normal_font,command=self.add_favorite,
                   fg='#000000', bg="#40e0d0", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor).place(x=10,y=340)
        Button(text='Add Rating', font=self.__normal_font,command=self.add_rating,
                   fg='#000000', bg="#40e0d0", activebackground=self.__bgcolor,
                   activeforeground=self.__txtcolor).place(x=170,y=340)
        


        self.__detail.mainloop()
        
    def add_rating(self):
        self.__detail.destroy()
        AddRating(self.__plate,self.__token)
        
        
    def add_favorite(self):
        data = {
            "car_plate": str(self.__plate)
        }
        r = requests.post('http://127.0.0.1:8000/add_favourite',json=data,headers={'Authorization': "Bearer "+self.__token})
        if json.loads(r.text)["status"] == "Success":
            tkinter.messagebox.showinfo(title="Success", message="Add Success!!!!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Add Fail!!!")
        
class AddRating:
    def __init__(self,plate,token):
        self.__add_rating = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        self.__token = token
        self.__plate = plate
        values=['1', '2', '3', '4', '5']
        #font 
        self.__add_rating.title("Add_rating")
        self.__add_rating.geometry("400x250")
        self.__add_rating.resizable(width=False, height=False)

        Label(text="Add Rating", font=self.__title_font).pack(anchor="center")
        Label(text="Rating:", font=self.__normal_font).place(x=20, y=50)
        
        self.value_inside = tkinter.StringVar(self.__add_rating)
        self.value_inside.set("Select an Option")
        self.rating_entry = tkinter.OptionMenu(self.__add_rating, self.value_inside,*values)
        self.rating_entry.place(x=150, y=50)
        
        Label(text="Comment:", font=self.__normal_font).place(x=20, y=100)
        self.comment_entry = Entry(self.__add_rating, font=self.__text_font)
        self.comment_entry.place(x=150, y=100)
        
        Button(text="Confirm Edit", font=self.__normal_font, command=self.add_rating).place(x=100, y=185)
        Button(text="Back", font=self.__normal_font, command=self.back).place(x=300, y=185)
        self.__add_rating.mainloop()
        
    def back(self):
        self.__add_rating.destroy()
        Detail(self.__plate,self.__token)
        
    def add_rating(self):
        print(self.value_inside.get())
        if self.value_inside.get() == "":
            tkinter.messagebox.showerror(message="Please enter score", title="Error")
        
        else:data = {
                    "score": int(self.value_inside.get()),
                    "comment": str(self.comment_entry.get()),
                    "car_plate": str(self.__plate)
                }
        r = requests.post('http://127.0.0.1:8000/add_rating',json = data,headers={'Authorization': "Bearer "+self.__token})
        if json.loads(r.text)["status"] == "Add Success":
            tkinter.messagebox.showinfo(title="Success", message="Add Success!!!!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Add Fail!!!")

        
        
                
            
        
        
        
        
        
        