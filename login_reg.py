# module import
# module imports

from tkinter import *
import os
from tkinter import messagebox
from management_sys import login_page
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("310x230")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below", bg="orange", font=("Times", "15", "bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username  ", font=("Times", "12", "bold"))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, font=("Times", "12", "bold"))
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ", font=("Times", "12", "bold"))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, font=("Times", "12", "bold"))
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, font=("Times", "12", "bold"),
           command=register_user).pack()

    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("310x230")
        Label(login_screen, text="Enter the details  to login", font=("Times", "15", "bold italic")).pack()
        Label(login_screen, text="").pack()
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()
        global username_login_entry
        global password_login_entry
        Label(login_screen, text="Username  ", font=("Times", "12", "bold")).pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify, font=("Times", "12", "bold"))
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password  ", font=("Times", "12", "bold")).pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, font=("Times", "12", "bold"))
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, font=("Times", "12", "bold"),
               command=login_verify).pack()
