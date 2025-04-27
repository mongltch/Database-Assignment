

word = '2035-12-31'

def validateMonth(date):
    if int(date[5:7]) > 12:
        return 'this is not a valid month'
    elif int(date[8:10]) > 32:
        return 'this is not a valid date'
    elif int(date[0:4]) > 2025:
        return 'this is not a valid year'
    return 'valid month'



table_create_query = '''CREATE TABLE IF NOT EXISTS Buses
            (Bus_Number INTEGER, Registration_Number INTEGER UNIQUE, Seating_Capacity INTEGER, Last_Serviced TEXT, Last_MOTED TEXT,
            PRIMARY KEY("Bus_Number" AUTOINCREMENT))                                         
            '''