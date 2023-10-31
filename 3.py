import tkinter as tk
from tkinter import simpledialog
import pickle

class JeopardyGame:
    def __init__(self, root, categories, questions, answers):
        self.root = root
        self.root.title("Silicon Showdown")

        self.categories = categories
        self.prices = ["100", "200", "300", "400", "500"]

        self.player_name = None
        self.load_leaderboard()
        
        self.score_labels = []
        self.scores = {}  # Dictionary to store scores for each player

        self.num_players = 1  # Number of players in the game

        self.questions = questions
        self.answers = answers

        self.active_player = 0

        self.buttons = {}  # To keep track of buttons and their states

        self.create_ui()
        self.show_player_name_dialog()

    def show_player_name_dialog(self):
        self.player_name = simpledialog.askstring("Enter Your Name", "Please enter your name:")
        if self.player_name:
            self.root.title(f"Silicon Showdown - {self.player_name}")

    def create_ui(self):
        for col, category in enumerate(self.categories):
            category_label = tk.Label(self.root, text=category, font=("font2.ttf", 20, "bold"))
            category_label.grid(row=0, column=col)

            for row, price in enumerate(self.prices):
                button = tk.Button(self.root, text=price, font=("font2.ttf", 20, "bold"), width=20, height=4, bg="red", state=tk.NORMAL)
                button.grid(row=row + 1, column=col)
                self.buttons[(col, row)] = button

                # Bind the button to a function
                button.config(command=lambda c=category, p=price: self.show_question(c, p))

        self.score_label = tk.Label(self.root, text="Score: 0", font=("font2.ttf", 25, "bold"))
        self.score_label.grid(row=7, column=0, columnspan=6)

    def show_question(self, category, price):
        if self.active_player is not None:
            if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == tk.NORMAL:
                question = self.questions[category][self.prices.index(price)]
                answer = self.answers[category][self.prices.index(price)]
                player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")

                if player_answer and player_answer.lower() == answer.lower():
                    self.scores[self.active_player] += int(price)
                    self.update_score()
                    self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
                    self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                    self.check_game_over()
                else:
                    self.scores[self.active_player] -= int(price)
                    self.update_score()
                    self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
                    self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                    self.check_game_over()
                self.active_player = None


    # def show_question(self, category, price):
    #         if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == tk.NORMAL:
    #             question = self.questions[category][self.prices.index(price)]
    #             answer = self.answers[category][self.prices.index(price)]
    #             player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")

    #             if player_answer and player_answer.lower() == answer.lower():
    #                 # Correct answer
    #                 self.score += int(price)
    #                 self.update_score()
    #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
    #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #                 self.check_game_over()
    #             else:
    #                 # Incorrect answer
    #                 self.score -= int(price)
    #                 self.update_score()
    #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
    #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #                 self.check_game_over()





    def update_score(self):
        self.score_label.config(text=f"Score: {self.scores[self.active_player]}")

    def check_game_over(self):
        # Check if all questions have been answered
        if all(self.buttons[(col, row)]['state'] == tk.DISABLED for col in range(6) for row in range(5)):
            game_over_label = tk.Label(self.root, text="Game Over!", font=("font2.ttf", 25, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)
            self.show_leaderboard()
            self.save_leaderboard()
            self.root.quit()

    def load_leaderboard(self):
        try:
            with open("leaderboard.pkl", "rb") as file:
                self.leaderboard = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.leaderboard = []

    def save_leaderboard(self):
        self.leaderboard.append((self.player_name, self.scores[self.active_player]))
        self.leaderboard.sort(key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:10]  # Keep only the top 10 scores
        with open("leaderboard.pkl", "wb") as file:
            pickle.dump(self.leaderboard, file)

    def show_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.root)
        leaderboard_window.title("Leaderboard")

        tk.Label(leaderboard_window, text="Top 10 Scores", font=("font2.ttf", 20, "bold")).pack()

        player_score = self.scores[self.active_player]
        leaderboard_position = self.leaderboard.index((self.player_name, player_score)) + 1 if (self.player_name, player_score) in self.leaderboard else "N/A"

        tk.Label(leaderboard_window, text=f"You finished in position {leaderboard_position}", font=("font2.ttf", 16)).pack()

        if self.leaderboard:
            for i, (name, score) in enumerate(self.leaderboard):
                tk.Label(leaderboard_window, text=f"{i+1}. {name}: {score}", font=("font2.ttf", 16)).pack()
        else:
            tk.Label(leaderboard_window, text="No scores yet.", font=("font2.ttf", 16)).pack()

def main():
    root = tk.Tk()
    root.geometry('1920x1080')

    custom_categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]

    questions = {
        "Category 1": ["Question 1-1", "Question 1-2", "Question 1-3", "Question 1-4", "Question 1-5"],
        "Category 2": ["Question 2-1", "Question 2-2", "Question 2-3", "Question 2-4", "Question 2-5"],
        "Category 3": ["Question 3-1", "Question 3-2", "Question 3-3", "Question 3-4", "Question 3-5"],
        "Category 4": ["Question 4-1", "Question 4-2", "Question 4-3", "Question 4-4", "Question 4-5"],
        "Category 5": ["Question 5-1", "Question 5-2", "Question 5-3", "Question 5-4", "Question 5-5"],
        "Category 6": ["Question 6-1", "Question 6-2", "Question 6-3", "Question 6-4", "Question 6-5"]
    }

    answers = {
        "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
        "Category 2": ["Answer 2-1", "Answer 2-2", "Answer 2-3", "Answer 2-4", "Answer 2-5"],
        "Category 3": ["Answer 3-1", "Answer 3-2", "Answer 3-3", "Answer 3-4", "Answer 3-5"],
        "Category 4": ["Answer 4-1", "Answer 4-2", "Answer 4-3", "Answer 4-4", "Answer 4-5"],
        "Category 5": ["Answer 5-1", "Answer 5-2", "Answer 5-3", "Answer 5-4", "Answer 5-5"],
        "Category 6": ["Answer 6-1", "Answer 6-2", "Answer 6-3", "Answer 6-4", "Answer 6-5"]
    }

    game = JeopardyGame(root, custom_categories, questions, answers)

    root.mainloop()

if __name__ == "__main__":
    main()
