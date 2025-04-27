import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
from drivers import *
from tkinter import *
from buses import *
from route import *
from journey import *
from bankAccount import *
from queries import *

menu_window = tkinter.Tk()

menu_window.title('Main Menu')
frame = tkinter.Frame(menu_window)
frame.pack()

menu_frame1 = tkinter.LabelFrame(frame, text= 'Select Form')
menu_frame1.grid(row= 0 , column= 0, padx=20, pady=20)


def openDriversWindow():
    openDrivers()

driver_button = tkinter.Button(menu_frame1, text='Drivers', command= openDriversWindow)
driver_button.grid(row= 0, column=0, sticky='news' , padx=20, pady=10)

def openBusesWindow():
    busesWin()

buses_button = tkinter.Button(menu_frame1, text='Buses', command= openBusesWindow)
buses_button.grid(row= 2, column=0, sticky='news' , padx=20, pady=10)


def openRouteWindow():
    routeWin()

route_button = tkinter.Button(menu_frame1, text='Route', command= openRouteWindow)
route_button.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)


def openJourneyWindow():
    journeyWin()


journey_button = tkinter.Button(menu_frame1, text='Journey', command= openJourneyWindow)
journey_button.grid(row= 4, column=0, sticky='news' , padx=20, pady=10)

def openBankAccount():
    bankAccountWin()


bank_account_button = tkinter.Button(menu_frame1, text='Bank Account', command= openBankAccount)
bank_account_button.grid(row= 5, column=0, sticky='news' , padx=20, pady=10)

for widget in menu_frame1.winfo_children():
        widget.grid_configure(padx=10, pady= 10, ipadx= 50, ipady= 10)



menu_frame2 = tkinter.LabelFrame(frame, text= 'Select Query')
menu_frame2.grid(row= 0 , column= 2, padx=20, pady=20)

display_highest = tkinter.Button(menu_frame2, text='Display Highest Salary', command= highestSalary)
display_highest.grid(row= 0, column=0, sticky='news' , padx=20, pady=10)


display_journeyDays = tkinter.Button(menu_frame2, text='Display journey day information', command= selectDay)
display_journeyDays.grid(row= 1, column=0, sticky='news' , padx=20, pady=10)


display_genderSalary = tkinter.Button(menu_frame2, text='Display total gender salary', command= totalSalary)
display_genderSalary.grid(row= 2, column=0, sticky='news' , padx=20, pady=10)

display_journeyDuration = tkinter.Button(menu_frame2, text='Display journey duration', command= duration)
display_journeyDuration.grid(row= 3, column=0, sticky='news' , padx=20, pady=10)


display_journeyRange = tkinter.Button(menu_frame2, text='Display start time journey range', command= selectTime)
display_journeyRange.grid(row= 4, column=0, sticky='news' , padx=20, pady=10)

display_newSalary = tkinter.Button(menu_frame2, text='New Salary', command= newSalary)
display_newSalary.grid(row= 5, column=0, sticky='news' , padx=20, pady=10)


for widget in menu_frame2.winfo_children():
        widget.grid_configure(padx=10, pady= 10, ipadx= 20, ipady= 10)

menu_window.mainloop()