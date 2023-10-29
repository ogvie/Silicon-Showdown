# Way number 1
add = lambda x, y: x + y

print(add(1,2))

# from tkinter import* 


# root = Tk()
# root.geometry('1920x1080')
# root.eval('tk::PlaceWindow . center')



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
    backbtn = Button(root, text="Back", command=main_menu)

    backbtn.grid(row=0, column=0)

    JeopardyGame(root)


# def options():
#     clear()

    



# main_menu()
# root.mainloop()



# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     game = 
# #     root.mainloop()

# # import tkinter as tk
# # from tkinter import simpledialog

# # class JeopardyGame:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Silicon Showdown")

# #         self.categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]
# #         self.prices = ["£100", "£200", "£300", "£400", "£500"]

# #         self.questions = {
# #             "Category 1": ["Question 1-1", "Question 1-2", "Question 1-3", "Question 1-4", "Question 1-5"],
# #             "Category 2": ["Question 2-1", "Question 2-2", "Question 2-3", "Question 2-4", "Question 2-5"],
# #             "Category 3": ["Question 3-1", "Question 3-2", "Question 3-3", "Question 3-4", "Question 3-5"],
# #             "Category 4": ["Question 4-1", "Question 4-2", "Question 4-3", "Question 4-4", "Question 4-5"],
# #             "Category 5": ["Question 5-1", "Question 5-2", "Question 5-3", "Question 5-4", "Question 5-5"],
# #             "Category 6": ["Question 6-1", "Question 6-2", "Question 6-3", "Question 6-4", "Question 6-5"]
# #         }

# #         self.answers = {
# #             "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
# #             "Category 2": ["Answer 2-1", "Answer 2-2", "Answer 2-3", "Answer 2-4", "Answer 2-5"],
# #             "Category 3": ["Answer 3-1", "Answer 3-2", "Answer 3-3", "Answer 3-4", "Answer 3-5"],
# #             "Category 4": ["Answer 4-1", "Answer 4-2", "Answer 4-3", "Answer 4-4", "Answer 4-5"],
# #             "Category 5": ["Answer 5-1", "Answer 5-2", "Answer 5-3", "Answer 5-4", "Answer 5-5"],
# #             "Category 6": ["Answer 6-1", "Answer 6-2", "Answer 6-3", "Answer 6-4", "Answer 6-5"]
# #         }

# #         self.score = 0

# #         self.create_ui()

# # # x = ["a", "b", "c"]
# # # for i, j in enumerate(x):
# # #   print(i,j)
# # # 
# # # Output:
# # # 0, "a"
# # # 1, "b"
# # # 2, "c"

# #     def create_ui(self):
# #         self.buttons = {}  # To keep track of buttons and their states

# #         for col, category in enumerate(self.categories):
# #             category_label = tk.Label(self.root, text=category, font=("Arial", 12, "bold"))
# #             category_label.grid(row=0, column=col, padx=10, pady=10)

# #             for row, price in enumerate(self.prices):
# #                 button = tk.Button(self.root, text=price, font=("Arial", 10), width=10, height=2, state=tk.NORMAL)
# #                 button.grid(row= row + 1, column=col, padx=10, pady=10)
# #                 self.buttons[(col, row)] = button  # Store the button in a dictionary

# #                 # Bind the button to a function
# #                 button.config(command=lambda c=category, p=price: self.show_question(c, p))

# #     def show_question(self, category, price):
# #         if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == tk.NORMAL:
# #             question = self.questions[category][self.prices.index(price)]
# #             answer = self.answers[category][self.prices.index(price)]
# #             player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")
            
# #             if player_answer and player_answer.lower() == answer.lower():
# #                 # Correct answer
# #                 self.score += int(price.lstrip('£'))
# #                 self.update_score()
# #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
# #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
# #                 self.check_game_over()

# #     def update_score(self):
# #         score_label.config(text=f"Score: £{self.score}")

# #     def check_game_over(self):
# #         # Check if all questions have been answered
# #         if all(self.buttons[(col, row)]['state'] == tk.DISABLED for col in range(6) for row in range(5)):
# #             game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 20, "bold"), fg="red")
# #             game_over_label.grid(row=6, column=0, columnspan=6)

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     game = JeopardyGame(root)
    
