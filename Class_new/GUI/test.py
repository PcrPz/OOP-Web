# from tkinter import *
# from tkinter.font import *
# import tkinter.messagebox
# from tkcalendar  
# import customtkinter as ctk
# import requests
# import json
# from functools import partial
# from Gui_dtforcaravalible import DetailCA

# class GetAvailableCarGUI:
    
    
#     def __init__(self,token):

#         self.__find_available_car = Tk()
#         self.__header_font = Font(family="Kanit", weight="bold", size=20)
#         self.__normal_font = Font(family="Kanit", weight="normal", size=16)
#         self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
#         self.__find_available_car.title("Find Available Car")
#         self.__find_available_car.geometry("800x800")
#         self.__find_available_car.resizable(width=False, height=False)
#         startdate = None
#         starttime = None
#         enddate = None
#         endtime = None
        
#         self.__token = token

      

#         #start_date
#         Label(text="Find Avalible", font=self.__header_font).pack()
#         Label(text="Start_date :", font=self.__normal_font).place(x=10, y=50)
#         self.__sd_entry = DateEntry(self.__find_available_car, width=25,background="blue", foreground="sky-blue", bd=4,date_pattern="dd-mm-yyyy")
#         self.__sd_entry.place(x=140, y=50)
        
#         Label(text="Start_time :", font=self.__normal_font).place(x=10, y=100)
#         self.__st_entry = Entry(self.__find_available_car, font=self.__normal_font)
#         self.__st_entry.place(x=140, y=100)
        
#         Label(text="End_date :", font=self.__normal_font).place(x=10, y=150)
#         self.__ed_entry = DateEntry(self.__find_available_car, width=25,background="blue", foreground="sky-blue", bd=4,date_pattern="dd-mm-yyyy")
#         self.__ed_entry.place(x=140, y=150)
        
#         Label(text="End_time :", font=self.__normal_font).place(x=10, y=200)
#         self.__et_entry = Entry(self.__find_available_car, font=self.__normal_font)
#         self.__et_entry.place(x=140, y=200)
        
#         Button(text="Confirm", font=self.__normal_font, command = self.find_avalible).place(x=100, y=250)
#         self.__sd_entry.get()
#         self.__st_entry.get()
#         self.__ed_entry.get()
#         self.__et_entry.get()
        
#         self.__find_available_car.mainloop()
        
#     def find_avalible(self):
#         #setting
#         self.__car_count = 0
#         self.__list_car_to_show =[]
#         self.__row_base = 350
#         self.__bgcolor = "#242424"
#         self.__txtcolor = "white"

#         url = 'http://127.0.0.1:8000/get_available_car'
#         data = {
#                     "start_date": self.__sd_entry.get(),
#                     "start_time": self.__st_entry.get(),
#                     "end_date": self.__ed_entry.get(),
#                     "end_time": self.__et_entry.get()
#                 }
#         r = requests.post(url, json = data)
#         all_cata =json.loads(r.text)
#         self.__car_count = len(all_cata)
#         print(len(all_cata))
#         for i in all_cata:
#             self.__list_car_to_show.append(i)
            
#         Label(text="CarAvalible", font=self.__header_font).place(x=300,y=300)    
#         if self.__car_count % 4 == 0:   
#             for i in range(0,self.__car_count,4):
#                 for j in range(4):
#                     Label(text='Brand :'+self.__list_car_to_show[i+j]['_Car__car_brand'], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
#                     Label(text='Model :'+self.__list_car_to_show[i+j]['_Car__car_model'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
#                     Label(text='Price :'+str(self.__list_car_to_show[i+j]["_Car__car_amount"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
#                     Label(text='Plate :'+self.__list_car_to_show[i+j]["_Car__car_plate_number"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+90)
#                     Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j]["car_plate_number"])),fg=self.__txtcolor, 
#                            bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*j, y=self.__row_base+125)
#                 self.__row_base +=185

#         else: 
#             num = self.__car_count%4
#             for i in range(0,self.__car_count-4,4):
#                 for j in range(4):
#                     Label(text='Brand :'+self.__list_car_to_show[i+j]['_Car__car_brand'], font=self.__normal_font).place(x=50+175*j,y=self.__row_base)
#                     Label(text='Model :'+self.__list_car_to_show[i+j]['_Car__car_model'], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+30)
#                     Label(text='Price :'+str(self.__list_car_to_show[i+j]["_Car__car_amount"]), font=self.__normal_font).place(x=50+175*j, y=self.__row_base+60)
#                     Label(text='Plate :'+self.__list_car_to_show[i+j]["_Car__car_plate_number"], font=self.__normal_font).place(x=50+175*j, y=self.__row_base+90)
#                     Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j]["_Car__car_plate_number"])),fg=self.__txtcolor, 
#                            bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*j, y=self.__row_base+125)
#                 self.__row_base +=185
#             for k in range(num):
#                     Label(text='Brand :'+self.__list_car_to_show[i+j+k+1]['_Car__car_brand'], font=self.__normal_font).place(x=50+175*k,y=self.__row_base)
#                     Label(text='Model :'+self.__list_car_to_show[i+j+k+1]['_Car__car_model'], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+30)
#                     Label(text='Price :'+str(self.__list_car_to_show[i+j+k+1]["_Car__car_amount"]), font=self.__normal_font).place(x=50+175*k, y=self.__row_base+60)
#                     Label(text='Plate :'+self.__list_car_to_show[i+j+k+1]["_Car__car_plate_number"], font=self.__normal_font).place(x=50+175*k, y=self.__row_base+90)
#                     Button(text='More Detail', font=self.__normal_font,command=partial(self.more_detail, str(self.__list_car_to_show[i+j+k+1]["_Car__car_plate_number"])),fg=self.__txtcolor, 
#                            bg="#1F6AA5", activebackground=self.__bgcolor,activeforeground=self.__txtcolor).place(x=50+176*k, y=self.__row_base+125)
    
#     def more_detail(self,plate):
#         self.__find_available_car.destroy()
#         DetailCA(plate,self.__token)
        
