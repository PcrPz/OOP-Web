from tkinter import *
from tkinter.font import *

class RegisterGUI:
    def __init__(self):
        self.__register = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12)
        #setting 
        self.__register.title("Register")
        self.__register.geometry("600x600")
        self.__register.resizable(width=False, height=False)
        #interface
        Label(text="Register", font=self.__title_font).pack()
        self.__register.mainloop()
        
        

RegisterGUI()
    