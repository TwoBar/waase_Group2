from tkinter import *
import time

def show_data(dtype, dinput, ui_screenx):
    global ui_screen
    global w
    global b
    global img
    img = PhotoImage()

    ui_screen = ui_screenx

    w = 'white'

    b = 'black'
    letter_position = 0

    if dtype == 1:
        dinput= "     " + dinput + "     :"
        dinput_clone = dinput
        for i in range(len(dinput)-4):
            time.sleep(0.1)
            dinput = dinput_clone[0+i:4+i]
            letter_position = letter_position + 1
            arrayplotting(dinput, dtype)
    if dtype == 3:
        dinput= "     " + dinput + "     :"
        dinput_clone = dinput
        for i in range(len(dinput)-4):
            time.sleep(0.1)
            dinput = dinput_clone[0+i:4+i]
            letter_position = letter_position + 1
            arrayplotting(dinput, dtype)
    elif dtype == 2:
        direction(dinput, dtype, letter_position)

def direction(dinput, dtype, letter_position):

    time.sleep(0.3)
    letter_position = letter_position + 1
    dinput = dinput + str(letter_position)
    print(dinput)
    arrayplotting(dinput, dtype)
    dinput = dinput[0]

    if dinput == 'W' or dinput == 'D':
        if letter_position <= 4:
            direction(dinput, dtype, letter_position)
    if dinput == 'L' or dinput == 'R':
        if letter_position <= 3:
            direction(dinput, dtype, letter_position)

