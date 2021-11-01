#Import alle de nødvendige moduller
from tkinter import *
import time
from PIL import ImageTk, Image
import mysql.connector
import pandas_datareader as web
import ui_screen as pidisplay
import matplotlib.pyplot as plt
from yahoo_fin import stock_info
from functools import partial
import re

global screen
global b
global w

#Connecter til database Kunder, hvis den ikke eksistere, opretter den en ny
db = mysql.connector.connect(
    host="waaseteam2.mysql.database.azure.com",
    user="group2@waaseteam2",
    passwd="Waaseteam2",
    database="waaseteam2",
)
mycursor = db.cursor()

#Åbner vores gui - Main Screen, og kalder den Bank App 
master = Tk()
master.title('Project')
master.configure(background='black')
#Funktioner
#Definere funktion for kunde oprettelse


def activate_screen():
    global ui_screenx
    global screen
    if screen == 0:
        ui_screenx = Toplevel(master)
        screen = 1
        pidisplay.show_data(1, '    on!     ', ui_screenx)
    else:
        screen = 0
        ui_screenx.destroy()


def finish_reg():
    global reg
    reg = StringVar()
    email = temp_email.get() #Definere variabler, som information som systemet får af kunden ved hjælp af .get() funktion
    first_name = temp_firstname.get()
    last_name = temp_lastname.get()
    password = temp_password.get()
    mycursor.execute("SELECT email FROM user")
    myreg = mycursor.fetchall()
    for registrer in myreg:
        reg = registrer[0]
        if email == reg:  # sikre at kunden ikke allerede eksistere i systemet. Dette gøres ved hjælp af find_one, på id's
            notif.config(fg="red", text="Email already used")
            return

    if len(password) < 5:
        notif.config(fg="red", text="Password too short,it should be at least 6 characters")
        return

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        notif.config(fg="red", text="Insert a valid Emil address")
        return

    if email == "" or first_name == "" or last_name == "" or password == "": #Sikre kunden udfylder alle felter.
        notif.config(fg="red",text="Please udfyld alle oplysninger * ") #Hvis et af felterne er tomme, skrives dette til kunden
        return
    else:
        mycursor.execute("INSERT INTO user (first_name, last_name, email, password) VALUES (%s,%s,%s,%s)", (first_name, last_name, email, password))
        db.commit()
        notif.config(fg="green", text="Bruger oprettet")

