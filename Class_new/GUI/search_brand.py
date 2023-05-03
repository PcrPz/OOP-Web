import requests
from pathlib import Path
import json

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
class Searchbymake:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\watsa\OneDrive\Desktop\assignment\year 1 term 2\oop pre\OOP-Web\Class_new\GUI\build\assets\frame0")
        window = Tk()
        window.geometry("720x420")
        window.configure(bg = "#EBEBEB")


        self.canvas = Canvas(
            window,
            bg = "#EBEBEB",
            height = 420,
            width = 720,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            360.0,
            114.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            144.0,
            210.0,
            573.0,
            238.0,
            fill="#FAC87D",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            436.5,
            328.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=250.0,
            y=304.0,
            width=373.0,
            height=46.0
        )

        self.canvas.create_rectangle(
            75.0,
            304.0,
            646.0,
            352.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            237.0,
            311.0,
            238.0,
            342.0,
            fill="#8C8888",
            outline="")

        self.canvas.create_text(
            123.0,
            323.0,
            anchor="nw",
            text="search by make",
            fill="#000000",
            font=("JosefinSlabRoman Regular", 11 * -1)
        )

        self.canvas.create_text(
            157.0,
            210.0,
            anchor="nw",
            text="FIND YOUR DRIVE",
            fill="#000000",
            font=("JacquesFrancois Regular", 47 * -1)
    )
        Button(window,text="Search",bd = 5 ,command = self.searchcar).place(x = 320, y= 360)
        window.resizable(width = False , height = False)
        window.mainloop()
        
    def searchcar(self):
        url = 'http://127.0.0.1:8000/search/search_car_by_brand?name={payload}'
        payload ={"":self.entry_1.get()}
        r = requests.get(url,json=payload)
        response = json.loads(r.text)
        print(response)
    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)    

Searchbymake()