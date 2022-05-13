from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          
sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=account).place(x=20,y=10)
sbmibtn=Button(screen,text='Y:Data',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=180,y=10)
sbmibtn=Button(screen,text='Z:Exchange',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=340,y=10)
sbmibtn=Button(screen,text='G:Go To',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=600,y=10)
sbmibtn=Button(screen,text='O:Import',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
sbmibtn=Button(screen,text='E;Export',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
sbmibtn=Button(screen,text='M:E-mail',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
sbmibtn=Button(screen,text='F1:Help',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)

global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850)
Label5 = Label(Canvas1,text='Select Company',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


global Canvas4
Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas4.place(relx=0.330, rely=0.0300, relheight=0.100, relwidth=0.350)
Label6 = Label(Canvas4,text='Select Company',borderwidth="0", width=12, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 12 -weight bold ")
Label6.place(relx=0.35, rely=0.20, relheight=0.30, relwidth=0.300)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.35, rely=0.50, relheight=0.30, relwidth=0.300)


global Canvas2
Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas2.place(relx=0.250, rely=0.300, relheight=0.500, relwidth=0.500)

global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
screen.mainloop()