import requests
from tkinter import *

root = Tk()
root.title("Tech Jokes")
root.geometry("400x300")

def fetch_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/random")
    joke_data = response.json()[0]
    joke_text.set(joke_data['setup'] + '\n' + joke_data['punchline'])

joke_text = StringVar()
joke_label = Label(root, textvariable=joke_text, font=("font2.ttf", 16))
joke_label.pack(pady=20)

fetch_button = Button(root, text="Get Joke", command=fetch_joke, font=("font2.ttf", 12))
fetch_button.pack()

root.mainloop()
