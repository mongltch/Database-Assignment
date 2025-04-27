import tkinter
#collection of themed widgets allow creation of modern widgets need for combo box
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from tkinter import *
import sqlite3

def validateDate(date):
    if int(date[5:7]) > 12:
        return False
    elif int(date[8:10]) > 32:
        return False
    return True

#function that executes when data submitted


    
def openDrivers():

    def showData():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM Driver")
        records = cursor.fetchall()
        print(records)

        print_records = ''
        #loop through the records and turn them into a string + add new line
        for record in records:
            print_records += str(record[0]) + ' \t' + str(record[1]) + ' ' + str(record[2]) + '\n'

        query_label = Label(frame, text = print_records)
        query_label.grid(row= 4, column = 0)
        
        conn.commit()  
        conn.close()


    def enter_data():

        driverTermStatus = terms_status_var.get()

        if driverTermStatus=='Accepted':
            #retrieve user info
            #save surname value in variable
            driverSurname = surname_entry.get()
            driverFname = first_name_entry.get()
            driverAddress = driver_address_entry.get()
            driverPostcode = driver_postcode_entry.get()
            driverTel = driver_tel_entry.get()
            driverDOB = driver_dob_entry.get()
            if validateDate(driverDOB) == True:
                driverGender = driver_gender_combobox.get()
                if driverSurname and driverFname and driverAddress and driverPostcode and driverTel and driverDOB and driverGender:
                    print('Surname: ', driverSurname, '\nFirst name: ', driverFname)
                    print('Address: ', driverAddress, '\nPostcode ', driverPostcode, '\nTel Ext: ', driverTel)
                    print('DOB: ', driverDOB, '\nGender: ', driverGender)
                    print('Terms and conditions:', driverTermStatus)
                    print('------------------------------------------------------------')

                    #connect to sqlite3

                    conn = sqlite3.connect('SpeedyTravelDatabase.db')
                    table_create_query = '''CREATE TABLE IF NOT EXISTS Driver
                    (Driver_No INTEGER, Fname TEXT, Lname TEXT, Address	TEXT, Postcode varchar,
                        Tel_Ext	INTEGER, DOB TEXT, Gender TEXT, PRIMARY KEY(Driver_No AUTOINCREMENT))                               
                    '''
                    conn.execute(table_create_query)

                    #insert data

                    data_insert_query = '''INSERT INTO Driver (Fname, Lname, Address, Postcode, Tel_Ext, DOB, Gender) VALUES (?, ?, ?, ?, ?, ?, ?)'''
                    data_insert_tuple = (driverFname, driverSurname, driverAddress, driverPostcode,
                                        driverTel, driverDOB, driverGender)
                    
                    cursor = conn.cursor()
                    cursor.execute(data_insert_query, data_insert_tuple)
                    conn.commit()

                


                    #close connection
                    conn.close()



                else:
                    tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')
            else:
                tkinter.messagebox.showwarning(title='Invalid Date', message= 'Invalid Date input. Please try again')
        else:
                tkinter.messagebox.showwarning(title='Terms and Conditions', message= 'Please accept terms and conditions')





    window = Toplevel()

    window.title('SpeedyTravels Form')
    #frame is nested inside the window
    # saving widget into a variable  
    frame = tkinter.Frame(window)
    #geometry managers, helps organise widgets on the screen
    #pack keeps things responsive and nicely organised 
    frame.pack()

    #saving user information
    user_info_frame = tkinter.LabelFrame(frame, text= 'User Information')
    user_info_frame.grid(row= 0 , column= 0, padx=20, pady=20)

    #placing this label inside the label frame
    #this is the surname label being placed 
    driver_surname_label = tkinter.Label(user_info_frame, text= 'Driver Surname')
    driver_surname_label.grid(row= 0, column= 0)

    #placing the first name label on the column beside it but on the same row WITHIN the user info frame
    driver_first_name_label = tkinter.Label(user_info_frame, text= 'Driver First Name')
    driver_first_name_label.grid(row= 0, column= 1)

    #creating the enteries for surname and last name 
    surname_entry = tkinter.Entry(user_info_frame)
    first_name_entry = tkinter.Entry(user_info_frame)

    #placing the enteries within the user info frame now on the second row at column 0
    surname_entry.grid(row=1, column= 0)
    first_name_entry.grid(row=1, column = 1)

    #creating gender list for users to only choose male and female
    #always specify the parent
    driver_gender_label = tkinter.Label(user_info_frame, text='Gender')
    #allow user to choose from selection of gender
    driver_gender_combobox = ttk.Combobox(user_info_frame, values=['Male', 'Female'])
    #placing combo entry and label
    driver_gender_label.grid(row= 0, column= 2)
    driver_gender_combobox.grid(row=1, column = 2)

    #driver date of birth
    driver_dob_label = tkinter.Label(user_info_frame, text= 'DOB (yyyy-mm-dd)')
    driver_dob_entry = tkinter.Entry(user_info_frame)
    driver_dob_label.grid(row= 2, column=0)
    driver_dob_entry.grid(row=3, column=0)

    #changing padding for every grid item in first frame
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady= 5)



    #creating second frame for more driver info
    driver_second_frame = tkinter.LabelFrame(frame)
    #sticky news(north east west south) expand in these directions so that it is the same size as previous frame, consistent 
    driver_second_frame.grid(row= 1 , column= 0, sticky='news', padx=20, pady=10)

    #driver address label and entry
    driver_address_label = tkinter.Label(driver_second_frame, text='Address')
    driver_address_entry= tkinter.Entry(driver_second_frame)
    driver_address_label.grid(row= 0, column= 0)
    driver_address_entry.grid(row=1, column= 0)

    #driver postcode label and entry 
    driver_postcode_label = tkinter.Label(driver_second_frame, text='Postcode')
    driver_postcode_entry= tkinter.Entry(driver_second_frame)
    driver_postcode_label.grid(row= 0, column= 1)
    driver_postcode_entry.grid(row=1, column= 1)

    #driver tel label and entry 
    driver_tel_label = tkinter.Label(driver_second_frame, text='Tel Ext.')
    driver_tel_entry= tkinter.Entry(driver_second_frame)
    driver_tel_label.grid(row= 0, column= 2)
    driver_tel_entry.grid(row=1, column= 2)

    #changing padding for every grid item in first frame
    for widget in driver_second_frame.winfo_children():
        widget.grid_configure(padx=10, pady= 5)

    #creating third frame for more driver info
    driver_third_frame = tkinter.LabelFrame(frame, text='Terms & Conditions') 
    driver_third_frame.grid(row= 2 , column= 0, sticky='news', padx=20, pady=10)


    #creating variable to store whether user has checked terms and conditions or not
    terms_status_var = tkinter.StringVar(value='Not Accepted')
    terms_check = tkinter.Checkbutton(driver_third_frame, text='I accept the terms and conditions', 
                                    variable= terms_status_var, onvalue='Accepted', offvalue='Not Accepted')
    terms_check.grid(row=0, column=0)

    #adding final data entry button
    #want button to exist outside the other frames but within the main frame
    #when button is clicked execute function enter data
    button = tkinter.Button(driver_third_frame, text='Submit', command= enter_data)
    button.grid(row= 1, column=2, sticky='news', ipadx= 90)

        
    #show data button
    show_data_button = tkinter.Button(driver_third_frame, text='Show Data', command= showData)
    show_data_button.grid(row= 2, column=2, sticky='news', ipadx=90 , pady= 5)


    #new frame for delete and update button

    driver_fourth_frame = tkinter.LabelFrame(frame, text= 'Edit Data')
    #sticky news(north east west south) expand in these directions so that it is the same size as previous frame, consistent 
    driver_fourth_frame.grid(row= 3 , column= 0, sticky='news', padx=20, pady=10)

    #delete function
    def delete():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from Driver WHERE oid= ' + delete_entry.get()) 

        conn.commit()  
        conn.close()


    #delete button and entry 
    delete_label= Label(driver_fourth_frame, text= 'Enter Driver Number' )
    delete_label.grid(row= 0, column= 0)
    delete_entry = Entry(driver_fourth_frame, width=30)
    delete_entry.grid(row= 1, column= 0)


    delete_button = tkinter.Button(driver_fourth_frame, text='Delete Record', command= delete)
    delete_button.grid(row= 1, column=1, sticky='news', ipadx=90 , pady= 5, padx= 5)
    
    def update():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        record_id = delete_entry.get()

        cursor.execute("""UPDATE Driver SET 
                    
                Fname = :fname, 
                Lname = :lname, 
                Address = :address,
                Postcode = :postcode,
                Tel_Ext = :tel_Ext,
                DOB = :dob,
                Gender = :gender
                
                WHERE oid = :oid """,

    #create dictionary to give values to ^ (the keys and we match them to the entries)
                { 'fname': first_name_entry_edit.get(),
                    'lname': surname_entry_edit.get(),
                    'address': driver_address_entry_edit.get(),
                    'postcode': driver_postcode_entry_edit.get(),
                    'tel_Ext': driver_tel_entry_edit.get(),
                    'dob': driver_dob_entry_edit.get(),
                    'gender': driver_gender_combobox_edit.get(),

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
        cursor.execute("SELECT * FROM Driver WHERE oid =" + record_id)
        records = cursor.fetchall()
        print(records)



        editor = Tk()
        editor.title('Edit Record')
        editor.geometry('400x600')


        #create global variables to access in dictionary 
        global surname_entry_edit
        global first_name_entry_edit
        global driver_gender_combobox_edit
        global driver_dob_entry_edit
        global driver_address_entry_edit
        global driver_postcode_entry_edit
        global driver_tel_entry_edit

        user_info_frame = tkinter.LabelFrame(editor, text= 'User Information')
        user_info_frame.grid(row= 0 , column= 0, padx=20, pady=20)

        #placing this label inside the label frame
        #this is the surname label being placed 
        driver_surname_label = tkinter.Label(user_info_frame, text= 'Driver Surname')
        driver_surname_label.grid(row= 0, column= 0)

        #placing the first name label on the column beside it but on the same row WITHIN the user info frame
        driver_first_name_label = tkinter.Label(user_info_frame, text= 'Driver First Name')
        driver_first_name_label.grid(row= 0, column= 1)

        #creating the enteries for surname and last name 
        surname_entry_edit = tkinter.Entry(user_info_frame)
        first_name_entry_edit = tkinter.Entry(user_info_frame)

        #placing the enteries within the user info frame now on the second row at column 0
        surname_entry_edit.grid(row=1, column= 0)
        first_name_entry_edit.grid(row=1, column = 1)

        #creating gender list for users to only choose male and female
        #always specify the parent
        driver_gender_label = tkinter.Label(user_info_frame, text='Gender')
        #allow user to choose from selection of gender
        driver_gender_combobox_edit = ttk.Combobox(user_info_frame, values=['Male', 'Female'])
        #placing combo entry and label
        driver_gender_label.grid(row= 0, column= 2)
        driver_gender_combobox_edit.grid(row=1, column = 2)

        #driver date of birth
        driver_dob_label = tkinter.Label(user_info_frame, text= 'DOB (yyyy-mm-dd)')
        driver_dob_entry_edit = tkinter.Entry(user_info_frame)
        driver_dob_label.grid(row= 2, column=0)
        driver_dob_entry_edit.grid(row=3, column=0)

        #changing padding for every grid item in first frame
        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady= 5)



        #creating second frame for more driver info
        driver_second_frame = tkinter.LabelFrame(editor)
        #sticky news(north east west south) expand in these directions so that it is the same size as previous frame, consistent 
        driver_second_frame.grid(row= 1 , column= 0, sticky='news', padx=20, pady=10)

        #driver address label and entry
        driver_address_label = tkinter.Label(driver_second_frame, text='Address')
        driver_address_entry_edit= tkinter.Entry(driver_second_frame)
        driver_address_label.grid(row= 0, column= 0)
        driver_address_entry_edit.grid(row=1, column= 0)

        #driver postcode label and entry 
        driver_postcode_label = tkinter.Label(driver_second_frame, text='Postcode')
        driver_postcode_entry_edit= tkinter.Entry(driver_second_frame)
        driver_postcode_label.grid(row= 0, column= 1)
        driver_postcode_entry_edit.grid(row=1, column= 1)

        #driver tel label and entry 
        driver_tel_label = tkinter.Label(driver_second_frame, text='Tel Ext.')
        driver_tel_entry_edit= tkinter.Entry(driver_second_frame)
        driver_tel_label.grid(row= 0, column= 2)
        driver_tel_entry_edit.grid(row=1, column= 2)

        #changing padding for every grid item in first frame
        for widget in driver_second_frame.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

        #add values to input boxes once user has entered the route number
        for record in records:
            surname_entry_edit.insert(0, record[1])
            first_name_entry_edit.insert(0, record[2])
            driver_gender_combobox_edit.insert(0, record[7])
            driver_dob_entry_edit.insert(0, record[6])
            driver_address_entry_edit.insert(0, record[3])
            driver_postcode_entry_edit.insert(0, record[4])
            driver_tel_entry_edit.insert(0, record[5])



        editor_submit = Button(editor, text='Submit Changes', command= update)
        editor_submit.grid(row= 2, column= 0, pady= 10, padx= 10, ipadx= 50)

        conn.commit()  
        conn.close()
    #update button
    edit_button = tkinter.Button(driver_fourth_frame, text='Edit Record', command= edit)
    edit_button.grid(row= 2, column=1, sticky='news', ipadx=90 , pady= 5, padx= 5)
    




    #infinte main loop that runs while the window is open
    #dont put anything underneath this
    window.mainloop()


