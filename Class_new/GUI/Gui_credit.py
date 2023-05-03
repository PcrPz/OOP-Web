from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial

class addcredGUI:
    def __init__(self,plate,token):

        self.__addcred = Tk()
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__addcred.title("addcred")
        self.__addcred.geometry("450x350")
        self.__addcred.resizable(width=False, height=False)
        
        #setting
        self.__token = token
        self.__plate = plate
        
        Label(text="Add Credit For Payment", font=self.__title_font).pack()
        Label(text="Card Number :", font=self.__normal_font).place(x=10, y=50)
        self.__num_entry = Entry(self.__addcred, font=self.__normal_font)
        self.__num_entry.place(x=140, y=50)
        
        Label(text="Expire Card :", font=self.__normal_font).place(x=10, y=100)
        self.__exp_entry = Entry(self.__addcred, font=self.__normal_font)
        self.__exp_entry.place(x=140, y=100)
        
        Label(text="Security Num :", font=self.__normal_font).place(x=10, y=150)
        self.__sc_entry = Entry(self.__addcred, font=self.__normal_font)
        self.__sc_entry.place(x=140, y=150)
        
        Button(text="Make Payment", font=self.__normal_font, command = self.make_payment).place(x=150, y=230)
        self.__addcred.mainloop()
        
        
    def make_payment(self):
        data = {
                    "card_number":  str(self.__num_entry.get()),
                    "exprie_card": str(self.__exp_entry.get()),
                    "security_number": str(self.__sc_entry.get())
                }
        r = requests.post('http://127.0.0.1:8000/Payment',json = data,headers={'Authorization': "Bearer "+self.__token})
        print(json.loads(r.text))
        if json.loads(r.text)["status"] == "Payment success":
            tkinter.messagebox.showinfo(title="Success", message="Payment Success!!!!")
            self.__addcred.destroy()
        else:
            tkinter.messagebox.showerror(title="Error", message="Payment Fail!!!")
        
        
