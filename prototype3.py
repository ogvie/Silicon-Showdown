from tkinter import *
from tkinter import simpledialog

# Initialize the Tkinter root window
root = Tk()
root.geometry('1920x1080')

# Define a common font for labels and buttons
common_font = ("font2.ttf", 20)

# Class for the Jeopardy game
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
            "Category 2": ["Question 2-1", "Question 2-2", "Question 2-3", "Question 2-4", "Question 2-5"],
            "Category 3": ["Question 3-1", "Question 3-2", "Question 3-3", "Question 3-4", "Question 3-5"],
            "Category 4": ["Question 4-1", "Question 4-2", "Question 4-3", "Question 4-4", "Question 4-5"],
            "Category 5": ["Question 5-1", "Question 5-2", "Question 5-3", "Question 5-4", "Question 5-5"],
            "Category 6": ["Question 6-1", "Question 6-2", "Question 6-3", "Question 6-4", "Question 6-5"]
        }

        self.answers = {
            "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
            "Category 2": ["Answer 2-1", "Answer 2-2", "Answer 2-3", "Answer 2-4", "Answer 2-5"],
            "Category 3": ["Answer 3-1", "Answer 3-2", "Answer 3-3", "Answer 3-4", "Answer 3-5"],
            "Category 4": ["Answer 4-1", "Answer 4-2", "Answer 4-3", "Answer 4-4", "Answer 4-5"],
            "Category 5": ["Answer 5-1", "Answer 5-2", "Answer 5-3", "Answer 5-4", "Answer 5-5"],
            "Category 6": ["Answer 6-1", "Answer 6-2", "Answer 6-3", "Answer 6-4", "Answer 6-5"]
        }

        # Initialize score
        self.score = 0

        self.score_label = Label(self.root, text="Score: 0", font=("font2.ttf", 25, "bold"))
        self.score_label.grid(row=7, column=0, columnspan=6)

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
                # Correct answer: update score and disable the button
                self.score += int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()
            else:
                # Incorrect answer: update score and disable the button
                self.score -= int(price)
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()

    def update_score(self):
        # Update the score label with the current score
        self.score_label.config(text=f"Score: £{self.score}")

    def check_game_over(self):
        # Check if all questions have been answered
        if all(self.buttons[(col, row)]['state'] == DISABLED for col in range(6) for row in range(5)):
            game_over_label = Label(self.root, text="Game Over!", font=("font2.ttf", 25, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)

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
    backbtn = Button(root, text="Return to Main Menu", font=common_font, command=main_menu)
    backbtn.grid(row=8, column=0, columnspan=6)
    JeopardyGame(root)

def options():
    clear()

# Initial call to main menu function
main_menu()

# Start the Tkinter event loop
root.mainloop()