#Ny variable defineres som register
def register():
    #Definere variabler som skal bruges på login skærmen
    global temp_email
    global temp_firstname
    global temp_lastname
    global temp_password
    global notif
    temp_email = StringVar()
    temp_firstname = StringVar()
    temp_lastname =  StringVar()
    temp_password = StringVar()

    #Åbner login skærmen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.configure(background='black')

    #Laver labels på skærmen
    Label(register_screen, text="Udfyldt dine detaljer her, for at opret dig", bg='black', fg='white', font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Email", bg='black', fg='white', font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="First name", bg='black', fg='white', font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Last name", bg='black', fg='white', font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", bg='black', fg='white', font=('Calibri',12)).grid(row=4,sticky=W)
    notif = Label(register_screen, bg='black', font=('Calibri',12))
    notif.grid(row=7,sticky=N,pady=10)    

    #Entries
    Entry(register_screen, textvariable=temp_email) .grid(row=1, column=1,padx=5)
    Entry(register_screen, textvariable=temp_firstname) .grid(row=2, column=1,padx=5)
    Entry(register_screen, textvariable=temp_lastname) .grid(row=3, column=1,padx=5)
    Entry(register_screen, textvariable=temp_password,show="*") .grid(row=4, column=1,padx=5)

    #Opretter en knap som hedder "Registrer"
    Button(register_screen, text="Registrer", command = finish_reg, bg='black', fg='white', font=('Calibri',12)).grid(row=6, sticky=N,pady=10)
    #Definere ny variable for hvis kunden vil logge ind

def clock():
    Clock_screen = Toplevel(master)
    Clock_screen.title('Clock')
    digi_clock = Label(Clock_screen, font=('Calibri',100), bg="red", fg="black")
    def present_time():
        display_time = time.strftime("%H:%M:%S")
        digi_clock.config(text=display_time)
        if screen == 1:
            digi_clock.after(10000,present_time)
        else:
            digi_clock.after(200, present_time)
        create_data(3, display_time)

    present_time()
    digi_clock.pack()

def login_session():
    global login_email
    global Device_dashboard
    global dev
    global user_id
    global temp_device
    temp_device = StringVar()
    dev = StringVar()
    login_email = temp_login_email.get()
    login_password = temp_login_password.get()

    #Cpr nummer skal stemme overens med et id, og med Password
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()

    for x in myresult:
        if login_email == x[3] and login_password == x[4]:
            user_id = x[0]

            global screen
            screen = 0

            #Finder denne kundes navn, ved hjælp af cpr nummer
            #Åbner en ny skærm efter login er successfuldt
            login_screen.destroy()
            Device_dashboard = Toplevel(master)
            Device_dashboard.configure(background='black')
            Device_dashboard.title('Choose your device')
            Label(Device_dashboard, text="Type your device details in here: ", bg='black', fg='white', font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
            Label(Device_dashboard, text="Add new Mac Adress:", bg='black', fg='white', font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
            Entry(Device_dashboard, textvariable=temp_device) .grid(row=1, column=1,padx=5)

            mycursor.execute("SELECT * FROM device")
            myresult = mycursor.fetchall()
            rownum = 2
            for x in myresult:
                if user_id == x[3]:
                    Button(Device_dashboard, text=x[0], bg='black', fg='white', command=partial(userprofil, x[0])).grid(row=rownum, sticky=N, padx=10)
                    rownum = rownum + 1

            Button(Device_dashboard, text="Submit", bg='black', fg='white', command=partial(userprofil, '')).grid(row=1, column=2,padx=5)

        else:
            #Hvis login ikke er successfuldt
            login_notif.config(fg="red", text="Ingen bruger fundet med denne kombination *")

def create_data(dtype, dinput):

    try:
        mycursor.execute("INSERT INTO input_data (user_ID_data, device_ID, data_type_ID, input) VALUES (%s, %s, %s, %s)", (str(user_id), str(device), dtype, dinput))
        db.commit()
    except mysql.connector.errors.IntegrityError as err:
        print(err)
        mycursor.execute("Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s", (dinput, dtype, str(user_id)))
        db.commit()
    if screen == 1:
        pidisplay.show_data(dtype, dinput, ui_screenx)

def userprofil(mac):
    global device
    device = mac
    if device == '':
        device = temp_device.get()
    Device_dashboard.destroy()
    try:
        mycursor.execute("INSERT INTO device (MAC_address, device_password, device_type_ID, user_ID_device) VALUES (%s, %s, %s, %s)", (str(device),'1234', 1, str(user_id)))
        db.commit()
    except mysql.connector.errors.IntegrityError as err:
        print(err)

    User_dashboard = Toplevel(master)
    User_dashboard.title('Data Portal')
    User_dashboard.configure(background='black')
    Label(User_dashboard, text="Account oversigt", bg='black', fg='white', font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
    Label(User_dashboard, text="Velkommen til din profil", bg='black', fg='white', font=('Calibri',12)).grid(row=1, sticky=N,pady=5)
    Button(User_dashboard, text="Profil", bg='black', fg='white', image =profilimage,command=personal_details).grid(row=3, sticky=N)
    Button(User_dashboard, text="Stocks", bg='black', fg='white',command=AllStocks,font=('Calibri',12),width=30).grid(row=4,sticky=N,padx=10)
    Button(User_dashboard, text="Clock", bg='black', fg='white', command=clock,font=('Calibri',12),width=30).grid(row=5,sticky=N,padx=10)
    Button(User_dashboard, text="Directions", bg='black', fg='white', command=directions, font=('Calibri', 12), width=30).grid(row=6,sticky=N,padx=10)
    Button(User_dashboard, text='Screen on/off', bg='black', fg='white', font=('Calibri', 12), width=20, command=activate_screen).grid(row=7, sticky=N, pady=10)
    create_data(1, 'on')

def directions():
    global notif
    # Personal Details Screen
    directions_screen = Toplevel(master)
    directions_screen.title('Directions')
    # Buttons
    directions_screen.configure(background='black')
    notif = Label(directions_screen, font=('Calibri', 12))
    notif.grid(row=2, sticky=N, pady=10)
    Button(directions_screen, text="UP", image=UPimage, command=UP).grid(row=0, column=1)
    Button(directions_screen, text="LEFT", image=LEFTimage, command=LEFT).grid(row=1, column=0)
    Button(directions_screen, text="DOWN", image=DOWNimage, command=DOWN).grid(row=1, column=1)
    Button(directions_screen, text="RIGHT", image=RIGHTimage, command=RIGHT).grid(row=1, column=2)

def AppleStock():
    #Vi får fat i aktie data
    #Plot aktie kurven for aktieselskabet
    plt.figure(figsize=(16,8))
    df = web.DataReader('AAPL', data_source='yahoo', start='2019-01-01', end='2021-12-27')
    plt.title('Apple')
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()

def NetflixStock():
    #Vi får fat i aktie data
    #Plot aktie kurven for aktieselskabet
    plt.figure(figsize=(16,8))
    df = web.DataReader('NFLX', data_source='yahoo', start='2019-01-01', end='2021-12-27')
    plt.title('Netflix')
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()

def AmazonStock():
    #Vi får fat i aktie data
    #Plot aktie kurven for aktieselskabet
    plt.figure(figsize=(16,8))
    df = web.DataReader('AMZN', data_source='yahoo', start='2019-01-01', end='2021-12-27')
    plt.title('Amazon')
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()

def FacebookStock():
    #Vi får fat i aktie data
    #Plot aktie kurven for aktieselskabet
    plt.figure(figsize=(16,8))
    df = web.DataReader('FB', data_source='yahoo', start='2019-01-01', end='2021-12-27')
    plt.title('Facebook')
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()

def personal_details():
    #Definere de foskellige columns i databasen som variabler
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    for x in myresult:
        if user_id == x[0]:
            name = x[1]
            lastname = x[2]
            email = x[3]
            password = x[4]

    #Personal Details Screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.configure(background='black')
    #Labels
    Label(personal_details_screen, text="Personal Details", bg='black', fg='white',font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
    Label(personal_details_screen, text="Name: "+name, bg='black', fg='white',font=('Calibri',12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Lastname : " + lastname,  bg='black', fg='white', font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Email : "+email, bg='black', fg='white', font=('Calibri',12)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Password : "+password, bg='black', fg='white', font=('Calibri',12)).grid(row=4, sticky=W)

def UP():
    create_data(2, 'W')
    notif.config(fg="green", text="UP!")
def LEFT():
    create_data(2, 'L')
    notif.config(fg="green", text="LEFT!")
def DOWN():
    create_data(2, 'D')
    notif.config(fg="green", text="DOWN!")
def RIGHT():
    create_data(2, 'R')
    notif.config(fg="green", text="RIGHT!")

def login():
    #variabler
    global temp_login_email
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_email = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.configure(background='black')
    #Labels
    Label(login_screen, text="Login til din account", bg='black', fg='white', font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Email", bg='black', fg='white', font=('Calibri',12)).grid(row=1,sticky=W,pady=10)
    Label(login_screen, text="Password", bg='black', fg='white', font=('Calibri',12)).grid(row=2,sticky=W,pady=10)
    login_notif = Label(login_screen, bg='black', font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_email).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show='*').grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, bg='black', fg='white', width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)

def AllStocks():
    Current_stock = StringVar()
#Personal Details Screen
    AllStocks_screen = Toplevel(master)
    AllStocks_screen.title('All Stocks')
    #Buttons
    AllStocks_screen.configure(background='black')
    Button(AllStocks_screen, text="Apple stock", bg='black', fg='white', image = appleimage, command=AppleStock).grid(row=0,sticky=N, column=0)
    Button(AllStocks_screen, text="Netflix stock", bg='black', fg='white', image = netfliximage, command=NetflixStock).grid(row=0,sticky=N, column=1)
    Button(AllStocks_screen, text="Amazon stock", bg='black', fg='white', image = Amazonimage, command=AmazonStock).grid(row=1,sticky=N, column=0)
    Button(AllStocks_screen, text="Facebook stock", bg='black', fg='white', image = Facebookimage, command=FacebookStock).grid(row=1, sticky=N,column=1)
    Label(AllStocks_screen, text="Company Symbol : ", bg='black', fg='white').grid(row=4, sticky=W)
    Label(AllStocks_screen, text="Stock current value:", bg='black', fg='white').grid(row=6, sticky=W)
    price = 0
    def stock_price():
     
        price = stock_info.get_live_price(e1.get())
        Current_stock.set(price)
        create_data(1, str(price))
 
    result2 = Label(AllStocks_screen, text="", textvariable=Current_stock, bg='black', fg='white').grid(row=6, column=1, sticky=W)
 
    e1 = Entry(AllStocks_screen)
    e1.grid(row=4, column=1)
 
    b = Button(AllStocks_screen, text="Show", bg='black', fg='white', command=stock_price)
    b.grid(row=4, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

#Image import
img = Image.open('6s.jpg')
img = img.resize((400,300))
img = ImageTk.PhotoImage(img)

appleimage = Image.open('apple.png')
appleimage = appleimage.resize((150,150))
appleimage = ImageTk.PhotoImage(appleimage)

netfliximage = Image.open('netflix.png')
netfliximage = netfliximage.resize((150,150))
netfliximage = ImageTk.PhotoImage(netfliximage)

Facebookimage = Image.open('facebook.png')
Facebookimage = Facebookimage.resize((150,150))
Facebookimage = ImageTk.PhotoImage(Facebookimage)

Amazonimage = Image.open('amazon.png')
Amazonimage = Amazonimage.resize((150,150))
Amazonimage = ImageTk.PhotoImage(Amazonimage)

Stocksimage = Image.open('stocks.png')
Stocksimage = Stocksimage.resize((150,150))
Stocksimage = ImageTk.PhotoImage(Stocksimage)


UPimage = Image.open('UP.png')
UPimage = UPimage.resize((150,150))
UPimage = ImageTk.PhotoImage(UPimage)

LEFTimage = Image.open('LEFT.png')
LEFTimage = LEFTimage.resize((150,150))
LEFTimage = ImageTk.PhotoImage(LEFTimage)

DOWNimage = Image.open('DOWN.png')
DOWNimage = DOWNimage.resize((150,150))
DOWNimage = ImageTk.PhotoImage(DOWNimage)

RIGHTimage = Image.open('RIGHT.png')
RIGHTimage = RIGHTimage.resize((150,150))
RIGHTimage = ImageTk.PhotoImage(RIGHTimage)

profilimage = Image.open('white.jpg')
profilimage = profilimage.resize((150,150))
profilimage = ImageTk.PhotoImage(profilimage)


#Labels
Label(master, text = "Group X", bg='black', fg='white', font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Sixth Sense", bg='black', fg='white', font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img, bg='black', fg='white',).grid(row=2,sticky=N,pady=15)


#Buttons
Button(master, text='Register', bg='black', fg='white', font=('Calibri',12), width=20,command=register).grid(row=3,sticky=N)
Button(master, text='Login', bg='black', fg='white', font=('Calibri',12), width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
