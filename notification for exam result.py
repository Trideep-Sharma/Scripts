from tkinter import ttk
from tkinter import *
import time
import requests
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
def popupmsg(msg):
    popup =Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
while(1):
    a=requests.get('http://www.exam.dtu.ac.in/result.htm').text
    b=a.find('II')
    if(b!=9112):
        popupmsg('Notified')
    time.sleep(1800)


 
