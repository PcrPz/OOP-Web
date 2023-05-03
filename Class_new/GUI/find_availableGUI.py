from tkinter import *
from tkinter.font import *
from tkcalendar import DateEntry
from datetime import *
import requests
import json

class GetAvailableCarGUI:
    def __init__(self,token):

        self.__find_available_car = Tk()

        self.token = token
        r = requests.get('http://127.0.0.1:8000/users/me',headers={'Authorization': "Bearer "+self.token})
        self.user = json.loads(r.text)
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__find_available_car.title("Find Available Car")
        self.__find_available_car.geometry("800x800")
        self.__find_available_car.resizable(width=False, height=False)

        #set variable
        self.__start_date = StringVar()
        self.__start_time = StringVar()
        self.__end_date = StringVar()
        self.__end_time = StringVar()
        
        #start_date
        self.__cal1 = DateEntry(self.__find_available_car,selectmode='day')
        sd = self.__cal1.get_date()
        self.__start_date = sd.strftime("%d-%m-%y")

        self.__cal1.grid(row=1, column = 1, padx = 15)
        #start_time
        Label(text="start time:", font=self.__normal_font).place(x=25, y=110)
        self.__start_time = Entry(self.__find_available_car, font=self.__txtbox_font)
        self.__start_time.place(x=130, y=110)
        #end_date
        self.__cal3 = DateEntry(self.__find_available_car,selectmode='day')
        ed = self.__cal3.get_date()
        self.__end_date = ed.strftime("%d-%m-%y")
        self.__cal3.grid(row=1, column = 2, padx = 15)
        #end_time
        Label(text="end time:", font=self.__normal_font).place(x=25, y=140)
        self.__end_time = Entry(self.__find_available_car, font=self.__txtbox_font)
        self.__end_time.place(x=130, y=140)

        print(type(self.__start_date))
        Button(text="Confirm", font=self.__normal_font, command = self.search_available_car).place(x=15, y=30)
        self.__find_available_car.mainloop()   

    def search_available_car(self):
        url = "http://127.0.0.1:8000/get_available_car"
        data = {
                    "start_date": str(self.__start_date),
                    "start_time": str(self.__start_time.get()),
                    "end_date": str(self.__end_date),
                    "end_time": str(self.__end_time.get())
                }
        r = requests.post(url, json = data, headers={'Authorization': "Bearer "+self.token})
        print(data)
        #print(json.loads(r.text))

GetAvailableCarGUI("petch")