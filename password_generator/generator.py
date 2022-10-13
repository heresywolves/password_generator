from secrets import choice
import string
import random
from tkinter import *


def generate(mode='letters'):
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

    # Get the length from the entry
    try:
        lenght = int(entry.get())
    except:
        password.set('Please enter the length of the password')

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
    gui.geometry('400x350')
    gui.configure(bg='black')
    gui.resizable(False, False)

    # Images and icons
    icon = PhotoImage(file='GUI\\logo.png')
    gui.iconphoto(True, icon)

    # Generation textfield
    password = StringVar()

    generation_field = Entry(gui, textvariable=password,
                             bg='#191818', borderwidth=1, highlightthickness=1, fg='light green', font=("Times New Roman", 12),
                             width=30)
    generation_field.grid(columnspan=1, ipadx=20, padx=60, pady=50)

    # Buttons
    letters_button = Button(gui, bg='gray', text='Only Letters', activebackground="green", anchor='center',
                            borderwidth=0, highlightthickness=0, command=lambda: generate('letters'))
    letters_button.grid(row=3, column=0, pady=10)

    digits_button = Button(gui, bg='gray', text='With Digits', activebackground="green", anchor='center',
                           borderwidth=0, highlightthickness=0, command=lambda: generate('digits'))
    digits_button.grid(row=4, column=0, pady=10)

    special_button = Button(gui, bg='gray', text='With Special Characters', activebackground="green", anchor='center',
                            borderwidth=0, highlightthickness=0, command=lambda: generate('special'))
    special_button.grid(row=5, column=0, pady=10)

    # Getting the lenght of the password
    text = Label(gui, text='Enter the length of the password',
                 font=('calibre', 10, 'bold'), background='black', fg='white')
    text.grid(row=1, column=0, pady=2)

    entry = Entry(gui, bg='#191818', fg='white',
                  borderwidth=1, highlightthickness=1, width=4)
    entry.grid(row=2, column=0, pady=10)

    # Execute tkinter
    gui.mainloop()
