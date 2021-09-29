#Import alle de nødvendige moduller
from tkinter import *
from PIL import ImageTk, Image
from pymongo import MongoClient


#Åbner vores gui - Main Screen, og kalder den Bank App 
master = Tk()
master.title('Bank App')

#Funktioner
#Definere funktion for kunde oprettelse
def finish_reg():
    cpr = temp_cpr.get() #Definere variabler, som information som systemet får af kunden ved hjælp af .get() funktion
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()

    if cpr == "" or name == "" or age == "" or gender == "" or password == "": #Sikre kunden udfylder alle felter.
        notif.config(fg="red",text="Please udfyld alle oplysninger * ") #Hvis et af felterne er tomme, skrives dette til kunden
        return
    if collection.find_one({'_id': cpr}): #sikre at kunden ikke allerede eksistere i systemet. Dette gøres ved hjælp af find_one, på id's
        notif.config(fg="red",text="Account eksisterer allerede")
        return
    else:
        #Hvis kunden har udfyldt alle felter, og ikke allerede eksisterer, så oprettes kunden i databasen.
        mydict = {"_id": cpr, "Navn": name, "Alder": age, "Gender": gender, "Password": password, "Balance": "0"}
        collection.insert_one(mydict)
        notif.config(fg="green", text="Bruger oprettet")

