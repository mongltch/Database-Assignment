import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
from tkinter import *

def bankAccountWin():
    def enter_data():

        driverNo = bank_driverNO_entry.get()
        salary = salary_entry.get()
        bankName = bank_entry.get()
        accountNO = bank_accountNO_entry.get()
        sortCode = bank_sortNO_entry.get()

        if driverNo and salary and bankName and accountNO and sortCode:

            conn = sqlite3.connect('SpeedyTravelDatabase.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Bank_Account
            (BankACC_ID INTEGER, Driver_Number, Salary NUMERIC, Bank TEXT, Account_No INTEGER, Sort_Code TEXT,
            PRIMARY KEY(BankACC_ID AUTOINCREMENT), FOREIGN KEY(Driver_Number) REFERENCES Driver(Driver_No))                                           
            '''
            conn.execute(table_create_query)

            #insert data

            data_insert_query = '''INSERT INTO Bank_Account (Driver_Number, Salary, Bank, Account_No, Sort_Code) VALUES (?, ?, ?, ?, ?)'''
            data_insert_tuple = (driverNo, salary, bankName, accountNO, sortCode)
            
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            


            #close connection
            conn.close()











            print('works')
        else:
            tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')


    window = tkinter.Tk()

    window.title('Bank Account Form')
    frame = tkinter.Frame(window)
    frame.pack()


    bank_account_frame1 = tkinter.LabelFrame(frame, text= 'Bank Account')
    bank_account_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


    bank_driverNo_label = tkinter.Label(bank_account_frame1, text= 'Driver Number')
    bank_driverNo_label.grid(row= 0, column= 0)
    bank_driverNO_entry = tkinter.Entry(bank_account_frame1)
    bank_driverNO_entry.grid(row=1, column=0)

    salary_label = tkinter.Label(bank_account_frame1, text= 'Salary')
    salary_label.grid(row= 0, column= 1)
    salary_entry = tkinter.Entry(bank_account_frame1)
    salary_entry.grid(row=1, column=1)

    bank_label = tkinter.Label(bank_account_frame1, text= 'Bank')
    bank_label.grid(row= 2, column= 0)
    bank_entry = tkinter.Entry(bank_account_frame1)
    bank_entry.grid(row=3, column=0)

    bank_accountNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Account Number')
    bank_accountNO_label.grid(row= 2, column= 1)
    bank_accountNO_entry = tkinter.Entry(bank_account_frame1)
    bank_accountNO_entry.grid(row=3, column=1)

    bank_sortNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Sort Code')
    bank_sortNO_label.grid(row= 4, column= 0)
    bank_sortNO_entry = tkinter.Entry(bank_account_frame1)
    bank_sortNO_entry.grid(row=5, column=0)


    for widget in bank_account_frame1.winfo_children():
        widget.grid_configure(padx=10, pady= 5)


    button = tkinter.Button(bank_account_frame1, text='Submit', command= enter_data)
    button.grid(row= 6, column=1, sticky='news' , padx=10, pady=10)


    #show data function

    def showData():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM Bank_Account")
        records = cursor.fetchall()
        print(records)

        print_records = ''
        for record in records:
            print_records +=  str(record[0]) + '\t' + 'Driver No: ' + str(record[1]) + '\t' + 'Salary: £' + str(record[2]) + '\t ' + 'Acc No: ' + str(record[4]) + ' \t ' + 'Sort Code: ' +str(record[5]) +'\n' + '\n' 

        query_label = Label(frame, text = print_records)
        query_label.grid(row= 2, column = 0)


        


        conn.commit()  
        conn.close()

    #show data button
    show_data_button = tkinter.Button(bank_account_frame1, text='Show Data', command= showData)
    show_data_button.grid(row= 6, column=0, sticky='news' , padx=10, pady=10)


    #delete and edit frame
    bank_account_frame2 = tkinter.LabelFrame(frame, text= 'Edit Data')
    bank_account_frame2.grid(row= 1 , column= 0, padx=20, pady=20)

    ##delete button + entry + function
    def delete():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from Bank_Account WHERE oid= ' + delete_entry.get()) 

        

        
        conn.commit()  
        conn.close()

    delete_btn = Button(bank_account_frame2, text= 'Delete Record', command= delete)
    delete_btn.grid(row = 1, column= 1, pady= 10, padx= 10, sticky='news' , )

    delete_label= Label(bank_account_frame2, text= 'Enter Bank ID' )
    delete_label.grid(row= 0, column= 0)
    delete_entry = Entry(bank_account_frame2, width=30)
    delete_entry.grid(row= 0, column= 1, pady= 5, padx= 10)


    #edit record button + function


    def update():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        record_id = delete_entry.get()

        cursor.execute("""UPDATE Bank_Account SET 
                    
                    
                Driver_Number = :driverNo, 
                Salary = :salary, 
                Bank = :bank, 
                Account_No = :accNo,
                Sort_Code = :sortCode
                
                WHERE oid = :oid """,

    #create dictionary to give values to ^ (the keys and we match them to the entries)


                { 'driverNo': bank_driverNO_entry_edit.get(),
                    'salary': salary_entry_edit.get(),
                    'bank': bank_entry_edit.get(),
                    'accNo': bank_accountNO_entry_edit.get(),
                    'sortCode': bank_sortNO_entry_edit.get(),

                    'oid': record_id

                })

        conn.commit()  
        conn.close()

        editor.destroy()

    def edit():
        global editor
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()
        #store the value user has input into variable so that we can find it

        record_id = delete_entry.get()
        cursor.execute("SELECT * FROM Bank_Account WHERE oid =" + record_id)
        records = cursor.fetchall()
        print(records)
        
    

        editor = Tk()
        editor.title('Edit Record')
        editor.geometry('400x600')


        #create global variables to access in dictionary 
        global bank_driverNO_entry_edit
        global salary_entry_edit
        global bank_entry_edit
        global bank_accountNO_entry_edit
        global bank_sortNO_entry_edit

        bank_account_frame1 = tkinter.LabelFrame(editor, text= 'Bank Account')
        bank_account_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


        bank_driverNo_label = tkinter.Label(bank_account_frame1, text= 'Driver Number')
        bank_driverNo_label.grid(row= 0, column= 0)
        bank_driverNO_entry_edit = tkinter.Entry(bank_account_frame1)
        bank_driverNO_entry_edit.grid(row=1, column=0)

        salary_label = tkinter.Label(bank_account_frame1, text= 'Salary')
        salary_label.grid(row= 0, column= 1)
        salary_entry_edit = tkinter.Entry(bank_account_frame1)
        salary_entry_edit.grid(row=1, column=1)

        bank_label = tkinter.Label(bank_account_frame1, text= 'Bank')
        bank_label.grid(row= 2, column= 0)
        bank_entry_edit = tkinter.Entry(bank_account_frame1)
        bank_entry_edit.grid(row=3, column=0)

        bank_accountNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Account Number')
        bank_accountNO_label.grid(row= 2, column= 1)
        bank_accountNO_entry_edit = tkinter.Entry(bank_account_frame1)
        bank_accountNO_entry_edit.grid(row=3, column=1)

        bank_sortNO_label = tkinter.Label(bank_account_frame1, text= 'Bank Sort Code')
        bank_sortNO_label.grid(row= 4, column= 0)
        bank_sortNO_entry_edit = tkinter.Entry(bank_account_frame1)
        bank_sortNO_entry_edit.grid(row=5, column=0)


        for widget in bank_account_frame1.winfo_children():
            widget.grid_configure(padx=10, pady= 5)


        for record in records:
            bank_driverNO_entry_edit.insert(0, record[1])
            salary_entry_edit.insert(0, record[2])
            bank_entry_edit.insert(0, record[3])
            bank_accountNO_entry_edit.insert(0, record[4])
            bank_sortNO_entry_edit.insert(0, record[5])


        editor_submit = Button(bank_account_frame1, text='Submit Changes' , command= update)
        editor_submit.grid(row= 5, column= 1, pady= 5, padx= 5, sticky= 'news')

        conn.commit()  
        conn.close()

    delete_btn = Button(bank_account_frame2, text= 'Edit Record', command= edit)
    delete_btn.grid(row = 2, column= 1, pady= 5, padx= 10, sticky='news')




    window.mainloop()


