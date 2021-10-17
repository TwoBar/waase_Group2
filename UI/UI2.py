#Import alle de nødvendige moduller
from tkinter import *
import time
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import cursor
import pandas_datareader as web
import matplotlib.pyplot as plt
from yahoo_fin import stock_info


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

#Funktioner
#Definere funktion for kunde oprettelse
def finish_reg():
    email = temp_email.get() #Definere variabler, som information som systemet får af kunden ved hjælp af .get() funktion
    first_name = temp_firstname.get()
    last_name = temp_lastname.get()
    password = temp_password.get()

    #if email == "" or first_name == "" or last_name == "" or password == "": #Sikre kunden udfylder alle felter.
        #notif.config(fg="red",text="Please udfyld alle oplysninger * ") #Hvis et af felterne er tomme, skrives dette til kunden
        #return
    #if collection.find_one({'email': email}): #sikre at kunden ikke allerede eksistere i systemet. Dette gøres ved hjælp af find_one, på id's
       # notif.config(fg="red",text="Account eksisterer allerede")
        #return
    #else:
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

    #Laver labels på skærmen
    Label(register_screen, text="Udfyldt dine detaljer her, for at opret dig", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Email", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="First name", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Last name", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=7,sticky=N,pady=10)    

    #Entries
    Entry(register_screen, textvariable=temp_email) .grid(row=1, column=1,padx=5)
    Entry(register_screen, textvariable=temp_firstname) .grid(row=2, column=1,padx=5)
    Entry(register_screen, textvariable=temp_lastname) .grid(row=3, column=1,padx=5)
    Entry(register_screen, textvariable=temp_password,show="*") .grid(row=4, column=1,padx=5)

    #Opretter en knap som hedder "Registrer"
    Button(register_screen, text="Registrer", command = finish_reg, font=('Calibri',12)).grid(row=6, sticky=N,pady=10)
    #Definere ny variable for hvis kunden vil logge ind

def clock():
    Clock_screen = Toplevel(master)
    Clock_screen.title('Clock')
    digi_clock = Label(Clock_screen, font=('Calibri',100), bg="red", fg="black")
    def present_time():
        display_time = time.strftime("%H:%M:%S")
        digi_clock.config(text=display_time)
        digi_clock.after(200,present_time)
    present_time()
    digi_clock.pack()


def directions():
    global notif
    # Personal Details Screen
    directions_screen = Toplevel(master)
    directions_screen.title('Directions')
    # Buttons
    notif = Label(directions_screen, font=('Calibri', 12))
    notif.grid(row=2, sticky=N, pady=10)
    Button(directions_screen, text="UP", image=UPimage, command=UP).grid(row=0, column=1)
    Button(directions_screen, text="LEFT", image=LEFTimage, command=LEFT).grid(row=1, column=0)
    Button(directions_screen, text="DOWN", image=DOWNimage, command=DOWN).grid(row=1, column=1)
    Button(directions_screen, text="RIGHT", image=RIGHTimage, command=RIGHT).grid(row=1, column=2)



