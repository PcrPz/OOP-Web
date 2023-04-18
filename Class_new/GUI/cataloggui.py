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
        self.token = token
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
        self.user = json.loads(r.text)
        print(self.user["_contact_name"])
        
        #setting 
        self.__car_catalog.title("CarCatalog")
        self.__car_catalog.geometry("800x800")
        self.__car_catalog.resizable(width=False, height=False)
        
        #value
        self.__token = token
        self.__car_count = 0
        self.__list_car_to_show =[]
        self.__row_base = 100
        #menu
        self.__main_menu = Menu()
        self.__hello = Menu()
        self.__hello.add_command(label="Edit_Profile")
        self.__hello.add_command(label="Watch_Favourite")
        self.__hello.add_command(label="Watch_History")
        self.__main_menu.add_cascade(label="Setting",menu=self.__hello)
        self.__car_catalog.config(menu=self.__main_menu)
        
        
        
        
        #interface
        Label(text="CarCatalog", font=self.__title_font).place(x=300 , y=50)
        self.show_course()
        
        if self.__car_count % 4 == 0:   
            for i in range(0,self.__car_count,4):
                for j in range(4):
                    Label(text=self.__list_car_to_show[i+j]['car_brand'], font=self.__normal_font).place(x=100+150*j,y=self.__row_base)
                    Label(text=self.__list_car_to_show[i+j]['car_model'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+30)
                    Label(text=self.__list_car_to_show[i+j]['car_amount'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+60)
                    Label(text=self.__list_car_to_show[i+j]['car_plate_number'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+90)
                self.__row_base +=120

        else: 
            num = self.__car_count%4
            for i in range(0,self.__car_count-4,4):
                for j in range(4):
                    Label(text=self.__list_car_to_show[i+j]['car_brand'], font=self.__normal_font).place(x=100+150*j,y=self.__row_base)
                    Label(text=self.__list_car_to_show[i+j]['car_model'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+30)
                    Label(text=self.__list_car_to_show[i+j]['car_amount'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+60)
                    Label(text=self.__list_car_to_show[i+j]['car_plate_number'], font=self.__normal_font).place(x=100+150*j, y=self.__row_base+90)
                self.__row_base +=120
            
            for k in range(num):
                    Label(text=self.__list_car_to_show[i+j+k+1]['car_brand'], font=self.__normal_font).place(x=100+150*k,y=self.__row_base)
                    Label(text=self.__list_car_to_show[i+j+k+1]['car_model'], font=self.__normal_font).place(x=100+150*k, y=self.__row_base+30)
                    Label(text=self.__list_car_to_show[i+j+k+1]['car_amount'], font=self.__normal_font).place(x=100+150*k, y=self.__row_base+60)
                    Label(text=self.__list_car_to_show[i+j+k+1]['car_plate_number'], font=self.__normal_font).place(x=100+150*k, y=self.__row_base+90)
            
            
        
        
        
        self.__car_catalog.mainloop()
        
        
        
    def show_course(self):
        res = requests.get('http://127.0.0.1:8000/cars')
        all_cata = json.loads(res.text)["catalog"]
        self.__car_count = len(all_cata)
        print(len(all_cata))
        for i in all_cata:
            self.__list_car_to_show.append(i)
        print("")
        


    
        

            