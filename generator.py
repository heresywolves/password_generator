from secrets import choice
import string
import random
from tkinter import *


def generate(mode='letters', lenght=8):
    global password

    # Possible character list
    character_list = []
    new_password = ""

    # Getting character set for password
    while True:
        if mode == 'digits':
            character_list += string.ascii_letters
            character_list += string.digits
            break

        elif mode == 'letters':
            character_list += string.ascii_letters
            break

        elif mode == 'special':
            character_list += string.ascii_letters
            character_list += string.digits
            character_list += string.punctuation
            break

    for i in range(int(lenght)):

        # Picking a random character and adding to password
        randomchar = random.choice(character_list)
        new_password += randomchar

    # Showing the password
    password.set('')
    password.set(new_password)


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
    digits_button = Button(gui, bg='gray', text='Digits', activebackground="green", anchor='center',
                           borderwidth=0, highlightthickness=0, command=lambda: generate('digits', 5))
    digits_button.grid(row=1, column=0, pady=10)

    letters_button = Button(gui, bg='gray', text='Letters', activebackground="green", anchor='center',
                            borderwidth=0, highlightthickness=0, command=lambda: generate('letters', 5))
    letters_button.grid(row=2, column=0, pady=10)

    special_button = Button(gui, bg='gray', text='Special characters', activebackground="green", anchor='center',
                            borderwidth=0, highlightthickness=0, command=lambda: generate('special', 5))
    special_button.grid(row=3, column=0, pady=10)

    # Getting the lenght of the password
    text = Label(gui, text='Enter the length of the password',
                 font=('calibre', 10, 'bold'), background='black', fg='white')
    text.grid(row=1, column=2)

    entry = Entry(gui, bg='#191818', fg='green',
                  borderwidth=1, highlightthickness=1)
    entry.grid(row=2, column=2, ipadx=10)

    # Execute tkinter
    gui.mainloop()
