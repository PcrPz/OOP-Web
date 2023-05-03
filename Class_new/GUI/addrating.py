from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json
from functools import partial
from Gui_detailcar import Detail

class AddRating:
    def init(self,plate,token):
        self.add_rating = Tk()
        #font
        self.title_font = Font(family="Kanit", weight="bold", size=20)
        self.normal_font = Font(family="Kanit", weight="normal", size=16)
        self.text_font = Font(family="Kanit", weight="normal", size=12)
        self.token = token
        self.plate = plate
        #font 
        self.add_rating.title("Add_rating")
        self.add_rating.geometry("400x250")
        self.add_rating.resizable(width=False, height=False)

        Label(text="Add Rating", font=self.title_font).pack(anchor="center")
        Label(text="Rating:", font=self.normal_font).place(x=20, y=50)
        self.rating_entry = Entry(self.add_rating, font=self.text_font)
        self.rating_entry.place(x=150, y=50)
        
        Label(text="Comment:", font=self.normal_font).place(x=20, y=100)
        self.comment_entry = Entry(self.add_rating, font=self.text_font)
        self.comment_entry.place(x=150, y=100)
        Button(text="Confirm Edit", font=self.normal_font, command=self.add_rating).place(x=100, y=185)
        Button(text="Back", font=self.normal_font, command=self.back).place(x=300, y=185)
        self.add_rating.mainloop()

    def back(self):
        self.add_rating.destroy()
        Detail(self.plate,self.token)

    def add_rating(self):
        data = {
                    "score": int(self.rating_entry.get()),
                    "comment": str(self.comment_entry.get()),
                    "car_plate": str(self.plate)
                }
        r = requests.post('http://127.0.0.1:8000/add_rating',json = data,headers={'Authorization': "Bearer "+self.token})
        if json.loads(r.text)["status"] == "Add Success":
            tkinter.messagebox.showinfo(title="Success", message="Add Success!!!!")
        else:
            tkinter.messagebox.showerror(title="Error", message="Add Fail!!!")