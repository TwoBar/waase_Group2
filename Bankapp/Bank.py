#Import alle de nødvendige moduller
from tkinter import *
import time
from PIL import ImageTk, Image
from pymongo import MongoClient
import pandas_datareader as web
import matplotlib.pyplot as plt
from yahoo_fin import stock_info

#Connecter til mongodb
client = MongoClient("mongodb+srv://Victor:Skole@cluster0.ujn2z.mongodb.net/bank?retryWrites=true&w=majority")
#Connecter til database Kunder, hvis den ikke eksistere, opretter den en ny
db = client["Kunder"]
collection = db["Kunder"]

#Åbner vores gui - Main Screen, og kalder den Bank App 
master = Tk()
master.title('Project')

#Funktioner
#Definere funktion for kunde oprettelse
def finish_reg():
    email = temp_email.get() #Definere variabler, som information som systemet får af kunden ved hjælp af .get() funktion
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()

    if email == "" or name == "" or age == "" or gender == "" or password == "": #Sikre kunden udfylder alle felter.
        notif.config(fg="red",text="Please udfyld alle oplysninger * ") #Hvis et af felterne er tomme, skrives dette til kunden
        return
    if collection.find_one({'_id': email}): #sikre at kunden ikke allerede eksistere i systemet. Dette gøres ved hjælp af find_one, på id's
        notif.config(fg="red",text="Account eksisterer allerede")
        return
    else:
        #Hvis kunden har udfyldt alle felter, og ikke allerede eksisterer, så oprettes kunden i databasen.
        mydict = {"_id": email, "Navn": name, "Alder": age, "Gender": gender, "Password": password, "Balance": "0"}
        collection.insert_one(mydict)
        notif.config(fg="green", text="Bruger oprettet")

#Ny variable defineres som register
def register():
    #Definere variabler som skal bruges på login skærmen
    global temp_email
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_email = StringVar()
    temp_name = StringVar()
    temp_age =  StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Åbner login skærmen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Laver labels på skærmen
    Label(register_screen, text="Udfyldt dine detaljer her, for at opret dig", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Email", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Navn", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Alder", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=4,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=5,sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=7,sticky=N,pady=10)    

    #Entries
    Entry(register_screen, textvariable=temp_email) .grid(row=1, column=1,padx=5)
    Entry(register_screen, textvariable=temp_name) .grid(row=2, column=1,padx=5)
    Entry(register_screen, textvariable=temp_age) .grid(row=3, column=1,padx=5)
    Entry(register_screen, textvariable=temp_gender) .grid(row=4, column=1,padx=5)
    Entry(register_screen, textvariable=temp_password,show="*") .grid(row=5, column=1,padx=5)

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
    


def login_session():
    global login_email
    login_email = temp_login_email.get()
    login_password = temp_login_password.get()
    #Cpr nummer skal stemme overens med et id, og med Password
    if collection.find_one({'_id': login_email}) and collection.find_one({'Password': login_password}):
        #Finder denne kundes navn, ved hjælp af cpr nummer
        name = collection.find_one({'_id': login_email}, {'Navn': 1, '_id': 0})
        navn = name['Navn']
        #Åbner en ny skærm efter login er successfuldt 
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Dashboard')
        #opretter labels på denne skærm
        Label(account_dashboard, text="Account oversigt",font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
        Label(account_dashboard, text="Velkommen "+navn,font=('Calibri',12)).grid(row=1, sticky=N,pady=5)
        #Opretter 3 knapper
        Button(account_dashboard, text="Profil", image = profilimage,command=personal_details).grid(row=3, sticky=N)
        Button(account_dashboard, text="Stocks",command=AllStocks,font=('Calibri',12),width=30).grid(row=4,sticky=N,padx=10)
        Button(account_dashboard, text="Clock", command=clock,font=('Calibri',12),width=30).grid(row=5,sticky=N,padx=10)
        return
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

def personal_details():
    #Definere de foskellige columns i databasen som variabler
    details_name = collection.find({'_id': login_email}, {'Navn': 1, '_id': 0})
    for names in details_name:
       name = names['Navn']
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

#Labels
Label(master, text = "Group x", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Raspberry PI", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)


#Buttons
Button(master, text='Register', font=('Calibri',12), width=20,command=register).grid(row=3,sticky=N)
Button(master, text='Login', font=('Calibri',12), width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
