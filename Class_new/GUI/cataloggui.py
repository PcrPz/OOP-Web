from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json

class Login:
    
    def __init__(self):
        self.__login = Tk()
        self.__header_font = Font(family = "kanit" , weight = "bold",size=20)
        self.__normal_font
        
#ตัวนี้ไว้รันใช้ของ
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
        self.user = json.loads(r.text)
        print(self.user["_contact_name"])
    