from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please fill all the details")
    else:

        confirmation = messagebox.askokcancel(title="Details",
                                              message=f"The details entered are:\n Email:{email}\n password:{password}\n")
        if confirmation:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                web_entry.delete(0, END)
                pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=45, pady=45)
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
web_label = Label(text="Website")
web_label.grid(column=0, row=1)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
pw_label = Label(text="password")
pw_label.grid(column=0, row=3)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)
generate_pw = Button(text="Generate password", command=generate_password)
generate_pw.grid(column=2, row=3)
add_pw = Button(text="Add", command=save)
add_pw.grid(column=1, row=4, columnspan=2)

window.mainloop()
