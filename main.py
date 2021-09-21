from tkinter import *
from tkinter import messagebox
from passgen import password_gen
import pyperclip
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passw():
    our_password = password_gen()
    pyperclip.copy(our_password)
    password_name.delete(0,'end')
    password_name.insert('end',string=our_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_cred():
    if len(website_name.get()) == 0 or len(password_name.get()) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please do not leave the fields empty!"
        )
    else:
        save_pass()


def save_pass():
    website = website_name.get()
    email_address = email_add.get()
    password = password_name.get()

    new_data = {
        website:{
            'email':email_address,
            'password':password
        }
    }

    ask_user = messagebox.askyesno(
        title=website,
        message=f"Do you want to confirm the following details?\n"
                f"Email: {email_address}\npassword: {password}"
    )

    if ask_user == True:

        try:
            with open('data.json', mode='r') as file:

                data = json.load(file)
                data.update(new_data)

            with open('data.json',mode='w') as file:

                json.dump(data, file, indent=4)

        except FileNotFoundError:

            with open('data.json',mode='w') as file:
                json.dump(new_data, file)

        finally:
            website_name.delete(0, 'end')
            password_name.delete(0, 'end')
            website_name.focus()

# -------------------------PASSWORDSEARCH-------------------------------#


def search():
    try:
        website = website_name.get()
        with open('data.json','r') as file:
            data = json.load(file)
            email_addr = data[website]['email']
            passwrd = data[website]['password']
            messagebox.showinfo(
                title=website,
                message=f"Email Address: {email_addr}"
                        f"\nPassword: {passwrd}"
            )

    except FileNotFoundError:
        messagebox.showinfo(
            title='Oops!',
            message='No Data File Found')

    except KeyError:
        messagebox.showinfo(
            title='Oops!',
            message=f'No entry for {website_name.get()}')
    finally:
        website_name.focus()
        website_name.delete(0,'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('My Password Manager')
window.config(padx=30,pady=20, bg='white')

canvas = Canvas(width=200,height=190,bg='white',highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,95,image=logo_img)
canvas.grid(row=0,column=1)

website = Label(text="Website Name:",font=(FONT_NAME,10,'bold'),bg='white')
website.grid(row=1,column=0)


website_name = Entry(width= 40,highlightthickness=2)
website_name.focus()
website_name.grid(row=1,column=1)

email = Label(text="Email Address:",font=(FONT_NAME,10,'bold'),bg='white')
email.grid(row=2,column=0)

email_add = Entry(width= 59,highlightthickness=2)
email_add.insert('end',string='aavashdevil15@gmail.com')
email_add.grid(row=2,column=1,columnspan=2)

password = Label(text="Password:",font=(FONT_NAME,10,'bold'),bg='white')
password.grid(row=3,column=0)


password_name = Entry(width= 40,highlightthickness=2)
password_name.grid(row=3,column=1)

password_generator = Button(text="Generate Password",bg='white',command=passw)
password_generator.grid(row=3,column=2)


add_pass = Button(text='Add',width=50,bg='white',command=check_cred)
add_pass.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",bg='white',width=15,command=search)
search_button.grid(row=1,column=2)






window.mainloop()
