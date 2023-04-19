from tkinter import *
from tkinter.font import *

class AddRating:
    def __init__(self,token):
        self.__add_rating = Tk()
        #font
        self.__title_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__text_font = Font(family="Kanit", weight="normal", size=12) 