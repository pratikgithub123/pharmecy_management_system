from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
def login_page():
    #Databases
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book1.db')
    # Create cursor
    c = conn.cursor()
    # Create table
    '''
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
    '''
    # Create submit button for databases
    def submit():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # Insert into table
        c.execute("INSERT INTO addresses VALUES (:ref_no, :company_name, :med_name, :med_type, :lot_no, :issue_date, :expiry_date, :dosage, :tab_price, :precs_warning, :uses, :side_effects)",{
            'ref_no':Refno_entry.get(),
            'company_name':Company_entry.get(),
            'med_type':MedType_combo.get(),
            'med_name':Medname_entry.get(),
            'lot_no':Lot_entry.get(),
            'issue_date':Issue_entry.get(),
            'expiry_date':Expiry_entry.get(),
            'dosage':Dosage_entry.get(),
            'tab_price':Tablets_entry.get(),
            'precs_warning':Precs_entry.get(),
            'uses':Uses_entry.get(),
            'side_effects':Sideeffects_entry.get()
        })
        conn.commit()
        conn.close()
