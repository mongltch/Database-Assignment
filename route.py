import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
from tkinter import *



def routeWin():

    def enter_data():
        routeNO = route_number_entry.get()
        starting_point = starting_point_entry.get()
        destination = destination_entry.get()
        miles = length_spinBox.get()
        if routeNO and starting_point and destination and miles:
            print('hi')

            conn = sqlite3.connect('SpeedyTravelDatabase.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Route
                (Route_Number INTEGER, Starting_Point TEXT, Destination TEXT, Length_Miles INTEGER, 
                PRIMARY KEY(Route_Number)) '''

            conn.execute(table_create_query)

            

            data_insert_query = '''INSERT INTO Route (Route_Number, Starting_Point, Destination, Length_Miles) VALUES (?, ?, ?, ?)'''
            data_insert_tuple = (routeNO, starting_point, destination, miles)
            
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            


            #close connection
            conn.close()



        else:
            tkinter.messagebox.showwarning(title='Complete Form', message= 'Must fill all sections before submission')

    window = tkinter.Tk()

    window.title('Route Form')
    frame = tkinter.Frame(window)
    frame.pack()


    route_frame1 = tkinter.LabelFrame(frame, text= 'Route Information')
    route_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

    route_number_label = tkinter.Label(route_frame1, text= 'Route Number')
    route_number_label.grid(row= 0, column= 0)
    route_number_entry = tkinter.Entry(route_frame1)
    route_number_entry.grid(row=1, column=0)


    starting_point_label = tkinter.Label(route_frame1, text= 'Starting Point')
    starting_point_label.grid(row= 0, column= 1)
    starting_point_entry = tkinter.Entry(route_frame1)
    starting_point_entry.grid(row=1, column=1)


    destination_label = tkinter.Label(route_frame1, text='Destination')
    destination_label.grid(row=2, column=0)
    destination_entry = tkinter.Entry(route_frame1)
    destination_entry.grid(row=3, column=0)


    length_label = tkinter.Label(route_frame1, text='Length in Miles')
    length_label.grid(row=2, column=1)
    length_spinBox = tkinter.Spinbox(route_frame1, from_=10,  to= 'infinity')
    length_spinBox.grid(row = 3, column= 1)

    for widget in route_frame1.winfo_children():
        widget.grid_configure(padx=10, pady= 5)


    route_second_frame = tkinter.LabelFrame(frame, text= 'Records')
        #sticky news(north east west south) expand in these directions so that it is the same size as previous frame, consistent 
    route_second_frame.grid(row= 1 , column= 0, padx=20, pady=10)

    button = tkinter.Button(route_frame1, text='Submit', command= enter_data)
    button.grid(row= 4, column=1, pady= 10, padx= 10, sticky='news')

    #delete record have to refresh to see it deleted oid = primary key
    def delete():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute('DELETE from route WHERE oid= ' + delete_entry.get()) 

        

        
        conn.commit()  
        conn.close()
        

    #display records function added to button

    def query():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        cursor.execute("SELECT *, oid FROM Route")
        records = cursor.fetchall()
        print(records)

        print_records = ''
        #loop through the records and turn them into a string + add new line
        for record in records:
            print_records += 'Route Number: ' + str(record[0]) + '\n' + 'Starting: '+ str(record[1]) + ',' + ' Finishing: '+ str(record[2]) +'\n' 

        query_label = Label(frame, text = print_records)
        query_label.grid(row= 4, column = 0)
        


        conn.commit()  
        conn.close()

    #create button to display queries / or show data
    query_btn = Button(route_frame1, text= 'Show Data', command=query)
    query_btn.grid(row = 4, column= 0, pady= 10, padx= 10, sticky='news')

    #create delete button
    delete_btn = Button(route_second_frame, text= 'Delete Record', command= delete)
    delete_btn.grid(row = 5, column= 1, pady= 10, padx= 10, ipadx= 54)

    delete_label= Label(route_second_frame, text= 'Enter Route Number' )
    delete_label.grid(row= 4, column= 0)
    delete_entry = Entry(route_second_frame, width=30)
    delete_entry.grid(row= 4, column= 1)


    #function runs after we have submitted changes and want to update
    #finish this


    def update():
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()

        record_id = delete_entry.get()

        cursor.execute("""UPDATE Route SET 
                    
                    
                Route_Number = :routeNo, 
                Starting_Point = :starting, 
                Destination = :destination, 
                Length_Miles = :miles
                
                WHERE oid = :oid """,

    #create dictionary to give values to ^ (the keys and we match them to the entries)
                { 'routeNo': route_number_entry_edit.get(),
                    'starting': starting_point_entry_edit.get(),
                    'destination': destination_entry_edit.get(),
                    'miles': length_spinBox_edit.get(),

                    'oid': record_id

                })

        conn.commit()  
        conn.close()

        editor.destroy()

        


    #function to update record
    #will pop up in a new window
    def edit():
        global editor
        conn = sqlite3.connect('SpeedyTravelDatabase.db')
        cursor = conn.cursor()
        #store the value user has input into variable so that we can find it

        record_id = delete_entry.get()
        cursor.execute("SELECT * FROM Route WHERE oid =" + record_id)
        records = cursor.fetchall()
        print(records)
        
    

        editor = Tk()
        editor.title('Edit Record')
        editor.geometry('400x600')


        #create global variables to access in dictionary 
        global route_number_entry_edit
        global starting_point_entry_edit
        global destination_entry_edit
        global length_spinBox_edit

        route_frame1 = tkinter.LabelFrame(editor, text= 'Route Information')
        route_frame1.grid(row= 0 , column= 0, padx=20, pady=20)

        route_number_label = tkinter.Label(route_frame1, text= 'Route Number')
        route_number_label.grid(row= 0, column= 0)
        route_number_entry_edit = tkinter.Entry(route_frame1)
        route_number_entry_edit.grid(row=1, column=0)


        starting_point_label = tkinter.Label(route_frame1, text= 'Starting Point')
        starting_point_label.grid(row= 0, column= 1)
        starting_point_entry_edit = tkinter.Entry(route_frame1)
        starting_point_entry_edit.grid(row=1, column=1)


        destination_label = tkinter.Label(route_frame1, text='Destination')
        destination_label.grid(row=2, column=0)
        destination_entry_edit = tkinter.Entry(route_frame1)
        destination_entry_edit.grid(row=3, column=0)


        length_label = tkinter.Label(route_frame1, text='Length in Miles')
        length_label.grid(row=2, column=1)
        length_spinBox_edit = tkinter.Spinbox(route_frame1, from_=10,  to= 'infinity')
        length_spinBox_edit.grid(row = 3, column= 1)

        for widget in route_frame1.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

    #add values to input boxes once user has entered the route number
        for record in records:
            route_number_entry_edit.insert(0, record[0])
            starting_point_entry_edit.insert(0, record[1])
            destination_entry_edit.insert(0, record[2])
            length_spinBox_edit.insert(0, record[3])


        editor_submit = Button(route_frame1, text='Submit Changes', command= update)
        editor_submit.grid(row= 4, column= 1, pady= 10, padx= 10, sticky='news')

        conn.commit()  
        conn.close()

    #update button
    update_btn = Button(route_second_frame, text= 'Edit Record', command= edit)
    update_btn.grid(row = 6, column= 1, pady= 10, padx= 10, sticky='news')



    window.mainloop()