from secrets import choice
import string
import random
from tkinter import *


def generate():
    pass


if __name__ == "__main__":

    # GUI initialization
    gui = Tk()
    gui.title('Password Generator')
    gui.geometry('600x400')
    gui.configure(bg='black')
    gui.resizable(False, False)

    # Generation textfield
    password = StringVar()

    generation_field = Entry(gui, textvariable=password,
                             bg='#191818', borderwidth=1, highlightthickness=1, fg='light green', font=("Times New Roman", 12),
                             width=50)
    generation_field.grid(columnspan=4, ipadx=20, padx=60, pady=100)

    # Buttons
    button1 = Button(gui, image=button1_image, bg='black', activebackground="black", anchor='center',
                     borderwidth=0, highlightthickness=0, command=lambda: press(1))
    button1.grid(row=3, column=0, rowspan=2)
    # Getting password length
    # length = int(input("Enter password lenght: "))

    characterList = ""

    # Getting character set for password
