# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
master = Tk()
master.title('Bank App')
# creating tkinter window
def Clock():
    master = Toplevel(master)
    lbl = Label(master, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, Clock)
    lbl.pack(anchor = 'center')
 

 
mainloop()