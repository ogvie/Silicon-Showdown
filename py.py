from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
import customtkinter

mycolour = "#383434"
mycolour2 = "#ececec"

# from tkinter.font import Font
# from tkinter.ttk import *
# import ttkbootstrap as tb

# root = tb.Window(themename="darkly")
root = Tk()
root.geometry('1920x1080')
root.configure(bg=mycolour)
# root.eval('tk::PlaceWindow . center')

# bluestyle = tb.Style()
# bluestyle.configure("blue.TButton", font=("font.ttf", 20), background="red")

# bluestyle = Style()
# bluestyle.configure("blue.TButton", font=("font2.ttf", 20), foreground="white", background="blue")

class JeopardyGame:
    def __init__(self, root, categories, questions, answers):
        self.root = root
        self.root.title("Silicon Showdown")

        self.categories = categories
        self.prices = ["100", "200", "300", "400", "500"]

        self.score_label = Label(self.root, text="Score: 0", font=("font2.ttf", 25, "bold"))
        self.score_label.grid(row=7, column=0, columnspan=6)

        self.questions = questions
        self.answers = answers

        # self.questions = {
        #     "Category 1": ["Question 1-1", "Question 1-2", "Question 1-3", "Question 1-4", "Question 1-5"],
        #     "Category 2": ["Question 2-1", "Question 2-2", "Question 2-3", "Question 2-4", "Question 2-5"],
        #     "Category 3": ["Question 3-1", "Question 3-2", "Question 3-3", "Question 3-4", "Question 3-5"],
        #     "Category 4": ["Question 4-1", "Question 4-2", "Question 4-3", "Question 4-4", "Question 4-5"],
        #     "Category 5": ["Question 5-1", "Question 5-2", "Question 5-3", "Question 5-4", "Question 5-5"],
        #     "Category 6": ["Question 6-1", "Question 6-2", "Question 6-3", "Question 6-4", "Question 6-5"]
        # }

        # self.answers = {
        #     "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
        #     "Category 2": ["Answer 2-1", "Answer 2-2", "Answer 2-3", "Answer 2-4", "Answer 2-5"],
        #     "Category 3": ["Answer 3-1", "Answer 3-2", "Answer 3-3", "Answer 3-4", "Answer 3-5"],
        #     "Category 4": ["Answer 4-1", "Answer 4-2", "Answer 4-3", "Answer 4-4", "Answer 4-5"],
        #     "Category 5": ["Answer 5-1", "Answer 5-2", "Answer 5-3", "Answer 5-4", "Answer 5-5"],
        #     "Category 6": ["Answer 6-1", "Answer 6-2", "Answer 6-3", "Answer 6-4", "Answer 6-5"]
        # }

        self.score = 0

        self.create_ui()

    def create_ui(self):
        self.buttons = {}  # To keep track of buttons and their states

        for col, category in enumerate(self.categories):
            category_label = Label(self.root, text=category, font=("font2.ttf", 20, "bold"))
            category_label.grid(row=0, column=col)

            for row, price in enumerate(self.prices):
                button = Button(self.root, text=price, font=("font2.ttf", 20, "bold"), width=20, height=4, state=NORMAL)
                button.grid(row=row + 1, column=col)
                self.buttons[(col, row)] = button  # Store the button in a dictionary

                # Bind the button to a function
                button.config(command=lambda c=category, p=price: self.show_question(c, p))

    def show_question(self, category, price):
        if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
            question = self.questions[category][self.prices.index(price)]
            answer = self.answers[category][self.prices.index(price)]
            player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")

            if player_answer and player_answer.lower() == answer.lower():
                # Correct answer
                self.score += int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()
            else:
                # Incorrect answer
                self.score -= int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_game_over(self):
        # Check if all questions have been answered
        if all(self.buttons[(col, row)]['state'] == DISABLED for col in range(6) for row in range(5)):
            game_over_label = Label(self.root, text="Game Over!", font=("font2.ttf", 25, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)

def clear():
    for item in root.winfo_children():
        item.destroy()

def main_menu():
    clear()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # root.rowconfigure(1, weight=1)
    # root.rowconfigure(2, weight=1)
    playbtn = Button(root, text="Play", command=singleplayer, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    optionsbtn = Button(root, text="Options", command=options, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    exitbtn = Button(root, text='Exit', command=root.destroy, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    # playbtn.grid(row=0, column=0)
    # optionsbtn.grid(row=1, column=0)
    # exitbtn.grid(row=2, column=0)
    playbtn.pack(side='top', padx=10, pady=10)
    optionsbtn.pack(side='top', padx=10, pady=10)
    exitbtn.pack(side='top', padx=10, pady=10)

def singlemulti():
    clear()
    singleplayerbtn = Button(root, text="Singleplayer", command=singleplayer, font=("font2.ttf", 40), width=10, height=2)
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)
    singleplayerbtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

def singleplayer():
    clear()
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
    # backbtn = Button(root, text="Back", command=main_menu)
    # backbtn.grid(row=0, column=6)
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=singleplayer)
    backbtn.grid(row=8, column=0, columnspan=6)
    JeopardyGame(root, custom_categories11, questions11, answers11)

def lightmode():
    # customtkinter.disable_macos_darkmode()
    # customtkinter.set_appearance_mode("System")
    root.configure(bg=mycolour2)

def darkmode():
    # customtkinter.enable_macos_darkmode()
    # customtkinter.set_appearance_mode("System")
    root.configure(bg=mycolour)

def options():
    clear()
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # root.rowconfigure(1, weight=1)
    # root.rowconfigure(2, weight=1)
    lightmodebtn = Button(root, text="Light Mode", command=lightmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    darkmodebtn = Button(root, text="Dark Mode", command=darkmode, font=("LEMONMILK-Regular.otf", 40), width=10, height=2)
    backbtn = Button(root, text="Back", font=("font2.ttf", 20), command=main_menu)
    # playbtn.grid(row=0, column=0)
    # optionsbtn.grid(row=1, column=0)
    # exitbtn.grid(row=2, column=0)
    lightmodebtn.pack(side='top', padx=10, pady=10)
    darkmodebtn.pack(side='top', padx=10, pady=10)
    backbtn.pack(side='top', padx=10, pady=10)

main_menu()
root.mainloop()
