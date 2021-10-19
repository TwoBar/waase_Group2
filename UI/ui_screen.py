from tkinter import *
import time
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import cursor
import pandas_datareader as web
import matplotlib.pyplot as plt
from yahoo_fin import stock_info

master = Tk()
master.title('Project')

def show_data(dtype, dinput):
    if dtype == 1:
        if dinput == 'a' or dinput == 'A':


            x = [w, w, w, w,
                 w, b, b, w,
                 w, w, w, w,
                 w, b, b, w,
                 w, b, b, w]
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
            p17 = x[15]
            p18 = x[17]
            p19 = x[18]
            p20 = x[19]
            screen_plot(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)


def screen_plot(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20):
    ui_screen = Toplevel(master)
    ui_screen.title('Device output')
    # Buttons
    Label(ui_screen, image=p1).grid(row=0, column=0)
    Label(ui_screen,  image=p2).grid(row=0, column=1)
    Label(ui_screen,  image=p3).grid(row=0, column=2)
    Label(ui_screen,  image=p4).grid(row=0, column=3)
    Label(ui_screen, image=p5).grid(row=0, column=4)
    Label(ui_screen, image=p6).grid(row=1, column=0)
    Label(ui_screen, image=p7).grid(row=1, column=1)
    Label(ui_screen, image=p8).grid(row=1, column=2)
    Label(ui_screen, image=p9).grid(row=1, column=3)
    Label(ui_screen, image=p10).grid(row=1, column=4)
    Label(ui_screen, image=p11).grid(row=2, column=0)
    Label(ui_screen, image=p12).grid(row=2, column=1)
    Label(ui_screen, image=p13).grid(row=2, column=2)
    Label(ui_screen, image=p14).grid(row=2, column=3)
    Label(ui_screen, image=p15).grid(row=2, column=4)
    Label(ui_screen, image=p16).grid(row=3, column=0)
    Label(ui_screen, image=p17).grid(row=3, column=1)
    Label(ui_screen, image=p18).grid(row=3, column=2)
    Label(ui_screen, image=p19).grid(row=3, column=3)
    Label(ui_screen, image=p20).grid(row=3, column=4)


w = Image.open('white.png')
w = w.resize((150, 150))
w = ImageTk.PhotoImage(w)

b = Image.open('black.png')
b = b.resize((150, 150))
b = ImageTk.PhotoImage(b)
