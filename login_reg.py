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