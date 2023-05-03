from tkinter import *
from tkinter.font import *
import tkinter.messagebox
import customtkinter as ctk
import requests
import json
from functools import partial
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
        pass
        # self.__watch_his.destroy()
        # CarCatalogTK(self.__token)
          
        
    def show_car(self):
        r = requests.get('http://127.0.0.1:8000/watch_history',headers={'Authorization': "Bearer "+self.__token})
        res = json.loads(r.text)
        # self.__car_count = len(res)
        # for car in res:
        #     self.__list_car_to_show.append(car)