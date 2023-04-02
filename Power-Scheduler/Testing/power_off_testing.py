import os
import time
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter.messagebox import askyesno
import threading

#Backend Section
class Power():
    def __init__(self, hours=None):
        self.hours = hours
        # self.now = datetime.now()
        if not hours is None:
            self.target = datetime.now() + timedelta(hours=float(hours))
        else:
            self.target = None

    def shutdown(self):
        if self.target == None:
            print('You are about to shutdown now!')
        else:
            while datetime.now() < self.target:
                time.sleep(10)
                print('Still have time to shutdown \n', datetime.now())
            if datetime.now() >= self.target:
                print('You are about to shutdown now (2)!')
power = Power()

#Frontend Section
root = Tk()
root.title('Power')
root.configure(bg='light grey')
frame = ttk.Frame(root, padding=50)
frame.grid()

def shutdown_now():
    confirm = askyesno(title='Confirmation!', message='Are you sure want to shutdown now?')
    if confirm:
        # os.system("shutdown /s /t 1")
        # power.shutdown()
        print('Shutdown now')

def schedule_shutdown():
    hour = simpledialog.askfloat(title='How many hours?', prompt='Shutdown after ?? hours? >', parent=root)
    if hour > 0:
        power = Power(hours=hour)
        power.shutdown()

def restart():
    confirm = askyesno(title='Confirmation!', message='Are you sure want to restart now?')
    if confirm:
        # os.system("shutdown /s /t 1")
        # power.restart()
        print('restart now')

def confirm_quit():
    confirm = askyesno(title='Confirmation!', message='Are you sure want to quit?')
    if confirm:
        root.destroy()

ttk.Label(frame, text="Power Off").grid(column=0, row=0)
ttk.Button(frame, text="Shutdown", command=shutdown_now).grid(column=1, row=0)

ttk.Label(frame, text="Auto Power Off").grid(column=0, row=2)
ttk.Button(frame, text="Set Time", command=schedule_shutdown).grid(column=1, row=2)

ttk.Label(frame, text="Restart Now").grid(column=0, row=3)
ttk.Button(frame, text="Restart", command=restart).grid(column=1, row=3)

ttk.Label(frame, text="Quit!").grid(column=0, row=4)
ttk.Button(frame, text="Quit", command=confirm_quit).grid(column=1, row=4)
root.mainloop()









    # while time.gmtime().tm_mday < date:
    #     print('Still have time!')
    #     time.sleep(300)  # wait 5 minutes
    # if time.gmtime().tm_mday >= date and time.gmtime().tm_hour == hour and time.gmtime().tm_min == min:
    #     os.system("shutdown /s /t 1")
    #     time.mktime((2023, 1, 27, ))