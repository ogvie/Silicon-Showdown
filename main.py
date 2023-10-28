from tkinter import* 
from tkinter import ttk
import ttkbootstrap as tb
import sv_ttk

root = Tk()
root.geometry('1920x1080')
root.eval('tk::PlaceWindow . center')

sv_ttk

def clear():
    for item in root.winfo_children():
        item. destroy()

def main_menu():

    # Clear screen
    clear()
    sv_ttk.set_theme("dark")
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
    playbtn = Button(root, text="go back", command=main_menu)

    text.pack(side="top")
    playbtn.pack(side='top')



main_menu()
root.mainloop()
