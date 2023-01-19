from tkinter import *
import pandas
import random



BACKGROUND_COLOR = "#B1DDC6"

french_words = pandas.read_csv("data/french_words.csv")

window = Tk()
window.title("Flashcard")
window.config(bg = BACKGROUND_COLOR, padx=50,pady=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(height = 550, width = 795,highlightthickness=0,bg= BACKGROUND_COLOR)
fre_card = canvas.create_image(400,263,image=card_back)
canvas.grid(row=1,column=1)
Language = canvas.create_text(400,150, text= "Title", font=("Ariel",40))
word = canvas.create_text(400,263, text= "The Word", font=("Ariel",40))
#eng_card= canvas.create_image(image=card_front)

def fr():
    word.config(text= french_words.loc[random.randint])


right_button = Button(image=right)
right_button.grid(row = 2, column= 0)

wrong_button = Button(image=wrong)
wrong_button.grid(row= 2, column= 2)




window.mainloop()






