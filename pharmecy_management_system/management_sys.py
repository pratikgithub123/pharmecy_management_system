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
        Refno_entry.delete(0, END)
        Company_entry.delete(0, END)
        MedType_combo.delete(0, END)
        Medname_entry.delete(0, END)
        Lot_entry.delete(0, END)
        Issue_entry.delete(0, END)
        Expiry_entry.delete(0, END)
        Dosage_entry.delete(0, END)
        Tablets_entry.delete(0, END)
        Precs_entry.delete(0, END)
        Uses_entry.delete(0, END)
        Sideeffects_entry.delete(0, END)
        messagebox.showinfo("Medicine added", "MEDICINE ADDED SUCCESSFULLY")

    def query():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book1.db')
        # Create cursor
        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print("After show button", records)
        # Loop through the results
        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(
                record[7]) + ' ' + str(record[8]) + ' ' + str(record[9]) + ' ' + str(record[10]) + ' ' + str(
                record[11]) + ' ' + str(record[12]) + "\n"
        print("showing data", print_record)
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0, y=0)
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
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(
                record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + ' ' + str(record[7]) + ' ' + str(
                record[8]) + ' ' + str(record[9]) + ' ' + str(record[10]) + ' ' + str(record[11]) + ' ' + str(
                record[12]) + "\n"
        query_label = Label(details_frame, text=print_record)
        query_label.place(x=0, y=0)
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
            # Creating global variable for all text boxes
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