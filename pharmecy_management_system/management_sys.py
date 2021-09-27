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
    Label(register_screen, text="Please enter details below", bg="orange",font=("Times", "15", "bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username  ",font=("Times", "12", "bold"))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,font=("Times", "12", "bold"))
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ",font=("Times", "12", "bold"))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password,font=("Times", "12", "bold"))
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1 ,font=("Times", "12", "bold"), command=register_user).pack()
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("310x230")
    Label(login_screen, text="Enter the details  to login",font=("Times", "15", "bold italic")).pack()
    Label(login_screen, text="").pack()
    global username_verify
 4  management_sys.py
@@ -1,328 +1,328 @@
#imports
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
        # clear the text boxes
        Refno_entry.delete(0,END)
        Company_entry.delete(0,END)
        MedType_combo.delete(0,END)
        Medname_entry.delete(0,END)
        Lot_entry.delete(0,END)
        Issue_entry.delete(0,END)
        Expiry_entry.delete(0,END)
        Dosage_entry.delete(0,END)
        Tablets_entry.delete(0,END)
        Precs_entry.delete(0,END)
        Uses_entry.delete(0,END)
        Sideeffects_entry.delete(0,END)
        messagebox.showinfo("Medicine added", "MEDICINE ADDED SUCCESSFULLY")
    def query():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print("After show button",records)
        # Loop through the results
        print_record=''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1])+' '+ str(record[2])+ ' ' + str(record[3]) + ' ' + str(record[4]) + ' ' +  str(record[5]) + ' ' +  str(record[6]) + ' ' +  str(record[7]) + ' ' +  str(record[8]) + ' ' +  str(record[9]) + ' ' +  str(record[10]) + ' ' +  str(record[11]) + ' ' +  str(record[12]) + "\n"
        print("showing data", print_record)
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0,y=0)
        conn.commit()
        conn.close()
    def delete():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # Delete a record
        c.execute("DELETE from addresses WHERE oid = " + txtsearch.get())
        print("deleted sucessfully")
        # query of databases
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print(records)
        # Loop through the results
        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) + ' ' + str(
                record[8]) + ' ' + str(record[9]) + ' ' + str(record[10]) + ' ' + str(record[11]) + ' ' + str(
                record[12])  + "\n"
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0,y=0)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted successfully", "Data Deleted sucessfully")
    def edit():
        global editor
        editor = Tk()
        editor.title('Update Data')
        editor.geometry('600x600')
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        record_id = txtsearch.get()
        # query of the database
        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
        records = c.fetchall()
        #Creating global variable for all text boxes
        global ref_no_editor
        global Company_editor
        global med_type_editor
        global med_name_editor
        global lot_no_editor
        global issue_editor
        global dosage_editor
        global tab_price_editor
        global precs_editor
        global uses_editor
        global side_effects_editor
        # Creating an update function
        def update():
            # Create a databases or connect to one
            conn = sqlite3.connect('address_book1.db')
            # Create cursor
            c = conn.cursor()
            record_id = txtsearch.get()
            c.execute(""" UPDATE addresses SET
                 ref_no = :ref,
                 company_name = :company,
                 med_type = :med_t,
                 med_name = :med_n,
                 lot_no = :lot,
                 issue_date = :issue,
                 expiry_date = :expiry,
                 dosage = :dos,
                 tab_price = :tab_p,
                 precs_warning = :precs,
                 uses = :use,
                 side_effects = :side
                 WHERE oid = :oid""",
                      {'ref': ref_no_editor.get(),
                       'company': Company_editor.get(),
                       'med_t': med_type_editor.get(),
                       'med_n': med_name_editor.get(),
                       'lot': lot_no_editor.get(),
                       'issue': issue_editor.get(),
                       'expiry': expiry_editor.get(),
                       'dos': dosage_editor.get(),
                       'tab_p': tab_price_editor.get(),
                       'precs': precs_editor.get(),
                       'use': uses_editor.get(),
                       'side': side_effects_editor.get(),
                       'oid': record_id
                       }
                      )
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated sucessfully","YOUR DATA HAVE BEEN SUCCESSFULLY UPDATED")
            # Destroying all the data and closing window
            editor.destroy()
       # Create text boxes
        ref_no_editor = Entry(editor, width=30)
        ref_no_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        Company_editor = Entry(editor, width=30)
        Company_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
        med_type_editor = Entry(editor, width=30)
        med_type_editor.grid(row=2, column=1, padx=20, pady=(10, 0))
        med_name_editor = Entry(editor, width=30)
        med_name_editor.grid(row=3, column=1, padx=20, pady=(10, 0))
        lot_no_editor = Entry(editor, width=30)
        lot_no_editor.grid(row=4, column=1, padx=20, pady=(10, 0))
        issue_editor = Entry(editor, width=30)
        issue_editor.grid(row=5, column=1, padx=20, pady=(10, 0))
        expiry_editor = Entry(editor, width=30)
        expiry_editor.grid(row=6, column=1, padx=20, pady=(10, 0))
        dosage_editor = Entry(editor, width=30)
        dosage_editor.grid(row=7, column=1, padx=20, pady=(10, 0))
        tab_price_editor = Entry(editor, width=30)
        tab_price_editor.grid(row=8, column=1, padx=20, pady=(10, 0))
        precs_editor = Entry(editor, width=30)
        precs_editor.grid(row=9, column=1, padx=20, pady=(10, 0))
        uses_editor = Entry(editor, width=30)
        uses_editor.grid(row=10, column=1, padx=20, pady=(10, 0))
        side_effects_editor = Entry(editor, width=30)
        side_effects_editor.grid(row=11, column=1, padx=20, pady=(10, 0))
        # Create textbox labels
        ref_no_label = Label(editor, text="Refrence no")
        ref_no_label.grid(row=0, column=0, pady=(10, 0))
        Company_label = Label(editor, text="Company/Customer Name")
        Company_label.grid(row=1, column=0)
        med_type_label = Label(editor, text="Medicine Type")
        med_type_label.grid(row=2, column=0)
        med_name_label = Label(editor, text="Medicine Type")
        med_name_label.grid(row=3, column=0)
        lot_no_label = Label(editor, text="Lot no.")
        lot_no_label.grid(row=4, column=0)
        issue_label = Label(editor, text="Issue Date.")
        issue_label.grid(row=5, column=0)
        expiry_label = Label(editor, text="Expiry Date")
        expiry_label.grid(row=6, column=0)
        dosage_label = Label(editor, text="Dosage")
        dosage_label.grid(row=7, column=0)
        tab_price_label = Label(editor, text="Tablets price")
        tab_price_label.grid(row=8, column=0)
        precs_label = Label(editor, text="Precs & Warning")
        precs_label.grid(row=9, column=0)
        uses_label = Label(editor, text=" Uses")
        uses_label.grid(row=10, column=0)
        side_effects_label = Label(editor, text=" Side Effects")
        side_effects_label.grid(row=11, column=0)
        # loop through the results
        for record in records:
            ref_no_editor.insert(0, record[0])
            Company_editor.insert(0, record[1])
            med_type_editor.insert(0, record[2])
            med_name_editor.insert(0, record[3])
            lot_no_editor.insert(0, record[4])
            issue_editor.insert(0, record[5])
            expiry_editor.insert(0, record[6])
            dosage_editor.insert(0, record[7])
            tab_price_editor.insert(0, record[8])
            precs_editor.insert(0, record[9])
            uses_editor.insert(0, record[10])
            side_effects_editor.insert(0, record[11])
        # Create a update button
        edit_btn = Button(editor, text=" SAVE ", command=update)
        edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=125)
    def exit_fun():
        ask = messagebox.askyesno("exit","Do you want to exit?")
        if ask == 1 :
            root.destroy()