#Ny variable defineres som register
def register():
    #Definere variabler som skal bruges på login skærmen
    global temp_cpr
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_cpr = StringVar()
    temp_name = StringVar()
    temp_age =  StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Åbner login skærmen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Laver labels på skærmen
    Label(register_screen, text="Udfyldt dine detaljer her, for at opret dig", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="CPR", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Navn", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Alder", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=4,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',12)).grid(row=5,sticky=W)
    notif = Label(register_screen, font=('Calibri',12))
    notif.grid(row=7,sticky=N,pady=10)    

    #Entries
    Entry(register_screen, textvariable=temp_cpr) .grid(row=1, column=1,padx=5)
    Entry(register_screen, textvariable=temp_name) .grid(row=2, column=1,padx=5)
    Entry(register_screen, textvariable=temp_age) .grid(row=3, column=1,padx=5)
    Entry(register_screen, textvariable=temp_gender) .grid(row=4, column=1,padx=5)
    Entry(register_screen, textvariable=temp_password,show="*") .grid(row=5, column=1,padx=5)

    #Opretter en knap som hedder "Registrer"
    Button(register_screen, text="Registrer", command = finish_reg, font=('Calibri',12)).grid(row=6, sticky=N,pady=10)
    #Definere ny variable for hvis kunden vil logge ind
def login_session():
    global login_cpr
    login_cpr = temp_login_cpr.get()
    login_password = temp_login_password.get()
    #Cpr nummer skal stemme overens med et id, og med Password
    if collection.find_one({'_id': login_cpr}) and collection.find_one({'Password': login_password}):
        #Finder denne kundes navn, ved hjælp af cpr nummer
        name = collection.find_one({'_id': login_cpr}, {'Navn': 1, '_id': 0})
        navn = name['Navn']
        #Åbner en ny skærm efter login er successfuldt 
        login_screen.destroy()
        account_dashboard = Toplevel(master)
        account_dashboard.title('Dashboard')
        #opretter labels på denne skærm
        Label(account_dashboard, text="Account oversigt",font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
        Label(account_dashboard, text="Velkommen "+navn,font=('Calibri',12)).grid(row=1, sticky=N,pady=5)
        #Opretter 3 knapper
        Button(account_dashboard, text="Personlige oplysninger", font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)
        Button(account_dashboard, text="Indsæt", font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
        Button(account_dashboard, text="Hæve", font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)
        Label(account_dashboard).grid(row=5,sticky=N, pady=10)
        return
    else:
        #Hvis login ikke er successfuldt
        login_notif.config(fg="red", text="Ingen bruger fundet med denne kombination *")
def deposit():
    #Definere nye funktioner for deposit
    global bal
    global amount
    global deposit_notif
    global updated_balance
    global current_balance_label
    amount = StringVar()
    #Definere balance column i databasen som en funktion "bal"
    balance = collection.find({'_id': login_cpr}, {'Balance': 1, '_id': 0})
    for bala in balance:
        bal = bala["Balance"]
    #Deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Indsæt penge')
    #Labels
    Label(deposit_screen, text=" ", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Nuværende balance : "+str(bal)+"DKK", font=("Calibri",12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Indsæt beløb : ", font=('Calibri',12)).grid(row=2,sticky=N)
    deposit_notif = Label(deposit_screen, font=('Calibri',12))
    deposit_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(deposit_screen,text='Finish', font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)

def finish_deposit():
    #Sikre at kunden har udfyldt feltet, og at kunden ikke prøver at indsætte 0 eller minus tal
    try:
        if amount.get() == "":
            deposit_notif.config(text='Indsæt et beløb',fg="red")
            return
        if float(amount.get()) <= 0:
            deposit_notif.config(text='Negativt beløb indtastet',fg="red")
            return
    except ValueError:
        deposit_notif.config(text='Indtast et tal',fg="red")
    #Ligger kundens nuværende balance, sammen med kundens nye indsatte penge
    current_balance = bal
    updated_balance = float(current_balance) + float(amount.get())
    #opdatere column balance i databasen, til den nye balance efter indsættelse af penge
    current_balance = collection.update_one({'_id': login_cpr}, {"$set": {'Balance': updated_balance}})

    current_balance_label.config(text="Current Balance : "+str(updated_balance), fg='green')
    deposit_notif.config(text='Balance Updated',fg="green")

def withdraw():
    #Veriabler
    global bal
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    #Definere balance column i databasen som en funktion "bal"
    balance = collection.find({'_id': login_cpr}, {'Balance': 1, '_id': 0})
    for bala in balance:
        bal = bala["Balance"]
    #Deposit screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Hæv penge')
    #Labels
    Label(withdraw_screen, text=" ", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen, text="Nuværende balance : "+str(bal)+"DKK", font=("Calibri",12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Hæv beløb : ", font=('Calibri',12)).grid(row=2,sticky=N)
    withdraw_notif = Label(withdraw_screen, font=('Calibri',12))
    withdraw_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2,column=1)
    #Button
    Button(withdraw_screen,text='Finish', font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)

def finish_withdraw():
    #Sikre at kunden har udfyldt feltet, og at kunden ikke prøver at indsætte 0 eller minus tal
    try:
        if withdraw_amount.get() == "":
            withdraw_notif.config(text='Indsæt et beløb',fg="red")
            return
        if float(withdraw_amount.get()) <= 0:
            withdraw_notif.config(text='Negativt beløb indtastet',fg="red")
            return
        if float(withdraw_amount.get()) > float(bal):
            withdraw_notif.config(text='Du har ikke penge nok', fg='red')
            return
    except ValueError:
        withdraw_notif.config(text='Indtast et tal', fg='red')
    #opdatere column balance i databasen, til den nye balance efter indsættelse af penge
    current_balance = bal
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    current_balance = collection.update_one({'_id': login_cpr}, {"$set": {'Balance': updated_balance}})

    current_balance_label.config(text="Current Balance : "+str(updated_balance), fg='green')
    withdraw_notif.config(text='Balance Updated',fg="green")

def personal_details():
    #Definere de foskellige columns i databasen som variabler
    details_name = collection.find({'_id': login_cpr}, {'Navn': 1, '_id': 0})
    for names in details_name:
       name = names['Navn']
    details_age = collection.find({'_id': login_cpr}, {'Alder': 1, '_id': 0})
    for alder in details_age:
        age = alder['Alder']
    details_gender = collection.find({'_id': login_cpr}, {'Gender': 1, '_id': 0})
    for gender in details_gender:
        gen = gender['Gender']
    details_balance = collection.find({'_id': login_cpr}, {'Balance': 1, '_id': 0})
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
    global temp_login_cpr
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_cpr = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Login til din account", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="CPR", font=('Calibri',12)).grid(row=1,sticky=W,pady=10)
    Label(login_screen, text="Password", font=('Calibri',12)).grid(row=2,sticky=W,pady=10)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_cpr).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show='*').grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)

#Image import
img = Image.open('Secure.png')
img = img.resize((250,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Bank 06", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Sikker Bank", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text='Register', font=('Calibri',12), width=20,command=register).grid(row=3,sticky=N)
Button(master, text='Login', font=('Calibri',12), width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
