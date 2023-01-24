from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self):
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 50, pady= 200, bg= THEME_COLOR)
        self.score = Label(self.window, text= "score:",font = ("Ariel",30), fg = "white",bg = THEME_COLOR)
        self.score.grid(row = 0, column = 1)
        self.canvas = Canvas(height = 500, width = 600,bg = "white")
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.canvas.create_image()
        self.window.mainloop()