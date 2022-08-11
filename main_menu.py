from tkinter import *
from tkinter import messagebox
from Mazda import Mazda
from Honda import Honda
import os

def coming_soon():
    messagebox.showerror(title="Working in it", message="This feature is coming soon")


def mazda():
    mazda = Mazda('Mazda')
    mazda.export(mazda.read())
    os.system('start "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" "Mazda.xlsx"')

def honda():
    honda = Honda('Honda')
    honda.export(honda.read())
    os.system('start "C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.EXE" "Honda.xlsx"')

geometry = '1080x720'

window = Tk()

window.geometry(geometry)
window.resizable(0,0)
window.title('Cars for Sale!')

# HEAD

head = Frame(window)
head.pack()
mazda_image = PhotoImage(file='Images\Mazda-logo-1997-1920x1080.png')
honda_image = PhotoImage(file='Images\honda-logo-1700x1150.png')
toyata_image = PhotoImage(file='Images\Toyota_logo.png')
ford_image = PhotoImage(file='Images\Ford_Logo_1927.png')

heading = Label(head, text='Cars for Sale!', font=('Times', 20), fg='red', padx=20, pady=10)
heading.pack()
sub_heading = Label(head, text='Select Car', font=('Times', 16), fg='green', padx=10, pady=10)
sub_heading.pack()

# BODY

car_frames = Frame(window)
car_frames.pack()

mazda_button = Button(car_frames, image=mazda_image, command=mazda)
mazda_button.grid(row=0, column=0, padx=150, pady=50)
honda_button = Button(car_frames, image=honda_image, command=honda)
honda_button.grid(row=0, column=1, padx=150)
toyota_button = Button(car_frames, image=toyata_image, command=coming_soon)
toyota_button.grid(row=1, column=0, padx=150, pady=50)
ford_button = Button(car_frames, image=ford_image, command=coming_soon)
ford_button.grid(row=1, column=1, padx=150)

# FOOT

close_button = Button(window, text='Close',font=('Times', 16), command=window.destroy, padx=5, pady=5)
close_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor=SE)

window.mainloop()