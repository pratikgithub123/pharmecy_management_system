from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import mes


    #Databases
    # Create a databases or connect to one
conn = sqlite3.connect('address_book1.db')

    # Create cursor
c = conn.cursor()


    # Create table

c.execute(""" CREATE TABLE addresses(
        ref_no integer,
        company_name text,
        med_type text,
        med_name text,
        lot_no integer,
        issue_date integer,
        expiry_date integer,
        dosage integer,
        tab_price integer,
        precs_warning text,
        uses text,
        side_effects text
) """)


    # Create submit button for databases
    def submit():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')

        # Create cursor
        c = conn.cursor()