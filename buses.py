import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
from tkinter import *

def validateDate(date):
    if int(date[5:7]) > 12:
        return False
    elif int(date[8:10]) > 32:
        return False
    elif int(date[0:4]) > 2025:
        return False
    return True


def busesWin():

    def enter_data():
        registrationNO = registration_entry.get()
        registrationYear = registration_year_entry.get()
        seatingCap = seating_capacity_spinBox.get()
        lastServiced = last_serviced_entry.get()
        lastMOTED = last_MOTED_entry.get()
        if registrationNO and registrationYear and seatingCap and lastServiced and lastMOTED:
            if validateDate(lastServiced) == True and validateDate(lastMOTED) == True:
                print('Reg No:', registrationNO, 'Year: ', registrationYear, 'Seating Capacity: ', seatingCap)
                print('Last Serviced: ', lastServiced, 'Last MOTED: ', lastMOTED)

                #connect to sqlite3

                conn = sqlite3.connect('SpeedyTravelDatabase.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS Buses
                (Bus_Number INTEGER, Registration_Number INTEGER UNIQUE, Seating_Capacity INTEGER, Last_Serviced TEXT, Last_MOTED TEXT,
                    PRIMARY KEY("Bus_Number" AUTOINCREMENT))                                            
                '''
                conn.execute(table_create_query)

                #insert data

                data_insert_query = '''INSERT INTO Buses (Registration_Number, Registration_Year, Seating_Capacity, Last_Serviced, Last_MOTED) VALUES (?, ?, ?, ?, ?)'''
                data_insert_tuple = (registrationNO, registrationYear, seatingCap, lastServiced,lastMOTED)
                
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()

                


                #close connection
                conn.close()










            else:
                tkinter.messagebox.showwarning(title='Invalid Date', message= 'Invalid Date input. Please try again')
        else:
            tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')

    window = Toplevel()

    window.title('Buses Form')
    frame = tkinter.Frame(window)
    frame.pack()

    #first frame of buses
    bus_info_frame1 = tkinter.LabelFrame(frame, text= 'Bus Information')
    bus_info_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

    #registration label + entry in frame 1
    registration_Number_label = tkinter.Label(bus_info_frame1, text= 'Registration Number')
    registration_Number_label.grid(row= 0, column= 0)
    registration_entry = tkinter.Entry(bus_info_frame1)
    registration_entry.grid(row=1, column=0)

    #year of reg
    registration_year_label = tkinter.Label(bus_info_frame1, text='Year of Registration')
    registration_year_entry = tkinter.Entry(bus_info_frame1)
    registration_year_label.grid(row=0, column=1)
    registration_year_entry.grid(row=1, column=1)

    #seating capacity
    seating_capacity_label = tkinter.Label(bus_info_frame1, text='Seating Capacity')
    seating_capacity_label.grid(row=2, column=0)
    seating_capacity_spinBox = tkinter.Spinbox(bus_info_frame1, from_=10,  to= 'infinity')
    seating_capacity_spinBox.grid(row = 3, column= 0)

    #Last date serviced 
    last_serviced_label = tkinter.Label(bus_info_frame1, text= 'Last Serviced (yyyy-mm-dd)')
    last_serviced_entry = tkinter.Entry(bus_info_frame1)
    last_serviced_label.grid(row= 2, column=1)
    last_serviced_entry.grid(row=3, column=1)

    #last date moted 
    last_MOTED_label = tkinter.Label(bus_info_frame1, text= "Last MOT'ed(yyyy-mm-dd) ")
    last_MOTED_entry = tkinter.Entry(bus_info_frame1)
    last_MOTED_label.grid(row= 4, column=0)
    last_MOTED_entry.grid(row=5, column=0)


    #spacing
    for widget in bus_info_frame1.winfo_children():
        widget.grid_configure(padx=10, pady= 5)


    button = tkinter.Button(bus_info_frame1, text='Submit', command= enter_data)
    button.grid(row= 6, column=1, sticky='news' , padx=10, pady=10)

    #display data

    def showData():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM Buses")
        records = cursor.fetchall()
        print(records)

        print_records = ''
        #loop through the records and turn them into a string + add new line
        for record in records:
            print_records += str(record[0]) + '\t' + str(record[1]) + ' \t ' + ' Seating: '+ str(record[3]) +'\n' 

        query_label = Label(frame, text = print_records)
        query_label.grid(row= 3, column = 0)
        


        conn.commit()  
        conn.close()


    #display data button
    show_data_button = tkinter.Button(bus_info_frame1, text='Show Data', command= showData)
    show_data_button.grid(row= 6, column= 0, sticky='news' , padx=10, pady=10)


    #second frame for edit and deleting records
    bus_info_frame2 = tkinter.LabelFrame(frame, text= 'Edit Data')
    bus_info_frame2.grid(row= 2 , column= 0, padx=20, pady=20)


    def delete():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from Buses WHERE oid= ' + delete_entry.get()) 

    

    
        conn.commit()  
        conn.close()

    #delete entry and button
    delete_label= Label(bus_info_frame2, text= 'Enter Bus Number: ' )
    delete_label.grid(row= 0, column= 0)
    delete_entry = Entry(bus_info_frame2, width=30,)
    delete_entry.grid(row= 0, column= 1, padx= 10)

    delete_button = tkinter.Button(bus_info_frame2, text='Delete Data', command= delete)
    delete_button.grid(row= 1, column= 1, sticky='news' , padx=10, pady=5)

    #edit button

    def update():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        record_id = delete_entry.get()

        cursor.execute("""UPDATE Buses SET 
                              
                Registration_Number = :regNo,
                Registration_Year = :year, 
                Seating_Capacity = :capacity, 
                Last_Serviced = :serviced, 
                Last_MOTED = :moted
                
                WHERE oid = :oid """,

        #create dictionary to give values to ^ (the keys and we match them to the entries)
                { 'regNo': registration_entry_edit.get(),
                    'year': registration_year_entry_edit.get(),
                    'capacity': seating_capacity_spinBox_edit.get(),
                    'serviced': last_serviced_entry_edit.get(),
                    'moted': last_MOTED_entry_edit.get(),

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
        cursor.execute("SELECT * FROM Buses WHERE oid =" + record_id)
        records = cursor.fetchall()
        print(records)
        
    

        editor = Tk()
        editor.title('Edit Record')
        editor.geometry('400x600')


        #create global variables to access in dictionary 
        global registration_entry_edit
        global registration_year_entry_edit
        global seating_capacity_spinBox_edit
        global last_serviced_entry_edit
        global last_MOTED_entry_edit

        #first frame of buses
        bus_info_frame1 = tkinter.LabelFrame(editor, text= 'Bus Information')
        bus_info_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

        #registration label + entry in frame 1
        registration_Number_label = tkinter.Label(bus_info_frame1, text= 'Registration Number')
        registration_Number_label.grid(row= 0, column= 0)
        registration_entry_edit = tkinter.Entry(bus_info_frame1)
        registration_entry_edit.grid(row=1, column=0)

        #year of reg
        registration_year_label = tkinter.Label(bus_info_frame1, text='Year of Registration')
        registration_year_entry_edit = tkinter.Entry(bus_info_frame1)
        registration_year_label.grid(row=0, column=1)
        registration_year_entry_edit.grid(row=1, column=1)

        #seating capacity
        seating_capacity_label = tkinter.Label(bus_info_frame1, text='Seating Capacity')
        seating_capacity_label.grid(row=2, column=0)
        seating_capacity_spinBox_edit = tkinter.Spinbox(bus_info_frame1,  to= 'infinity')
        seating_capacity_spinBox_edit.grid(row = 3, column= 0)

        #Last date serviced 
        last_serviced_label = tkinter.Label(bus_info_frame1, text= 'Last Serviced (yyyy-mm-dd)')
        last_serviced_entry_edit = tkinter.Entry(bus_info_frame1)
        last_serviced_label.grid(row= 2, column=1)
        last_serviced_entry_edit.grid(row=3, column=1)

        #last date moted 
        last_MOTED_label = tkinter.Label(bus_info_frame1, text= "Last MOT'ed(yyyy-mm-dd) ")
        last_MOTED_entry_edit = tkinter.Entry(bus_info_frame1)
        last_MOTED_label.grid(row= 4, column=0)
        last_MOTED_entry_edit.grid(row=5, column=0)

        

        editor_submit = Button(editor, text='Submit Changes', command= update)
        editor_submit.grid(row= 1, column= 0, pady= 10, padx= 10, sticky='news')


        #spacing
        for widget in bus_info_frame1.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

    #add values to input boxes once user has entered the route number
        for record in records:
            registration_entry_edit.insert(0, record[1])
            registration_year_entry_edit.insert(0, record[2])
            seating_capacity_spinBox_edit.insert(0, record[3])
            last_serviced_entry_edit.insert(0, record[4])
            last_MOTED_entry_edit.insert(0, record[5])


        

        conn.commit()  
        conn.close()

    edit_button = tkinter.Button(bus_info_frame2, text='Edit Data', command= edit)
    edit_button.grid(row= 2, column= 1, sticky='news' , padx=10, pady=5)

    window.mainloop()




















