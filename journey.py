import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
from tkinter import *

def journeyWin():
    def enter_data():
        busNO = bus_number_entry.get()
        routeNO = route_number_entry.get()
        driverNO = driver_number_entry.get()
        day = day_entry.get()
        startTime = startTime_entry.get()
        finishTime = finishTime_entry.get()

        if busNO and routeNO and driverNO and day and startTime and finishTime:
            if int(startTime) <= 2300 and int(finishTime) <= 2300:

                conn = sqlite3.connect('SpeedyTravelDatabase.db')
                table_create_query = '''CREATE TABLE IF NOT EXISTS Journey
                (Journey_No INTEGER, Bus_Number INTEGER, Route_No INTEGER, Driver_No INTEGER, Day_Of_Week TEXT, Start_Time INTEGER,
                Finish_Time INTEGER, PRIMARY KEY(Journey_No AUTOINCREMENT), FOREIGN KEY(Bus_Number) REFERENCES Buses (Bus_Number),
                FOREIGN KEY(Driver_No) REFERENCES Driver (Driver_No), FOREIGN KEY(Route_No) REFERENCES Route (Route_Number))
                                                        
                '''
                conn.execute(table_create_query)

                #insert data

                data_insert_query = '''INSERT INTO Journey (Bus_Number, Route_No, Driver_No, Day_Of_Week, Start_Time, Finish_Time) VALUES (?, ?, ?, ?, ?, ?)'''
                data_insert_tuple = (busNO, routeNO, driverNO, day , startTime, finishTime)
                
                cursor = conn.cursor()
                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()

                


                #close connection
                conn.close()








                print('works')
            else:
                tkinter.messagebox.showwarning(title='Invalid Time', message= 'Invalid Time input. Please try again')
        else:
            tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')


    window = tkinter.Tk()

    window.title('Journey Form')
    frame = tkinter.Frame(window)
    frame.pack()



    journey_frame1 = tkinter.LabelFrame(frame, text= 'Journey')
    journey_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


    bus_number_label = tkinter.Label(journey_frame1, text='Bus Number')
    bus_number_label.grid(row= 0, column= 0)
    bus_number_entry = tkinter.Entry(journey_frame1)
    bus_number_entry.grid(row=1, column=0)

    route_number_label = tkinter.Label(journey_frame1, text='Route Number')
    route_number_label.grid(row= 0, column= 1)
    route_number_entry = tkinter.Entry(journey_frame1)
    route_number_entry.grid(row=1, column=1)

    driver_number_label = tkinter.Label(journey_frame1, text='Driver Number')
    driver_number_label.grid(row= 2, column= 0)
    driver_number_entry = tkinter.Entry(journey_frame1)
    driver_number_entry.grid(row=3, column=0)

    day_label = tkinter.Label(journey_frame1, text='Day of week')
    day_label.grid(row= 2, column= 1)
    day_entry = tkinter.Entry(journey_frame1)
    day_entry.grid(row=3, column=1)

    startTime_label = tkinter.Label(journey_frame1, text='Journey Start Time \n(e.g. 14:00 = 1400)')
    startTime_label.grid(row= 4, column= 0)
    startTime_entry = tkinter.Entry(journey_frame1)
    startTime_entry.grid(row=5, column=0)

    finishTime_label = tkinter.Label(journey_frame1, text='Journey Finish Time \n(e.g. 16:30 = 1630)')
    finishTime_label.grid(row= 4, column= 1)
    finishTime_entry = tkinter.Entry(journey_frame1)
    finishTime_entry.grid(row=5, column=1)


    for widget in journey_frame1.winfo_children():
        widget.grid_configure(padx=10, pady= 5)


    button = tkinter.Button(journey_frame1, text='Submit', command= enter_data)
    button.grid(row= 6, column=1, sticky='news' , padx=10, pady=10)

    def showData():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM Journey")
        records = cursor.fetchall()
        print(records)

        print_records = ''
        #loop through the records and turn them into a string + add new line
        for record in records:
            print_records += 'Journey No: ' + str(record[0]) + ' \t' + 'Day: '+ str(record[4]) + '\t' + ' Start: '+ str(record[5]) + '\t' +'Finish: ' + str(record[6]) +'\n' 

        query_label = Label(frame, text = print_records)
        query_label.grid(row= 2, column = 0)
        


        conn.commit()  
        conn.close()

    show_data_button = tkinter.Button(journey_frame1, text='Show Data', command= showData)
    show_data_button.grid(row= 6, column=0, sticky='news' , padx=10, pady=10)


    #delete and edit records frame 

    journey_frame2 = tkinter.LabelFrame(frame, text= 'Edit data')
    journey_frame2.grid(row= 1 , column= 0, padx=20, pady=20)

    #delete frame 

    #delete function 

    def delete():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from Journey WHERE oid= ' + delete_entry.get()) 

        

        
        conn.commit()  
        conn.close()

    delete_btn = Button(journey_frame2, text= 'Delete Record', command= delete)
    delete_btn.grid(row = 2, column= 1, pady= 5, padx= 10, ipadx= 54)

    delete_label= Label(journey_frame2, text= 'Enter Journey Number' )
    delete_label.grid(row= 0, column= 0)
    delete_entry = Entry(journey_frame2, width=30)
    delete_entry.grid(row= 0, column= 1)

    #edit data 

    def update():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        record_id = delete_entry.get()

        cursor.execute("""UPDATE Journey SET 
                    
                    
                Bus_Number = :busNo, 
                Route_No = :routeNo, 
                Driver_No = :driverNo, 
                Day_Of_Week = :days,
                Start_Time = :start,
                Finish_Time = :finish
                
                WHERE oid = :oid """,

    #create dictionary to give values to ^ (the keys and we match them to the entries)
                { 'busNo': bus_number_entry_edit.get(),
                    'routeNo': route_number_entry_edit.get(),
                    'driverNo': driver_number_entry_edit.get(),
                    'days': day_entry_edit.get(),
                    'start': startTime_entry_edit.get(),
                    'finish': finishTime_entry_edit.get(),

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
        cursor.execute("SELECT * FROM Journey WHERE oid =" + record_id)
        records = cursor.fetchall()
        print(records)
        
    

        editor = Tk()
        editor.title('Edit Record')
        editor.geometry('400x600')


        #create global variables to access in dictionary 
        global bus_number_entry_edit
        global route_number_entry_edit
        global driver_number_entry_edit
        global day_entry_edit
        global startTime_entry_edit
        global finishTime_entry_edit

        journey_frame1 = tkinter.LabelFrame(editor, text= 'Journey')
        journey_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


        bus_number_label = tkinter.Label(journey_frame1, text='Bus Number')
        bus_number_label.grid(row= 0, column= 0)
        bus_number_entry_edit = tkinter.Entry(journey_frame1)
        bus_number_entry_edit.grid(row=1, column=0)

        route_number_label = tkinter.Label(journey_frame1, text='Route Number')
        route_number_label.grid(row= 0, column= 1)
        route_number_entry_edit = tkinter.Entry(journey_frame1)
        route_number_entry_edit.grid(row=1, column=1)

        driver_number_label = tkinter.Label(journey_frame1, text='Driver Number')
        driver_number_label.grid(row= 2, column= 0)
        driver_number_entry_edit = tkinter.Entry(journey_frame1)
        driver_number_entry_edit.grid(row=3, column=0)

        day_label = tkinter.Label(journey_frame1, text='Day of week')
        day_label.grid(row= 2, column= 1)
        day_entry_edit = tkinter.Entry(journey_frame1)
        day_entry_edit.grid(row=3, column=1)

        startTime_label = tkinter.Label(journey_frame1, text='Journey Start Time \n(e.g. 14:00 = 1400)')
        startTime_label.grid(row= 4, column= 0)
        startTime_entry_edit = tkinter.Entry(journey_frame1)
        startTime_entry_edit.grid(row=5, column=0)

        finishTime_label = tkinter.Label(journey_frame1, text='Journey Finish Time \n(e.g. 16:30 = 1630)')
        finishTime_label.grid(row= 4, column= 1)
        finishTime_entry_edit = tkinter.Entry(journey_frame1)
        finishTime_entry_edit.grid(row=5, column=1)


        for widget in journey_frame1.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

    #add values to input boxes once user has entered the route number
        for record in records:
            bus_number_entry_edit.insert(0, record[1])
            route_number_entry_edit.insert(0, record[2])
            driver_number_entry_edit.insert(0, record[3])
            day_entry_edit.insert(0, record[4])
            startTime_entry_edit.insert(0, record[5])
            finishTime_entry_edit.insert(0, record[6])


        editor_submit = Button(editor, text='Submit Changes', command= update)
        editor_submit.grid(row= 2, column= 0, pady= 10, padx= 10,ipadx= 50)

        conn.commit()  
        conn.close()

    edit_btn = Button(journey_frame2, text= 'Edit Record', command= edit)
    edit_btn.grid(row = 3, column= 1, pady= 5, padx= 10, sticky='news')




    window.mainloop()