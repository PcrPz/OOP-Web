from tkinter import *
from tkinter.font import *
import json
import requests

class Add_credit:
    def __init__(self,token):
        self.ep = Tk()
        self.token=token
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
        self.user = json.loads(r.text)
        self.header_font = Font(family="Kanit", weight="bold", size=20)
        self.normal_font = Font(family="Kanit", weight="normal", size=16)
        self.txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.ep.title("Add_credit:")
        self.ep.geometry("400x400")
        self.ep.resizable(width=False, height=False)

        Label(text="Add credit card", font=self.header_font).pack(anchor="center")
        Label(text="expire_card:", font=self.normal_font).place(x=25, y=50)
        self.expire_card = Entry(self.ep, font=self.txtbox_font)
        self.expire_card.place(x=130, y=50)


        Label(text="card_number:", font=self.normal_font).place(x=25, y=150)
        self.card_number = Entry(self.ep, font=self.txtbox_font)
        self.card_number.place(x=130, y=150)


        Label(text="security_credit:", font=self.normal_font).place(x=25, y=250)
        self.security_credit = Entry(self.ep, font=self.txtbox_font)
        self.security_credit.place(x=130, y=250)

        Button(text="Confirm", font=self.normal_font, command = self.add_credit).place(x = 150 , y = 290)

        self.ep.mainloop()

    def add_credit(self):
        url = "http://127.0.0.1:8000/add_credit_info"
        data = {
                    "exprie_card": str(self.expire_card.get()),
                    "card_number": str(self.card_number.get()),
                    "security_credit": str(self.security_credit.get()),
                }
        r = requests.post(url, json = data,headers={'Authorization': "Bearer "+self.token})
        print(json.loads(r.text))

Add_credit("petch")
