from tkinter import *
from tkinter import messagebox
from pwd_gen import generate_password
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def autofill_password():
    password_input.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please fill out all fields")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"New password entry:\n\nTitle: {website}\nUser: {email}\nPassword: {password} ")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}")
                file.write("\n")

            pyperclip.copy(password)
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(message="Your password has been copied to your clipboard!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=240, width=240, padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

canvas.grid(column=1, row=0)

# Form

# Website
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Username
user_label = Label()
user_label.config(text="Email / Username:")
user_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "markestrada8@gmail.com")

# Password
password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(show="•")
password_input.config(width=20)
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=11, command=autofill_password)
password_button.grid(column=2, row=3)

# Submit
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
