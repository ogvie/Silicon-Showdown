from tkinter import *
from tkinter import simpledialog

# Initialize the Tkinter root window
root = Tk()
root.geometry('1920x1080')

# Define a common font for labels and buttons
common_font = ("font2.ttf", 20)

class JeopardyGame:
    def __init__(self, root):
        # Initialize JeopardyGame object
        self.root = root
        self.root.title("Silicon Showdown")

        # Categories and prices for the Jeopardy board
        self.categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]
        self.prices = ["100", "200", "300", "400", "500"]

        # Questions and answers for each category and price
        self.questions = {
            "Category 1": ["Question 1-1", "Question 1-2", "Question 1-3", "Question 1-4", "Question 1-5"],
            # ... (similar entries for other categories)
        }

        self.answers = {
            "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
            # ... (similar entries for other categories)
        }

        # Create the user interface
        self.create_ui()

    def create_ui(self):
        # Create Jeopardy board with buttons
        self.buttons = {}  # To keep track of buttons and their states

        for col, category in enumerate(self.categories):
            category_label = Label(self.root, text=category, font=common_font)
            category_label.grid(row=0, column=col)

            for row, price in enumerate(self.prices):
                button = Button(self.root, text=price, font=common_font, width=20, height=4, state=NORMAL)
                button.grid(row=row + 1, column=col)
                self.buttons[(col, row)] = button  # Store the button in a dictionary

                # Bind the button to a function
                button.config(command=lambda c=category, p=price: self.show_question(c, p))

    def show_question(self, category, price):
        # Display the question and gather user input for an answer
        if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
            question = self.questions[category][self.prices.index(price)]
            answer = self.answers[category][self.prices.index(price)]
            player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: £{price}\n\n{question}\n\nYour Answer:")

            if player_answer and player_answer.lower() == answer.lower():
                # Correct answer: disable the button
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()
            else:
                # Incorrect answer: disable the button)
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'


# Function to clear the root window
def clear():
    for item in root.winfo_children():
        item.destroy()

# Main menu function
def main_menu():
    clear()
    playbtn = Button(root, text="Play", command=play, font=common_font, width=20, height=4)
    optionsbtn = Button(root, text="Options", font=common_font, width=20, height=4)
    exitbtn = Button(root, text='Exit', command=root.destroy, font=common_font, width=20, height=4)
    playbtn.pack(side='top', padx=10, pady=10)
    optionsbtn.pack(side='top', padx=10, pady=10)
    exitbtn.pack(side='top', padx=10, pady=10)

# Play function to initialize JeopardyGame
def play():
    clear()
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
    backbtn = Button(root, text="Back", font=common_font, command=main_menu)
    backbtn.grid(row=8, column=0, columnspan=6)
    JeopardyGame(root)

def options():
    clear()

# Initial call to main menu function
main_menu()

# Start the Tkinter event loop
root.mainloop()
