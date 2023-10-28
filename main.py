from tkinter import* 
from tkinter import ttk
import ttkbootstrap as tb

root = Tk()
root.geometry('1920x1080')
root.eval('tk::PlaceWindow . center')


def clear():
    for item in root.winfo_children():
        item. destroy()

def main_menu():

    # Clear screen
    clear()
    # Add new screen
    playbtn = Button(root, text="Play", command=play)
    optionsbtn = Button(root, text="Options")
    exitbtn = Button(root, text='Exit', command=root.destroy)

    playbtn.pack(side='top')
    optionsbtn.pack(side='top')
    exitbtn.pack(side='top')

def play():
    # Clear screen
    clear()

    # Add new screen
    text = Label(root, text="Play!")
    backbtn = Button(root, text="Back", command=main_menu)

    

    text.grid(row=1, column=1)
    backbtn.grid(row=0, column=0)


def options():
    clear()

    lightmodebtn = Button(root, text="Light Mode")



main_menu()
root.mainloop()
