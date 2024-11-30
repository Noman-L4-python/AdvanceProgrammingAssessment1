import tkinter as tk
import random

def loadJokes(path):
    with open(path, 'r') as f:
        return [line.strip().split('?') for line in f if '?' in line]

def tellJoke():
    global currentJoke
    currentJoke = random.choice(jokes)
    jokeLabel.config(text=currentJoke[0] + "?")
    punchlineButton.config(state=tk.NORMAL, text="Show me the punchline!")

def revealPunchline():
    jokeLabel.config(text=currentJoke[1])
    punchlineButton.config(state=tk.DISABLED, text="That's the joke!")

root = tk.Tk()
root.title("Joke Generator")

jokes = loadJokes('RandomJokes.txt')
currentJoke = None

welcomeLabel = tk.Label(root, text="Alexa Tell Me A Joke")
welcomeLabel.pack()

jokeLabel = tk.Label(root, text="")
jokeLabel.pack()

tellJokeButton = tk.Button(root, text="Give me a joke!", command=tellJoke)
tellJokeButton.pack()

punchlineButton = tk.Button(root, text="Show punchline", command=revealPunchline, state=tk.DISABLED)
punchlineButton.pack()

root.mainloop()
