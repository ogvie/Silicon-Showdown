from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import customtkinter
import requests

mycolour = "#383434"
mycolour2 = "#ececec"
mycolour3 = "#FF6961"
mycolour4 = "77DD77"

root = Tk()
# root.geometry('2560x1440')
root.configure(bg=mycolour)
root.attributes('-fullscreen', True)
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
    eastereggbtn = Button(root, text="???", command=easteregg)

    playbtn.pack(side='top', padx=10, pady=10)
    optionsbtn.pack(side='top', padx=10, pady=10)
    aboutbtn.pack(side='top', padx=10, pady=10)
    exitbtn.pack(side='top', padx=10, pady=10)
    eastereggbtn.pack(side='top')

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

def easteregg():
    clear()

    root.title("Silicon Showdown - ???")

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

    backbtn1 = Button(root, text="Back", command=main_menu)
    backbtn2 = Button(root, text="Back", command=main_menu)
    backbtn3 = Button(root, text="Back", command=main_menu)
    backbtn4 = Button(root, text="Back", command=main_menu)
    backbtn5 = Button(root, text="Back", command=main_menu)
    backbtn6 = Button(root, text="Back", command=main_menu)
    backbtn7 = Button(root, text="Back", command=main_menu)
    backbtn8 = Button(root, text="Back", command=main_menu)
    backbtn9 = Button(root, text="Back", command=main_menu)
    backbtn10 = Button(root, text="Back", command=main_menu)
    backbtn11 = Button(root, text="Back", command=main_menu)
    backbtn12 = Button(root, text="Back", command=main_menu)
    backbtn13 = Button(root, text="Back", command=main_menu)
    backbtn14 = Button(root, text="Back", command=main_menu)
    backbtn15 = Button(root, text="Back", command=main_menu)
    backbtn16 = Button(root, text="Back", command=main_menu)
    backbtn17 = Button(root, text="Back", command=main_menu)
    backbtn18 = Button(root, text="Back", command=main_menu)
    backbtn19 = Button(root, text="Back", command=main_menu)
    backbtn20 = Button(root, text="Back", command=main_menu)
    backbtn21 = Button(root, text="Back", command=main_menu)
    backbtn22 = Button(root, text="Back", command=main_menu)
    backbtn23 = Button(root, text="Back", command=main_menu)
    backbtn24 = Button(root, text="Back", command=main_menu)
    backbtn25 = Button(root, text="Back", command=main_menu)
    backbtn26 = Button(root, text="Back", command=main_menu)
    backbtn27 = Button(root, text="Back", command=main_menu)
    backbtn28 = Button(root, text="Back", command=main_menu)
    backbtn29 = Button(root, text="Back", command=main_menu)
    backbtn30 = Button(root, text="Back", command=main_menu)
    backbtn31 = Button(root, text="Back", command=main_menu)
    backbtn32 = Button(root, text="Back", command=main_menu)
    backbtn33 = Button(root, text="Back", command=main_menu)
    backbtn34 = Button(root, text="Back", command=main_menu)
    backbtn35 = Button(root, text="Back", command=main_menu)
    backbtn36 = Button(root, text="Back", command=main_menu)
    backbtn37 = Button(root, text="Back", command=main_menu)
    backbtn38 = Button(root, text="Back", command=main_menu)
    backbtn39 = Button(root, text="Back", command=main_menu)
    backbtn40 = Button(root, text="Back", command=main_menu)
    backbtn41 = Button(root, text="Back", command=main_menu)
    backbtn42 = Button(root, text="Back", command=main_menu)
    backbtn43 = Button(root, text="Back", command=main_menu)
    backbtn44 = Button(root, text="Back", command=main_menu)
    backbtn45 = Button(root, text="Back", command=main_menu)
    backbtn46 = Button(root, text="Back", command=main_menu)
    backbtn47 = Button(root, text="Back", command=main_menu)
    backbtn48 = Button(root, text="Back", command=main_menu)
    backbtn49 = Button(root, text="Back", command=joke)
    backbtn50 = Button(root, text="Back", command=main_menu)
    backbtn51 = Button(root, text="Back", command=main_menu)
    backbtn52 = Button(root, text="Back", command=main_menu)
    backbtn53 = Button(root, text="Back", command=main_menu)
    backbtn54 = Button(root, text="Back", command=main_menu)

    backbtn1.grid(row=0, column=0)
    backbtn2.grid(row=0, column=1)
    backbtn3.grid(row=0, column=2)
    backbtn4.grid(row=0, column=3)
    backbtn5.grid(row=0, column=4)
    backbtn6.grid(row=0, column=5)

    backbtn7.grid(row=1, column=0)
    backbtn8.grid(row=1, column=1)
    backbtn9.grid(row=1, column=2)
    backbtn10.grid(row=1, column=3)
    backbtn11.grid(row=1, column=4)
    backbtn12.grid(row=1, column=5)

    backbtn13.grid(row=2, column=0)
    backbtn14.grid(row=2, column=1)
    backbtn15.grid(row=2, column=2)
    backbtn16.grid(row=2, column=3)
    backbtn17.grid(row=2, column=4)
    backbtn18.grid(row=2, column=5)

    backbtn19.grid(row=3, column=0)
    backbtn20.grid(row=3, column=1)
    backbtn21.grid(row=3, column=2)
    backbtn22.grid(row=3, column=3)
    backbtn23.grid(row=3, column=4)
    backbtn24.grid(row=3, column=5)

    backbtn25.grid(row=4, column=0)
    backbtn26.grid(row=4, column=1)
    backbtn27.grid(row=4, column=2)
    backbtn28.grid(row=4, column=3)
    backbtn29.grid(row=4, column=4)
    backbtn30.grid(row=4, column=5)

    backbtn31.grid(row=5, column=0)
    backbtn32.grid(row=5, column=1)
    backbtn33.grid(row=5, column=2)
    backbtn34.grid(row=5, column=3)
    backbtn35.grid(row=5, column=4)
    backbtn36.grid(row=5, column=5)

    backbtn37.grid(row=6, column=0)
    backbtn38.grid(row=6, column=1)
    backbtn39.grid(row=6, column=2)
    backbtn40.grid(row=6, column=3)
    backbtn41.grid(row=6, column=4)
    backbtn42.grid(row=6, column=5)

    backbtn43.grid(row=7, column=0)
    backbtn44.grid(row=7, column=1)
    backbtn45.grid(row=7, column=2)
    backbtn46.grid(row=7, column=3)
    backbtn47.grid(row=7, column=4)
    backbtn48.grid(row=7, column=5)

    backbtn49.grid(row=8, column=0)
    backbtn50.grid(row=8, column=1)
    backbtn51.grid(row=8, column=2)
    backbtn52.grid(row=8, column=3)
    backbtn53.grid(row=8, column=4)
    backbtn54.grid(row=8, column=5)

def joke():
    clear()
    joke_text = StringVar()
    joke_label = Label(root, textvariable=joke_text, font=("font2.ttf", 30))
    joke_label.pack(pady=20)

    fetch_button = Button(root, text="Get Joke", command=lambda: fetch_joke(joke_text), font=("LEMONMILK-Regular.otf", 20), width=10, height=2)
    fetch_button.pack()

    backbtn = Button(root, text="Back", command=main_menu, font=("LEMONMILK-Regular.otf", 10), width=5, height=1)
    backbtn.pack(side='top', padx=10, pady=10)

def fetch_joke(joke_text):
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    joke_data = response.json()[0]
    joke_text.set(joke_data['setup'] + '\n' + joke_data['punchline'])

main_menu()
root.mainloop()