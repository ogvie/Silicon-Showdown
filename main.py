from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import customtkinter

mycolour = "#383434"
mycolour2 = "#ececec"
mycolour3 = "#FF6961"
mycolour4 = "77DD77"

root = Tk()
root.geometry('2560x1440')
root.configure(bg=mycolour)
root.title("Silicon Showdown")

class SiliconShowdown:
    def __init__(self, root, categories, questions, answers):
        self.root = root
        self.root.title("Silicon Showdown - In Game")

        self.categories = categories
        self.prices = ["100", "200", "300", "400", "500"]

        self.score_label = Label(self.root, text="Score: 0", font=("font2.ttf", 25, "bold"))
        self.score_label.grid(row=7, column=0, columnspan=6)

        self.questions = questions
        self.answers = answers

        self.score = 0

        self.create_ui()

    def create_ui(self):
        self.buttons = {}

        for col, category in enumerate(self.categories):
            category_label = Label(self.root, text=category, font=("font2.ttf", 20, "bold"))
            category_label.grid(row=0, column=col)

            for row, price in enumerate(self.prices):
                button = Button(self.root, text=price, font=("font2.ttf", 20, "bold"), width=20, height=4, state=NORMAL)
                button.grid(row=row + 1, column=col)
                self.buttons[(col, row)] = button

                button.config(command=lambda c=category, p=price: self.show_question(c, p))

    def show_question(self, category, price):
        if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
            question = self.questions[category][self.prices.index(price)]
            answer = self.answers[category][self.prices.index(price)]
            player_answer = simpledialog.askstring("Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")

            if player_answer and player_answer.lower() == answer.lower():
                self.score += int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'mycolour4'
                self.check_game_over()
            else:
                self.score -= int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'mycolour3'
                self.check_game_over()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_game_over(self):
        if all(self.buttons[(col, row)]['state'] == DISABLED for col in range(6) for row in range(5)):
            game_over_label = Label(self.root, text="Game Over!", font=("font2.ttf", 25, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)

def clear():
    for item in root.winfo_children():
        item.destroy()

def main_menu():
    clear()

    root.title("Silicon Showdown - Main Menu")

    playbtn = Button(root, text="Play", command=topicselector, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    optionsbtn = Button(root, text="Options", command=options, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    aboutbtn = Button(root, text="About", command=about, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    exitbtn = Button(root, text='Exit', command=root.destroy, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
 
    playbtn.pack(side='top', padx=10, pady=10)
    optionsbtn.pack(side='top', padx=10, pady=10)
    aboutbtn.pack(side='top', padx=10, pady=10)
    exitbtn.pack(side='top', padx=10, pady=10)

def topicselector():
    clear()

    root.title("Silicon Showdown - Topic Selector")

    oneonebtn = Button(root, text="1.1 - Processors and Storage Devices", command=oneone, font=("font2.ttf", 40))
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)
    
    oneonebtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def oneone():
    clear()

    custom_categories11 = ["Processor Basics", "Processor Types", "Computer Architecture", "I/O Devices", "Storage Devices", "Memory",]

    questions11 = {
        "Processor Basics": ["Are registers part of the processor?", "What does the F in FDE Cycle stand for?", "The higher the clock speed, the ______ instructions are carried out", "The accumulator ___________ stores data while instructions or calculations are being carried out.", "Pipelining improves __________."],
        "Processor Types": ["What does CISC stand for?", "Between CISC and RISC, which consumes less power?", "GPUs can be used for ________ processing.", "Are parallelism and concurrency the same thing?", "Does double the number of cores mean double the performance?"],
        "Computer Architecture": ["Out of Von Neumann and Harvard architecture, which has a simpler operating system?", "Instructions and data stored in separate memory units in _______ architecture.", "Von Neumann architecture uses the same _______ bus and data bus.", "Reading and writing data can be done at the same time as fetching an instruction in which architecture?", "Does contemporary processing use only Von Neumann architecture?"],
        "I/O Devices": ["Are speakers an input or output device?", "Can a device be both input and output?", "Is a microphone an input or output device?", "Is a monitor an input or output device?", "Is a touch screen an input or output device?"],
        "Storage Devices": ["What does SSD stand for?", "Can you write data to a DVD?", "A hard drive stores data using ________ storage.", "What kind of storage are CDs?", "Which type of storage has moving parts?"],
        "Memory": ["Which memory is non-volatile?", "Which is primary memory?", "What does ROM stand for?", "Virtual memory is used when ___ is full.", "Is cache memory faster than RAM?"]
    }

    answers11 = {
        "Processor Basics": ["Yes", "Fetch", "faster", "temporarily", "efficiency"],
        "Processor Types": ["Complex instruction set computer", "RISC", "parallel", "No", "No"],
        "Computer Architecture": ["Von Neumann", "harvard", "address", "Harvard", "No"],
        "I/O Devices": ["Output", "Yes", "Input", "Output", "Both"],
        "Storage Devices": ["Solid State Drive", "Yes", "magnetic", "Optical", "Magnetic"],
        "Memory": ["ROM", "RAM", "Read Only Memory", "RAM", "Yes"]
    }

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=topicselector)
    backbtn.grid(row=8, column=0, columnspan=6)

    SiliconShowdown(root, custom_categories11, questions11, answers11)

def lightmode():
    root.configure(bg=mycolour2)

def darkmode():
    root.configure(bg=mycolour)

def options():
    clear()

    root.title("Silicon Showdown - Options")

    lightmodebtn = Button(root, text="Light Mode", command=lightmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    darkmodebtn = Button(root, text="Dark Mode", command=darkmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)

    lightmodebtn.pack(side='top', padx=10, pady=10)
    darkmodebtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def about():
    clear()

    root.title("Silicon Showdown - About")

    about_text = "Silicon Showdown is a trivia quiz game that tests your knowledge of computer science and technology. \n" \
                 "You can choose from various topics and answer questions to earn points. \n" \
                 "The game is designed to be both fun and educational. \n" \
                 "Good luck and enjoy!"

    about_label = Label(root, text=about_text, font=("font2.ttf", 50), wraplength=800, justify="left")
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)

    about_label.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

main_menu()
root.mainloop()