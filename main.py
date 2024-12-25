from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("words_to_learn.csv")
    to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv("Hindi_words.csv")
    to_learn = data.to_dict(orient='records')
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text='Hindi',fill='black')
    canvas.itemconfig(card_word,text=current_card['Hindi'],fill='black')
    canvas.itemconfig(card_image,image=old_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():

    canvas.itemconfig(card_image, image=new_img)
    canvas.itemconfig(card_title, fill='white')
    canvas.itemconfig(card_word, fill='white')
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card['English'])

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()


#------------------------------UI SETUP----------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
BLACK = '#001C30'

window = Tk()
window.title("Hindi Flash Card Project")
window.config(bg=BACKGROUND_COLOR,padx=20,pady=20)

flip_timer = window.after(3000,flip_card)

#canvas
canvas = Canvas(width=400,height=262)
old_img = PhotoImage(file="./images/card_front (1).png")
new_img = PhotoImage(file="./images/card_back (1).png")
card_image = canvas.create_image(200,131,image=old_img)
card_title = canvas.create_text(200,50,text='',fill=BLACK,font=('Arial',20,'normal'))
card_word = canvas.create_text(200,131,text='',fill=BLACK,font=('Arial',30,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)



#Button
right_image = PhotoImage(file="./images/right (1).png")
right = Button(image=right_image,highlightthickness=0,command=is_known)
right.grid(column=0,row=1)

wrong_image = PhotoImage(file="./images/wrong (1).png")
wrong = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong.grid(column=1,row=1)


next_card()







window.mainloop()