def arrayplotting(dinput,dtype):

    x = []
    if dtype == 1 or dtype == 3:
        dinput = dinput.upper()
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
    elif dtype == 2:
        if dinput[0] == 'W':
            if dinput == 'W1':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            b, b, b, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'W2':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            b, b, b, b,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'W3':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            b, b, b, b,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'W4':
                arraypix = [w, w, w, w,
                            b, b, b, b,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'W5':
                arraypix = [b, b, b, b,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
        elif dinput[0] == 'D':
            if dinput == 'D1':
                arraypix = [b, b, b, b,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'D2':
                arraypix = [w, w, w, w,
                            b, b, b, b,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'D3':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            b, b, b, b,
                            w, w, w, w,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'D4':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            b, b, b, b,
                            w, w, w, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'D5':
                arraypix = [w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            w, w, w, w,
                            b, b, b, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
        elif dinput[0] == 'R':
            if dinput == 'R1':
                arraypix = [w, b, b, b,
                            w, b, b, b,
                            w, b, b, b,
                            w, b, b, b,
                            w, b, b, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'R2':
                arraypix = [b, w, b, b,
                            b, w, b, b,
                            b, w, b, b,
                            b, w, b, b,
                            b, w, b, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'R3':
                arraypix = [b, b, w, b,
                            b, b, w, b,
                            b, b, w, b,
                            b, b, w, b,
                            b, b, w, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'R4':
                arraypix = [b, b, b, w,
                            b, b, b, w,
                            b, b, b, w,
                            b, b, b, w,
                            b, b, b, w]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
        elif dinput[0] == 'L':
            if dinput == 'L1':

                arraypix = [b, b, b, w,
                            b, b, b, w,
                            b, b, b, w,
                            b, b, b, w,
                            b, b, b, w]


                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)

            elif dinput == 'L2':
                arraypix = [b, b, w, b,
                            b, b, w, b,
                            b, b, w, b,
                            b, b, w, b,
                            b, b, w, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'L3':
                arraypix = [b, w, b, b,
                            b, w, b, b,
                            b, w, b, b,
                            b, w, b, b,
                            b, w, b, b]


                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
            elif dinput == 'L4':
                arraypix = [w, b, b, b,
                            w, b, b, b,
                            w, b, b, b,
                            w, b, b, b,
                            w, b, b, b]

                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
                x.extend(arraypix)
        else:
            arrayplotting("   err    ", 1)






    display_output(x)

def display_output(x):


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



    Label(ui_screen, image=img,  width=50, height=50, bg=p1).grid(row=0, column=0)
    Label(ui_screen, image=img,  width=50, height=50, bg=p2).grid(row=0, column=1)
    Label(ui_screen, image=img,  width=50, height=50, bg=p3).grid(row=0, column=2)
    Label(ui_screen, image=img,  width=50, height=50, bg=p4).grid(row=0, column=3)
    Label(ui_screen, image=img,  width=50, height=50, bg=p5).grid(row=1, column=0)
    Label(ui_screen, image=img,  width=50, height=50, bg=p6).grid(row=1, column=1)
    Label(ui_screen, image=img,  width=50, height=50, bg=p7).grid(row=1, column=2)
    Label(ui_screen, image=img,  width=50, height=50, bg=p8).grid(row=1, column=3)
    Label(ui_screen, image=img,  width=50, height=50, bg=p9).grid(row=2, column=0)
    Label(ui_screen, image=img,  width=50, height=50, bg=p10).grid(row=2, column=1)
    Label(ui_screen, image=img,  width=50, height=50, bg=p11).grid(row=2, column=2)
    Label(ui_screen, image=img,  width=50, height=50, bg=p12).grid(row=2, column=3)
    Label(ui_screen, image=img,  width=50, height=50, bg=p13).grid(row=3, column=0)
    Label(ui_screen, image=img,  width=50, height=50, bg=p14).grid(row=3, column=1)
    Label(ui_screen, image=img,  width=50, height=50, bg=p15).grid(row=3, column=2)
    Label(ui_screen, image=img,  width=50, height=50, bg=p16).grid(row=3, column=3)
    Label(ui_screen, image=img,  width=50, height=50, bg=p17).grid(row=4, column=0)
    Label(ui_screen, image=img,  width=50, height=50, bg=p18).grid(row=4, column=1)
    Label(ui_screen, image=img,  width=50, height=50, bg=p19).grid(row=4, column=2)
    Label(ui_screen, image=img,  width=50, height=50, bg=p20).grid(row=4, column=3)

    Label(ui_screen, image=img,  width=50, height=50, bg=p21).grid(row=0, column=4)
    Label(ui_screen, image=img,  width=50, height=50, bg=p22).grid(row=0, column=5)
    Label(ui_screen, image=img,  width=50, height=50, bg=p23).grid(row=0, column=6)
    Label(ui_screen, image=img,  width=50, height=50, bg=p24).grid(row=0, column=7)
    Label(ui_screen, image=img,  width=50, height=50, bg=p25).grid(row=1, column=4)
    Label(ui_screen, image=img,  width=50, height=50, bg=p26).grid(row=1, column=5)
    Label(ui_screen, image=img,  width=50, height=50, bg=p27).grid(row=1, column=6)
    Label(ui_screen, image=img,  width=50, height=50, bg=p28).grid(row=1, column=7)
    Label(ui_screen, image=img,  width=50, height=50, bg=p29).grid(row=2, column=4)
    Label(ui_screen, image=img,  width=50, height=50, bg=p30).grid(row=2, column=5)
    Label(ui_screen, image=img,  width=50, height=50, bg=p31).grid(row=2, column=6)
    Label(ui_screen, image=img,  width=50, height=50, bg=p32).grid(row=2, column=7)
    Label(ui_screen, image=img,  width=50, height=50, bg=p33).grid(row=3, column=4)
    Label(ui_screen, image=img,  width=50, height=50, bg=p34).grid(row=3, column=5)
    Label(ui_screen, image=img,  width=50, height=50, bg=p35).grid(row=3, column=6)
    Label(ui_screen, image=img,  width=50, height=50, bg=p36).grid(row=3, column=7)
    Label(ui_screen, image=img,  width=50, height=50, bg=p37).grid(row=4, column=4)
    Label(ui_screen, image=img,  width=50, height=50, bg=p38).grid(row=4, column=5)
    Label(ui_screen, image=img,  width=50, height=50, bg=p39).grid(row=4, column=6)
    Label(ui_screen, image=img,  width=50, height=50, bg=p40).grid(row=4, column=7)

    Label(ui_screen, image=img,  width=50, height=50, bg=p41).grid(row=0, column=8)
    Label(ui_screen, image=img,  width=50, height=50, bg=p42).grid(row=0, column=9)
    Label(ui_screen, image=img,  width=50, height=50, bg=p43).grid(row=0, column=10)
    Label(ui_screen, image=img,  width=50, height=50, bg=p44).grid(row=0, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p45).grid(row=1, column=8)
    Label(ui_screen, image=img,  width=50, height=50, bg=p46).grid(row=1, column=9)
    Label(ui_screen, image=img,  width=50, height=50, bg=p47).grid(row=1, column=10)
    Label(ui_screen, image=img,  width=50, height=50, bg=p48).grid(row=1, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p49).grid(row=2, column=8)
    Label(ui_screen, image=img,  width=50, height=50, bg=p50).grid(row=2, column=9)
    Label(ui_screen, image=img,  width=50, height=50, bg=p51).grid(row=2, column=10)
    Label(ui_screen, image=img,  width=50, height=50, bg=p52).grid(row=2, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p53).grid(row=3, column=8)
    Label(ui_screen, image=img,  width=50, height=50, bg=p54).grid(row=3, column=9)
    Label(ui_screen, image=img,  width=50, height=50, bg=p55).grid(row=3, column=10)
    Label(ui_screen, image=img,  width=50, height=50, bg=p56).grid(row=3, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p57).grid(row=4, column=8)
    Label(ui_screen, image=img,  width=50, height=50, bg=p58).grid(row=4, column=9)
    Label(ui_screen, image=img,  width=50, height=50, bg=p59).grid(row=4, column=10)
    Label(ui_screen, image=img,  width=50, height=50, bg=p60).grid(row=4, column=11)

    Label(ui_screen, image=img,  width=50, height=50, bg=p61).grid(row=0, column=12)
    Label(ui_screen, image=img,  width=50, height=50, bg=p62).grid(row=0, column=13)
    Label(ui_screen, image=img,  width=50, height=50, bg=p63).grid(row=0, column=14)
    Label(ui_screen, image=img,  width=50, height=50, bg=p64).grid(row=0, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p65).grid(row=1, column=12)
    Label(ui_screen, image=img,  width=50, height=50, bg=p66).grid(row=1, column=13)
    Label(ui_screen, image=img,  width=50, height=50, bg=p67).grid(row=1, column=14)
    Label(ui_screen, image=img,  width=50, height=50, bg=p68).grid(row=1, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p69).grid(row=2, column=12)
    Label(ui_screen, image=img,  width=50, height=50, bg=p70).grid(row=2, column=13)
    Label(ui_screen, image=img,  width=50, height=50, bg=p71).grid(row=2, column=14)
    Label(ui_screen, image=img,  width=50, height=50, bg=p72).grid(row=2, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p73).grid(row=3, column=12)
    Label(ui_screen, image=img,  width=50, height=50, bg=p74).grid(row=3, column=13)
    Label(ui_screen, image=img,  width=50, height=50, bg=p75).grid(row=3, column=14)
    Label(ui_screen, image=img,  width=50, height=50, bg=p76).grid(row=3, column=11)
    Label(ui_screen, image=img,  width=50, height=50, bg=p77).grid(row=4, column=12)
    Label(ui_screen, image=img,  width=50, height=50, bg=p78).grid(row=4, column=13)
    Label(ui_screen, image=img,  width=50, height=50, bg=p79).grid(row=4, column=14)
    Label(ui_screen, image=img,  width=50, height=50, bg=p80).grid(row=4, column=11)


    ui_screen.update()
    x.clear()

