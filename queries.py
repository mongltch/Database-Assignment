import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.font
import tkinter.messagebox
import sqlite3
from tkinter import *
import tkinter.font as tkFont


def highestSalary():
    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT Fname, Lname, Driver_Number, MAX(Salary)
                    FROM Bank_Account
                    INNER JOIN Driver
                    ON Bank_account.Driver_Number = Driver.Driver_No""")
    
    records = cursor.fetchall()
    print(records)

    editor = Tk()
    editor.title('Highest Earner')
    editor.geometry('400x600')

    print_records = ''
    for record in records:
        print_records +=  'Name: '+ str(record[0]) + ' ' +  str(record[1]) + '\n' +  ' Driver No: ' + str(record[2]) + '\n' + 'Salary: £' + str(record[3])

    custom_font = tkFont.Font(family='Arial', size= 25)
    query_label = Label(editor, text = print_records, font= custom_font)
    query_label.place(relx= 0.4, rely= 0.5)

    


def selectDay():
    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

    #this needs to be in single quotes because we can only search using the single quotes
    def dayEntered():
        cursor.execute("""SELECT Bus_Number,Fname, Lname, Journey.Driver_No, Day_Of_Week
                    FROM Journey
                    INNER JOIN Driver
                    ON Journey.Driver_No = Driver.Driver_No
                    WHERE Day_of_Week =""" + "'" + enter_day_entry.get() + "'")
        
        records = cursor.fetchall()
        print(records)

        print_records = ''
        for record in records:
            print_records +=  'Bus Number: ' + str(record[0]) + ' \t ' +  ' Name: ' + str(record[1]) + ' ' + str(record[2]) + '\t' + ' Driver Number: ' + str(record[3]) + '\t' + 'Day: ' + str(record[4]) + '\n'

        query_label = Label(editor, text = print_records)
        query_label.grid(row= 3, column = 0)

        conn.commit() 

    editor = Tk()
    editor.title('Journey Day Information')
    editor.geometry('400x600')

    enter_day_label = Label(editor, text= 'Enter day of week')
    enter_day_label.grid(row = 0, column= 0)
    enter_day_entry = tkinter.Entry(editor)
    enter_day_entry.grid(row= 1, column= 0)
    enter_day_button = Button(editor, text= 'Submit', command= dayEntered)
    enter_day_button.grid(row= 2, column= 0, ipadx= 50)

    conn.commit()  



def totalSalary():
    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

        #this needs to be in single quotes because we can only search using the single quotes
    def genderSelected():
            cursor.execute("""SELECT SUM(Salary), Gender
                        FROM Bank_Account
                        INNER JOIN Driver 
                        ON Bank_account.Driver_Number = Driver.Driver_No
                        GROUP BY Gender
                        HAVING Gender =""" + "'" + driver_gender_combobox.get() + "'")
            
            records = cursor.fetchall()
            print(records)

            print_records = ''
            for record in records:
                print_records +=  'Sum: £' + str(record[0]) + '\t' + 'Gender: ' + str(record[1]) 

            query_label = Label(editor, text = print_records)
            query_label.grid(row= 3, column = 0)

            conn.commit() 

    editor = Tk()
    editor.title('Gender Information')
    editor.geometry('400x600')

    enter_day_label = Label(editor, text= 'Enter driver gender')
    enter_day_label.grid(row = 0, column= 0)
    driver_gender_combobox = ttk.Combobox(editor, values=['Male', 'Female'])
    driver_gender_combobox.grid(row=1, column = 0)
    enter_day_button = Button(editor, text= 'Submit', command= genderSelected)
    enter_day_button.grid(row= 2, column= 0, ipadx= 45)

    conn.commit()  



def duration():

    editor = Tk()
    editor.title('New driver Salary')
    editor.geometry('400x600')

    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

        #this needs to be in single quotes because we can only search using the single quotes
    
    cursor.execute("""SELECT Journey_No, Start_Time, Finish_Time, Finish_Time - Start_Time AS Duration
                FROM Journey;""")
    
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records +=  'Journey Number: ' + str(record[0]) + '\t' + 'Start Time: ' + str(record[1]) + '\t' + 'Finish Time: ' +  str(record[2]) + '\t' + 'Duration: ' + str(record[3]) + '\n'



    query_label = Label(editor, text = print_records)
    query_label.grid(row= 3, column = 0)
 

    
    conn.commit()
    conn.close()



def selectTime():
    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

    #this needs to be in single quotes because we can only search using the single quotes
    def range():
        cursor.execute("""SELECT Fname, Lname, Journey_No, Start_Time
                        FROM Driver
                        INNER JOIN Journey 
                        ON Journey.Driver_No = Driver.Driver_No
                        WHERE Start_Time BETWEEN """ + enter_time1_entry.get() + ' AND ' + enter_time2_entry.get())
        
        records = cursor.fetchall()
        print(records)

        print_records = ''
        for record in records:
            print_records +=  'Name: ' + str(record[0]) + ' ' + str(record[1]) + '\t' + ' Journey Number: ' + str(record[2]) + '\t' + 'Start Time: ' + str(record[3]) + '\n'

        query_label = Label(editor, text = print_records)
        query_label.grid(row= 5, column = 0)

        conn.commit() 

    editor = Tk()
    editor.title('Enter start time range')
    editor.geometry('400x600')

    enter_day_label = Label(editor, text= 'Enter time (e.g: 14:00 = 1400)')
    enter_day_label.grid(row = 0, column= 0)
    enter_time1_entry = tkinter.Entry(editor)
    enter_time1_entry.grid(row= 1, column= 0)

    enter_day_label = Label(editor, text= 'Enter time 2 (e.g: 12:00 = 1200)')
    enter_day_label.grid(row = 2, column= 0)
    enter_time2_entry = tkinter.Entry(editor)
    enter_time2_entry.grid(row= 3, column= 0)


    enter_day_button = Button(editor, text= 'Submit', command= range)
    enter_day_button.grid(row= 4, column= 0, pady= 5 , ipadx= 45)

    conn.commit()



def newSalary():

    editor = Tk()
    editor.title('Salary Increase')
    editor.geometry('400x600')

    conn = sqlite3.connect('SpeedyTravelDatabase.db')
    cursor = conn.cursor()

        #this needs to be in single quotes because we can only search using the single quotes
    
    cursor.execute("""SELECT Driver_Number, Salary, ROUND(0.06 * Salary, 2) AS Increase_Amount, ROUND(0.06 * Salary, 2) + Salary AS New_Salary
                FROM Bank_Account""")
    
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records +=  'Driver Number: ' + str(record[0]) + '\t' + 'Salary: £' + str(record[1]) + '\t' + 'Amount increase by: +' +  str(record[2]) + '\t' + 'New Salary: £' + str(record[3]) + '\n'



    query_label = Label(editor, text = print_records)
    query_label.grid(row= 3, column = 0)
 

    
    conn.commit()
    conn.close()