# #     score_label = tk.Label(root, text="Score: £0", font=("Arial", 12, "bold"))
# #     score_label.grid(row=7, column=0, columnspan=6)
    
# #     root.mainloop()


# # import somefile


# # #Imagine this is somefile
# # if __name__ == "__main__":
# #     print("hello")

 from tkinter import* 


# root = Tk()
# root.geometry('1920x1080')
# root.eval('tk::PlaceWindow . center')



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
    backbtn = Button(root, text="Back", command=main_menu)

    backbtn.grid(row=0, column=0)

    JeopardyGame(root)


# def options():
#     clear()

    



# main_menu()
# root.mainloop()



# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     game = 
# #     root.mainloop()

# # import tkinter as tk
# # from tkinter import simpledialog

# # class JeopardyGame:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Silicon Showdown")

# #         self.categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]
# #         self.prices = ["£100", "£200", "£300", "£400", "£500"]

# #         self.questions = {
# #             "Category 1": ["Question 1-1", "Question 1-2", "Question 1-3", "Question 1-4", "Question 1-5"],
# #             "Category 2": ["Question 2-1", "Question 2-2", "Question 2-3", "Question 2-4", "Question 2-5"],
# #             "Category 3": ["Question 3-1", "Question 3-2", "Question 3-3", "Question 3-4", "Question 3-5"],
# #             "Category 4": ["Question 4-1", "Question 4-2", "Question 4-3", "Question 4-4", "Question 4-5"],
# #             "Category 5": ["Question 5-1", "Question 5-2", "Question 5-3", "Question 5-4", "Question 5-5"],
# #             "Category 6": ["Question 6-1", "Question 6-2", "Question 6-3", "Question 6-4", "Question 6-5"]
# #         }

# #         self.answers = {
# #             "Category 1": ["Answer 1-1", "Answer 1-2", "Answer 1-3", "Answer 1-4", "Answer 1-5"],
# #             "Category 2": ["Answer 2-1", "Answer 2-2", "Answer 2-3", "Answer 2-4", "Answer 2-5"],
# #             "Category 3": ["Answer 3-1", "Answer 3-2", "Answer 3-3", "Answer 3-4", "Answer 3-5"],
# #             "Category 4": ["Answer 4-1", "Answer 4-2", "Answer 4-3", "Answer 4-4", "Answer 4-5"],
# #             "Category 5": ["Answer 5-1", "Answer 5-2", "Answer 5-3", "Answer 5-4", "Answer 5-5"],
# #             "Category 6": ["Answer 6-1", "Answer 6-2", "Answer 6-3", "Answer 6-4", "Answer 6-5"]
# #         }

# #         self.score = 0

# #         self.create_ui()

# # # x = ["a", "b", "c"]
# # # for i, j in enumerate(x):
# # #   print(i,j)
# # # 
# # # Output:
# # # 0, "a"
# # # 1, "b"
# # # 2, "c"

# #     def create_ui(self):
# #         self.buttons = {}  # To keep track of buttons and their states

# #         for col, category in enumerate(self.categories):
# #             category_label = tk.Label(self.root, text=category, font=("Arial", 12, "bold"))
# #             category_label.grid(row=0, column=col, padx=10, pady=10)

# #             for row, price in enumerate(self.prices):
# #                 button = tk.Button(self.root, text=price, font=("Arial", 10), width=10, height=2, state=tk.NORMAL)
# #                 button.grid(row= row + 1, column=col, padx=10, pady=10)
# #                 self.buttons[(col, row)] = button  # Store the button in a dictionary

# #                 # Bind the button to a function
# #                 button.config(command=lambda c=category, p=price: self.show_question(c, p))

# #     def show_question(self, category, price):
# #         if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == tk.NORMAL:
# #             question = self.questions[category][self.prices.index(price)]
# #             answer = self.answers[category][self.prices.index(price)]
# #             player_answer = simpledialog.askstring("Jeopardy Question", f"Category: {category}\nPrice: {price}\n\n{question}\n\nYour Answer:")
            
