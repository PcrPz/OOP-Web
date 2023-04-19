from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import requests
import json


class CarCatalogTK:
    
    def __init__(self,token):
        self.__car_catalog = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12) 
        # self.token = token
        # r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
        # self.user = json.loads(r.text)
        # print(self.user["_contact_name"])
        
        #setting 
        self.__car_catalog.title("CarCatalog")
        self.__car_catalog.geometry("1000x800")
        self.__car_catalog.resizable(width=False, height=False)
        
        #value
        self.__token = token
        self.__car_count = 0
        self.__list_car_to_show =[]
        self.__row_base = 1
        
        #interface
        Label(text="CarCatalog", font=self.__title_font).pack()
        self.show_course()
        for i in range(0,self.__car_catalog,3):
            if self.__car_catalog % 3 == 0:
                for j in range(3):
                    Label(text=self.__list_car_to_show[i+j]['_Courses__refcode'], font=self.__normal_font).grid(row=self.__row_base, column=j)
                    Label(text=self.__list_car_to_show[i+j]['_Courses__title'], font=self.__normal_font).grid(row=self.__row_base+1, column=j)
            self.__row_base +=2
        
        
        
        self.__car_catalog.mainloop()
        
        
        
    def show_course(self):
        res = requests.get('http://127.0.0.1:8000/cars')
        all_cata = json.loads(res.text)
        self.__car_count = len(all_cata)
        for i in all_cata:
            self.__list_car_to_show(i)
        print("")
        
#ตัวนี้ไว้รันใช้ของ
            r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
            self.user = json.loads(r.text)
            print(self.user["_contact_name"])
    