def login_session():
    global login_email
    global user_id
    login_email = temp_login_email.get()
    login_password = temp_login_password.get()
    #Cpr nummer skal stemme overens med et id, og med Password
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    for x in myresult:
        if login_email == x[3] and login_password == x[4]:
            user_id = x[0]

            #Finder denne kundes navn, ved hjælp af cpr nummer
            #Åbner en ny skærm efter login er successfuldt
            login_screen.destroy()
            account_dashboard = Toplevel(master)
            account_dashboard.title('Dashboard')
            #opretter labels på denne skærm
            Label(account_dashboard, text="Account oversigt",font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
            Label(account_dashboard, text="Velkommen til din profil",font=('Calibri',12)).grid(row=1, sticky=N,pady=5)
            #Opretter 3 knapper
            #Button(account_dashboard, text="Profil", image = profilimage,command=personal_details).grid(row=3, sticky=N)
            Button(account_dashboard, text="Stocks",command=AllStocks,font=('Calibri',12),width=30).grid(row=4,sticky=N,padx=10)
            Button(account_dashboard, text="Clock", command=clock,font=('Calibri',12),width=30).grid(row=5,sticky=N,padx=10)
            Button(account_dashboard, text="Directions", command=directions, font=('Calibri', 12), width=30).grid(row=6, sticky=N, padx=10)
        else:
            #Hvis login ikke er successfuldt
            login_notif.config(fg="red", text="Ingen bruger fundet med denne kombination *")

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

def UP():
    global user_id
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('W', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="UP!")

def LEFT():
    global user_id
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('L', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="LEFT!")

def DOWN():
    global user_id
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('D', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="DOWN!")


def RIGHT():
    global user_id
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('R', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="RIGHT!")

    #def personal_details():
    #Definere de foskellige columns i databasen som variabler
    mycursor.execute("SELECT email FROM user where ")
    myresult = mycursor.fetchall()
    for x in myresult:
        dev = x[0]
    details_age = collection.find({'_id': login_email}, {'Alder': 1, '_id': 0})
    for alder in details_age:
        age = alder['Alder']
    details_gender = collection.find({'_id': login_email}, {'Gender': 1, '_id': 0})
    for gender in details_gender:
        gen = gender['Gender']
    details_balance = collection.find({'_id': login_email}, {'Balance': 1, '_id': 0})
    for balance in details_balance:
        penge = balance['Balance']
    #Personal Details Screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text="Personlige oplysninger",font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
    Label(personal_details_screen, text="Navn : "+name,font=('Calibri',12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Alder : "+age,font=('Calibri',12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Gender : "+gen,font=('Calibri',12)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Balance : "+str(penge)+"DKK",font=('Calibri',12)).grid(row=4, sticky=W)
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
    #Labels
    Label(login_screen, text="Login til din account", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Email", font=('Calibri',12)).grid(row=1,sticky=W,pady=10)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2,sticky=W,pady=10)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_email).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show='*').grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)


def AllStocks():
    Current_stock = StringVar()
#Personal Details Screen
    AllStocks_screen = Toplevel(master)
    AllStocks_screen.title('All Stocks')
    #Buttons
    Button(AllStocks_screen, text="Apple stock", image = appleimage, command=AppleStock).grid(row=0, column=0)
    Button(AllStocks_screen, text="Netflix stock", image = netfliximage, command=NetflixStock).grid(row=0, column=1)
    Button(AllStocks_screen, text="Amazon stock", image = Amazonimage, command=AmazonStock).grid(row=1, column=0)
    Button(AllStocks_screen, text="Facebook stock", image = Facebookimage, command=FacebookStock).grid(row=1, column=1)
    Label(AllStocks_screen, text="Company Symbol : ").grid(row=4, sticky=W)
    Label(AllStocks_screen, text="Stock current value:").grid(row=6, sticky=W)

    def stock_price():
     
        price = stock_info.get_live_price(e1.get())
        Current_stock.set(price)
 
    result2 = Label(AllStocks_screen, text="", textvariable=Current_stock).grid(row=6, column=1, sticky=W)
 
    e1 = Entry(AllStocks_screen)
    e1.grid(row=4, column=1)
 
    b = Button(AllStocks_screen, text="Show", command=stock_price)
    b.grid(row=4, column=2, columnspan=2, rowspan=2, padx=5, pady=5)


#Image import
img = Image.open('raspberry.png')
img = img.resize((250,150))
img = ImageTk.PhotoImage(img)

appleimage = Image.open('apple.png')
appleimage = appleimage.resize((150,150))
appleimage = ImageTk.PhotoImage(appleimage)

netfliximage = Image.open('netflix.png')
netfliximage = netfliximage.resize((150,150))
netfliximage = ImageTk.PhotoImage(netfliximage)

profilimage = Image.open('profil.png')
profilimage = profilimage.resize((50,50))
profilimage = ImageTk.PhotoImage(profilimage)

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

#Labels
Label(master, text = "Group x", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Raspberry PI", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)


#Buttons
Button(master, text='Register', font=('Calibri',12), width=20,command=register).grid(row=3,sticky=N)
Button(master, text='Login', font=('Calibri',12), width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