# #             if player_answer and player_answer.lower() == answer.lower():
# #                 # Correct answer
# #                 self.score += int(price.lstrip('£'))
# #                 self.update_score()
# #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = tk.DISABLED
# #                 self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
# #                 self.check_game_over()

# #     def update_score(self):
# #         score_label.config(text=f"Score: £{self.score}")

# #     def check_game_over(self):
# #         # Check if all questions have been answered
# #         if all(self.buttons[(col, row)]['state'] == tk.DISABLED for col in range(6) for row in range(5)):
# #             game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 20, "bold"), fg="red")
# #             game_over_label.grid(row=6, column=0, columnspan=6)

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     game = JeopardyGame(root)
    
# #     score_label = tk.Label(root, text="Score: £0", font=("Arial", 12, "bold"))
# #     score_label.grid(row=7, column=0, columnspan=6)
    
# #     root.mainloop()


# # import somefile


# # #Imagine this is somefile
# # if __name__ == "__main__":
# #     print("hello")


sdfsdfsd
class JeopardyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Silicon Showdown")

        self.categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]
        self.prices = ["£100", "£200", "£300", "£400", "£500"]

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

        self.score = 0

        self.create_ui()

# x = ["a", "b", "c"]
# for i, j in enumerate(x):
#   print(i,j)
# 
# Output:
# 0, "a"
# 1, "b"
# 2, "c"

    def create_ui(self):
        self.buttons = {}  # To keep track of buttons and their states

        for col, category in enumerate(self.categories):
            category_label = Label(self.root, text=category, font=("Arial", 12, "bold"))
            category_label.grid(row=0, column=col, padx=10, pady=10)

            for row, price in enumerate(self.prices):
                button = Button(self.root, text=price, font=("Arial", 10), width=10, height=2, state=tk.NORMAL)
                button.grid(row= row + 1, column=col, padx=10, pady=10)
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
                self.score += int(price.lstrip('£'))
                self.update_score()
                self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
                self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
                self.check_game_over()

    def update_score(self):
        score_label.config(text=f"Score: £{self.score}")

    def check_game_over(self):
        # Check if all questions have been answered
        if all(self.buttons[(col, row)]['state'] == tk.DISABLED for col in range(6) for row in range(5)):
            game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 20, "bold"), fg="red")
            game_over_label.grid(row=6, column=0, columnspan=6)


            # def show_question(self, category, price):
    #     if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
    #         question = self.questions[category][self.prices.index(price)]
    #         answer = self.answers[category][self.prices.index(price)]

    #         # Create a pop-up window for answering the question
    #         question_window = Toplevel(self.root)
    #         question_window.title("Jeopardy Question")

    #         question_label = Label(question_window, text=f"Category: {category}\nPrice: {price}\n\n{question}", font=("Arial", 10))
    #         question_label.pack(padx=10, pady=10)

    #         player_answer = StringVar()
    #         answer_entry = Entry(question_window, textvariable=player_answer)
    #         answer_entry.pack(padx=10, pady=10)

    #         submit_button = Button(question_window, text="Submit", command=lambda c=category, p=price, answer_entry=answer_entry, question_window=question_window: self.check_answer(c, p, answer_entry, question_window))
    #         submit_button.pack(padx=10, pady=10)

    # def check_answer(self, category, price, answer_entry, question_window):
    #     answer = self.answers[category][self.prices.index(price)]
    #     player_answer = answer_entry.get()

    #     if player_answer.lower() == answer.lower():
    #         # Correct answer
    #         self.score += int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #         self.check_game_over()

    #     else:
    #         # Incorrect answer
    #         self.score -= int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'

    #     question_window.destroy()  # Close the question window

    # # ... (the rest of the code)


    # def show_question(self, category, price):
    #     if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
    #         question = self.questions[category][self.prices.index(price)]
    #         answer = self.answers[category][self.prices.index(price)]

    #     # Create a pop-up window for answering the question
    #         question_window = Toplevel(self.root)
    #         question_window.title("Jeopardy Question")

    #         question_label = Label(question_window, text=f"Category: {category}\nPrice: {price}\n\n{question}", font=("Arial", 10))
    #         question_label.pack(padx=10, pady=10)

    #         player_answer = StringVar()
    #         answer_entry = Entry(question_window, textvariable=player_answer)
    #         answer_entry.pack(padx=10, pady=10)
    #         answer_entry.bind("<Return>", lambda event, c=category, p=price, answer_entry=answer_entry, question_window=question_window: self.check_answer(c, p, answer_entry, question_window))

    # def check_answer(self, category, price, answer_entry, question_window):
    #     answer = self.answers[category][self.prices.index(price)]
    #     player_answer = answer_entry.get()

    #     if player_answer.lower() == answer.lower():
    #         # Correct answer
    #         self.score += int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #         self.check_game_over()

    #     else:
    #         # Incorrect answer
    #         self.score -= int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'

    #         question_window.destroy()  # Close the question window


    # def show_question(self, category, price):
    #     if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
    #         question = self.questions[category][self.prices.index(price)]
    #         answer = self.answers[category][self.prices.index(price)]

    #         # Create a pop-up window for answering the question
    #         question_window = Toplevel(self.root)
    #         question_window.title("Jeopardy Question")

    #         question_label = Label(question_window, text=f"Category: {category}\nPrice: {price}\n\n{question}", font=("Arial", 10))
    #         question_label.pack(padx=10, pady=10)

    #         player_answer = StringVar()
    #         answer_entry = Entry(question_window, textvariable=player_answer)
    #         answer_entry.pack(padx=10, pady=10)

    #         submit_button = Button(question_window, text="Submit", command=lambda c=category, p=price, answer_entry=answer_entry, question_window=question_window: self.check_answer(c, p, answer_entry, question_window))
    #         submit_button.pack(padx=10, pady=10)

    # def check_answer(self, category, price, answer_entry, question_window):
    #     answer = self.answers[category][self.prices.index(price)]
    #     player_answer = answer_entry.get()

    #     if player_answer.lower() == answer.lower():
    #         # Correct answer
    #         self.score += int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #         self.check_game_over()

    #     else:
    #         # Incorrect answer
    #         self.score -= int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'

    #     question_window.destroy()  # Close the question window

    # ... (the rest of the code)


    # def show_question(self, category, price):
    #     if self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] == NORMAL:
    #         question = self.questions[category][self.prices.index(price)]
    #         answer = self.answers[category][self.prices.index(price)]

    #         # Create a pop-up window for answering the question
    #         question_window = Toplevel(self.root)
    #         question_window.title("Jeopardy Question")

    #         question_label = Label(question_window, text=f"Category: {category}\nPrice: {price}\n\n{question}", font=("Arial", 10))
    #         question_label.pack(padx=10, pady=10)

    #         player_answer = StringVar()
    #         answer_entry = Entry(question_window, textvariable=player_answer)
    #         answer_entry.pack(padx=10, pady=10)

    #         give_up_button = Button(question_window, text="Give Up", command=lambda: self.give_up(category, price))
    #         give_up_button.pack(padx=10, pady=10)

    #         submit_button = Button(question_window, text="Submit", command=lambda: self.check_answer(category, price, player_answer, question_window))
    #         submit_button.pack(padx=10, pady=10)

    # def give_up(self, category, price):
        
    #     self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #     self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'

    # def check_answer(self, category, price, player_answer, question_window):
    #     answer = self.answers[category][self.prices.index(price)]
        
    #     if player_answer.get().lower() == answer.lower():
    #         # Correct answer
    #         self.score += int(price.lstrip('£'))
    #         self.update_score()
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
    #         self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
    #         self.check_game_over()

    #     question_window.destroy()


    def check_answer(self, category, price, player_answer):
        answer = self.answers[category][self.prices.index(price)]
        
        if player_answer.lower() == answer.lower():
            # Correct answer
            self.score += int(price.lstrip('£'))
            self.update_score()
            self.buttons[(self.categories.index(category), self.prices.index(price))]['state'] = DISABLED
            self.buttons[(self.categories.index(category), self.prices.index(price))]['bg'] = 'gray'
            self.check_game_over()

        question_window.destroy()  # Close the question window

    # ... (the rest of the code)