#Import alle de nødvendige moduller
from tkinter import *
import time
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import cursor
import pandas_datareader as web
import matplotlib.pyplot as plt
from yahoo_fin import stock_info
from functools import partial

global screen

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


def show_data(dtype, dinput):

    letter_position = 0
    dinput_clone = dinput
    for i in range(len(dinput)-4):
        time.sleep(0.1)
        dinput = dinput_clone[0+i:4+i]
        letter_position = letter_position + 1
        arrayplotting(dinput, dtype)
def arrayplotting(dinput,dtype):

    x = []
    if dtype == 1:
        dinput = dinput.upper()
        letter_pos = 0
        dinput = list(dinput)

        for i in dinput:



            if i == 'A':
                arraypix = [w, b, w, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, w, b, w]

                x.extend(arraypix)


            elif i == 'B':

                arraypix = [b, b, w, w,
                            b, w, b, w,
                            b, b, w, w,
                            b, w, b, w,
                            b, b, w, w]
                x.extend(arraypix)
            elif i == '!':

                arraypix = [w, b, w, w,
                            w, b, w, w,
                            w, b, w, w,
                            w, w, w, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == 'C':

                arraypix = [b, b, b, w,
                            b, w, w, w,
                            b, w, w, w,
                            b, w, w, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == 'D':

                arraypix = [b, b, w, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, b, w, w]
                x.extend(arraypix)
            elif i == 'E':

                arraypix = [b, b, b, w,
                            b, w, w, w,
                            b, b, b, w,
                            b, w, w, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == 'F':

                arraypix = [b, b, b, w,
                            b, w, w, w,
                            b, b, b, w,
                            b, w, w, w,
                            b, w, w, w]
                x.extend(arraypix)
            elif i == 'b':

                arraypix = [w, b, b, w,
                            b, w, w, w,
                            b, w, w, w,
                            b, w, b, w,
                            w, b, b, w]
                x.extend(arraypix)
            elif i == 'H':

                arraypix = [b, w, b, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'I':

                arraypix = [w, b, w, w,
                            w, w, w, w,
                            w, b, w, w,
                            w, b, w, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == 'J':

                arraypix = [w, w, b, w,
                            w, w, b, w,
                            w, w, b, w,
                            b, w, b, w,
                            b, b, w, w]
                x.extend(arraypix)
            elif i == 'K':

                arraypix = [b, w, w, w,
                            b, w, b, w,
                            b, b, w, w,
                            b, w, b, w,
                            b, w, w, w]
                x.extend(arraypix)
            elif i == 'L':

                arraypix = [b, w, w, w,
                            b, w, w, w,
                            b, w, w, w,
                            b, w, w, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == 'M':

                arraypix = [b, w, b, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'N':

                arraypix = [b, w, w, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'O':

                arraypix = [b, b, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == 'P':

                arraypix = [b, b, b, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, w, w,
                            b, w, w, w]
                x.extend(arraypix)
            elif i == 'Q':

                arraypix = [w, b, w, w,
                            b, w, b, w,
                            b, w, b, w,
                            w, b, w, w,
                            w, w, b, w]
                x.extend(arraypix)
            elif i == 'R':

                arraypix = [b, b, b, w,
                            b, w, b, w,
                            b, b, w, w,
                            b, w, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'S':

                arraypix = [w, b, b, w,
                            b, w, w, w,
                            w, b, w, w,
                            w, w, b, w,
                            b, b, w, w]
                x.extend(arraypix)
            elif i == 'T':

                arraypix = [b, b, b, w,
                            w, b, w, w,
                            w, b, w, w,
                            w, b, w, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == 'U':

                arraypix = [b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == 'V':

                arraypix = [b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            w, b, w, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == 'W':

                arraypix = [b, w, b, w,
                            b, w, b, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'X':

                arraypix = [b, w, b, w,
                            b, w, b, w,
                            w, b, w, w,
                            b, w, b, w,
                            b, w, b, w]
                x.extend(arraypix)
            elif i == 'Y':

                arraypix = [Y, w, Y, w,
                            Y, w, Y, w,
                            w, Y, w, w,
                            w, Y, w, w,
                            w, Y, w, w]
                x.extend(arraypix)
            elif i == 'Z':

                arraypix = [b, b, b, w,
                            w, w, b, w,
                            w, b, w, w,
                            b, w, w, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '1':

                arraypix = [w, w, b, w,
                            w, w, b, w,
                            w, w, b, w,
                            w, w, b, w,
                            w, w, b, w]
                x.extend(arraypix)
            elif i == '2':

                arraypix = [b, b, b, w,
                            w, w, b, w,
                            b, b, b, w,
                            b, w, w, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '3':

                arraypix = [b, b, b, w,
                            w, w, b, w,
                            w, b, b, w,
                            w, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '4':

                arraypix = [b, w, w, w,
                            b, w, w, w,
                            b, b, b, w,
                            w, w, b, w,
                            w, w, b, w]
                x.extend(arraypix)
            elif i == '5':

                arraypix = [b, b, b, w,
                            b, w, w, w,
                            b, b, b, w,
                            w, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '6':

                arraypix = [b, b, b, w,
                            b, w, w, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '7':

                arraypix = [b, b, b, w,
                            w, w, b, w,
                            w, w, b, w,
                            w, w, b, w,
                            w, w, b, w]
                x.extend(arraypix)
            elif i == '8':

                arraypix = [b, b, b, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '9':

                arraypix = [b, b, b, w,
                            b, w, b, w,
                            b, b, b, w,
                            w, w, b, w,
                            b, b, b, w]
                x.extend(arraypix)
            elif i == '0':

                arraypix = [w, b, w, w,
                            b, w, b, w,
                            b, b, b, w,
                            b, w, b, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == '.':

                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, b, w, w]
                x.extend(arraypix)
            elif i == ',':

                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, b, w, w,
                            w, b, w, w,
                            b, w, w, w]
                x.extend(arraypix)
            elif i == ':':

                arraypix = [w, w, w, w,
                            w, b, w, w,
                            w, w, w, w,
                            w, b, w, w,
                            w, w, w, w]
                x.extend(arraypix)
            elif i == ' ':

                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w]
                x.extend(arraypix)


    screen_plot_letter_1(x)

def screen_plot_letter_1(x):


    p1 = x[0]
    p2 = x[1]
    p3 = x[2]
    p4 = x[3]
    p5 = x[4]
    p6 = x[5]
    p7 = x[6]
    p8 = x[7]
    p9 = x[8]
    p10 = x[9]
    p11 = x[10]
    p12 = x[11]
    p13 = x[12]
    p14 = x[13]
    p15 = x[14]
    p16 = x[15]
    p17 = x[16]
    p18 = x[17]
    p19 = x[18]
    p20 = x[19]
    p21 = x[20]
    p22 = x[21]
    p23 = x[22]
    p24 = x[23]
    p25 = x[24]
    p26 = x[25]
    p27 = x[26]
    p28 = x[27]
    p29 = x[28]
    p30 = x[29]
    p31 = x[30]
    p32 = x[31]
    p33 = x[32]
    p34 = x[33]
    p35 = x[34]
    p36 = x[35]
    p37 = x[36]
    p38 = x[37]
    p39 = x[38]
    p40 = x[39]
    p41 = x[40]
    p42 = x[41]
    p43 = x[42]
    p44 = x[43]
    p45 = x[44]
    p46 = x[45]
    p47 = x[46]
    p48 = x[47]
    p49 = x[48]
    p50 = x[49]
    p51 = x[50]
    p52 = x[51]
    p53 = x[52]
    p54 = x[53]
    p55 = x[54]
    p56 = x[55]
    p57 = x[56]
    p58 = x[57]
    p59 = x[58]
    p60 = x[59]
    p61 = x[60]
    p62 = x[61]
    p63 = x[62]
    p64 = x[63]
    p65 = x[64]
    p66 = x[65]
    p67 = x[66]
    p68 = x[67]
    p69 = x[68]
    p70 = x[69]
    p71 = x[70]
    p72 = x[71]
    p73 = x[72]
    p74 = x[73]
    p75 = x[74]
    p76 = x[75]
    p77 = x[76]
    p78 = x[77]
    p79 = x[78]
    p80 = x[79]



    Label(ui_screen, image=p1).grid(row=0, column=0)
    Label(ui_screen, image=p2).grid(row=0, column=1)
    Label(ui_screen, image=p3).grid(row=0, column=2)
    Label(ui_screen, image=p4).grid(row=0, column=3)
    Label(ui_screen, image=p5).grid(row=1, column=0)
    Label(ui_screen, image=p6).grid(row=1, column=1)
    Label(ui_screen, image=p7).grid(row=1, column=2)
    Label(ui_screen, image=p8).grid(row=1, column=3)
    Label(ui_screen, image=p9).grid(row=2, column=0)
    Label(ui_screen, image=p10).grid(row=2, column=1)
    Label(ui_screen, image=p11).grid(row=2, column=2)
    Label(ui_screen, image=p12).grid(row=2, column=3)
    Label(ui_screen, image=p13).grid(row=3, column=0)
    Label(ui_screen, image=p14).grid(row=3, column=1)
    Label(ui_screen, image=p15).grid(row=3, column=2)
    Label(ui_screen, image=p16).grid(row=3, column=3)
    Label(ui_screen, image=p17).grid(row=4, column=0)
    Label(ui_screen, image=p18).grid(row=4, column=1)
    Label(ui_screen, image=p19).grid(row=4, column=2)
    Label(ui_screen, image=p20).grid(row=4, column=3)

    Label(ui_screen, image=p21).grid(row=0, column=4)
    Label(ui_screen, image=p22).grid(row=0, column=5)
    Label(ui_screen, image=p23).grid(row=0, column=6)
    Label(ui_screen, image=p24).grid(row=0, column=7)
    Label(ui_screen, image=p25).grid(row=1, column=4)
    Label(ui_screen, image=p26).grid(row=1, column=5)
    Label(ui_screen, image=p27).grid(row=1, column=6)
    Label(ui_screen, image=p28).grid(row=1, column=7)
    Label(ui_screen, image=p29).grid(row=2, column=4)
    Label(ui_screen, image=p30).grid(row=2, column=5)
    Label(ui_screen, image=p31).grid(row=2, column=6)
    Label(ui_screen, image=p32).grid(row=2, column=7)
    Label(ui_screen, image=p33).grid(row=3, column=4)
    Label(ui_screen, image=p34).grid(row=3, column=5)
    Label(ui_screen, image=p35).grid(row=3, column=6)
    Label(ui_screen, image=p36).grid(row=3, column=7)
    Label(ui_screen, image=p37).grid(row=4, column=4)
    Label(ui_screen, image=p38).grid(row=4, column=5)
    Label(ui_screen, image=p39).grid(row=4, column=6)
    Label(ui_screen, image=p40).grid(row=4, column=7)

    Label(ui_screen, image=p41).grid(row=0, column=8)
    Label(ui_screen, image=p42).grid(row=0, column=9)
    Label(ui_screen, image=p43).grid(row=0, column=10)
    Label(ui_screen, image=p44).grid(row=0, column=11)
    Label(ui_screen, image=p45).grid(row=1, column=8)
    Label(ui_screen, image=p46).grid(row=1, column=9)
    Label(ui_screen, image=p47).grid(row=1, column=10)
    Label(ui_screen, image=p48).grid(row=1, column=11)
    Label(ui_screen, image=p49).grid(row=2, column=8)
    Label(ui_screen, image=p50).grid(row=2, column=9)
    Label(ui_screen, image=p51).grid(row=2, column=10)
    Label(ui_screen, image=p52).grid(row=2, column=11)
    Label(ui_screen, image=p53).grid(row=3, column=8)
    Label(ui_screen, image=p54).grid(row=3, column=9)
    Label(ui_screen, image=p55).grid(row=3, column=10)
    Label(ui_screen, image=p56).grid(row=3, column=11)
    Label(ui_screen, image=p57).grid(row=4, column=8)
    Label(ui_screen, image=p58).grid(row=4, column=9)
    Label(ui_screen, image=p59).grid(row=4, column=10)
    Label(ui_screen, image=p60).grid(row=4, column=11)

    Label(ui_screen, image=p61).grid(row=0, column=12)
    Label(ui_screen, image=p62).grid(row=0, column=13)
    Label(ui_screen, image=p63).grid(row=0, column=14)
    Label(ui_screen, image=p64).grid(row=0, column=11)
    Label(ui_screen, image=p65).grid(row=1, column=12)
    Label(ui_screen, image=p66).grid(row=1, column=13)
    Label(ui_screen, image=p67).grid(row=1, column=14)
    Label(ui_screen, image=p68).grid(row=1, column=11)
    Label(ui_screen, image=p69).grid(row=2, column=12)
    Label(ui_screen, image=p70).grid(row=2, column=13)
    Label(ui_screen, image=p71).grid(row=2, column=14)
    Label(ui_screen, image=p72).grid(row=2, column=11)
    Label(ui_screen, image=p73).grid(row=3, column=12)
    Label(ui_screen, image=p74).grid(row=3, column=13)
    Label(ui_screen, image=p75).grid(row=3, column=14)
    Label(ui_screen, image=p76).grid(row=3, column=11)
    Label(ui_screen, image=p77).grid(row=4, column=12)
    Label(ui_screen, image=p78).grid(row=4, column=13)
    Label(ui_screen, image=p79).grid(row=4, column=14)
    Label(ui_screen, image=p80).grid(row=4, column=11)
    ui_screen.update()
    x.clear()


def activate_screen():
    global ui_screen
    global screen
    ui_screen = Toplevel(master)
    screen = 1

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
            Device_dashboard.title('Choose your device')
            Label(Device_dashboard, text="Type your device details in here: ", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
            Label(Device_dashboard, text="Add new Mac Adress:", font=('Calibri',12)).grid(row=1,sticky=N,pady=10)
            Entry(Device_dashboard, textvariable=temp_device) .grid(row=1, column=1,padx=5)

            Button(Device_dashboard, text="Screen", command=activate_screen, font=('Calibri', 12), width=30).grid(row=6,sticky=N, padx=10)
            mycursor.execute("SELECT * FROM device")
            myresult = mycursor.fetchall()
            rownum = 2
            for x in myresult:
                if user_id == x[3]:
                    Button(Device_dashboard, text=x[0], command=partial(userprofil, x[0])).grid(row=rownum, sticky=N, padx=10)
                    rownum = rownum + 1

            Button(Device_dashboard, text="Submit", command=partial(userprofil, '')).grid(row=1, column=2,padx=5)

            show_data(1, '         ')



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
    if dtype == 1 and screen == 1:
        show_data(dtype, '     ' + dinput + '     ')




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

    create_data(1, 'on')
    User_dashboard = Toplevel(master)
    User_dashboard.title('Choose your device')
    Label(User_dashboard, text="Account oversigt",font=('Calibri',12)).grid(row=0, sticky=N,pady=10)
    Label(User_dashboard, text="Velkommen til din profil",font=('Calibri',12)).grid(row=1, sticky=N,pady=5)
    #Button(User_dashboard, text="Profil", image = profilimage,command=personal_details).grid(row=3, sticky=N)
    Button(User_dashboard, text="Stocks",command=AllStocks,font=('Calibri',12),width=30).grid(row=4,sticky=N,padx=10)
    Button(User_dashboard, text="Clock", command=clock,font=('Calibri',12),width=30).grid(row=5,sticky=N,padx=10)
    Button(User_dashboard, text="Directions", command=directions, font=('Calibri', 12), width=30).grid(row=6,sticky=N,padx=10)


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


def UP():
    create_data(2, 'W')
    notif.config(fg="green", text="UP!")

def LEFT():
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('L', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="LEFT!")

def DOWN():
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('D', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
    notif.config(fg="green", text="DOWN!")


def RIGHT():
    query = """Update input_data set input = %s, data_type_ID = %s where user_ID_data = %s"""
    tuple1 = ('R', 2, user_id)
    mycursor.execute(query, tuple1)
    db.commit()
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
        create_data(1, str(price))
 
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

w = Image.open('white.png')
w = w.resize((50, 50))
w = ImageTk.PhotoImage(w)

b = Image.open('black.png')
b = b.resize((50, 50))
b = ImageTk.PhotoImage(b)



#Labels
Label(master, text = "Group x", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Raspberry PI", font=('Calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)


#Buttons
Button(master, text='Register', font=('Calibri',12), width=20,command=register).grid(row=3,sticky=N)
Button(master, text='Login', font=('Calibri',12), width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
