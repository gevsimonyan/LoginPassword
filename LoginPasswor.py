from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Sign in")

def registration():
    txt = Label(text = "register to login")
    txt_log = Label(text = "Enter login")
    reg_login = Entry()
    txt_password1 = Label(text="Enter password")
    reg_password1 = Entry(show = "*")
    txt_password2 = Label(text = "Enter password again")
    reg_password2 = Entry(show= "*")

    button_reg = Button(text = "Registr", command = lambda: save())

    txt.pack()
    txt_log.pack()
    reg_login.pack()
    txt_password1.pack()
    reg_password1.pack()
    txt_password2.pack()
    reg_password2.pack()
    button_reg.pack()

    def save():
        login_pass_save = {}
        login_pass_save[reg_login.get()] = reg_password1.get()
        func = open("login.txt", "wb")
        pickle.dump(login_pass_save, func)
        func.close()
        login()



def login():
    txt_log = Label(text = "You can log in")
    txt_enter_log = Label(text = "Enter login")
    enter_log = Entry()
    txt_enter_password = Label(text = "Enter password")
    enter_password = Entry(show = "*")
    button_enter = Button(text = "Sign in", command = lambda: log_chek())
    txt_log.pack()
    txt_enter_log.pack()
    enter_log.pack()
    txt_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def log_chek():
        func = open("login.txt", "rb")
        temp = pickle.load(func)
        func.close()
        if enter_log.get() in temp:
            if enter_password.get() == temp[enter_log.get()]:
                messagebox.showinfo("logged in" + " "+ "Hi dude")
            else:
                messagebox.showerror("Error" + " " + "Wrong login or password")
        else:
            messagebox.showerror("Error" + " " + "Wrong login or password")

registration()
#login()

root.mainloop()