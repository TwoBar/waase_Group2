from tkinter import *
import time
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import cursor
import pandas_datareader as web
import matplotlib.pyplot as plt
from yahoo_fin import stock_info




ui_screen = Tk()

# master.title('Project')
global letter_position


def show_data(dtype, dinput):



    letter_position = 0

    # if position == 5:
    #     position = 1
    dinput_clone = dinput
    for i in range(len(dinput)):
        time.sleep(1)
        dinput = dinput_clone[0+i:4+i]
        letter_position = letter_position + 1
        arrayplotting(dinput, dtype)
def arrayplotting(dinput,dtype) :

    print(dinput)
    x = []
    if dtype == 1:
        dinput = dinput.upper()
        letter_pos = 0
        dinput = list(dinput)

        for i in dinput:
            print(i)

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
    ui_screen.mainloop()
    time.sleep(1)
    ui_screen.destroy()







w = Image.open('white.png')
w = w.resize((50, 50))
w = ImageTk.PhotoImage(w)

b = Image.open('black.png')
b = b.resize((50, 50))
b = ImageTk.PhotoImage(b)

letter = "A"
show_data(1,"fuck")


