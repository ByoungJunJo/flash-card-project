from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
else:
    words_to_learn_list = []
finally:
    french_dict = df.to_dict(orient="records")

# ---------------------------- CREATE NEW FLASH CARDS ------------------------------- #
def right_button_is_clicked():
    french_dict.remove(word)
    known_words = pd.DataFrame(french_dict)
    known_words.to_csv("data/words_to_learn.csv", index=False)
    create_new_word()

def create_new_word():
    """
    Read the data from the french_words.csv file in the data folder
    Pick a random French word/translation and put the word into the flashcard.
    """
    global word, timer
    window.after_cancel(timer)
    word = random.choice(french_dict)
    french_word = word["French"]
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    # After a delay of 3s (3000ms), the card should flip and display the English translation for the current word
    timer = window.after(3000, show_answer)

def show_answer():
    """
    Read the data from the french_words.csv file in the data folder
    Pick a random French word/translation and put the word into the flashcard.
    """
    answer = word["English"]
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=answer, fill="white")
    canvas.itemconfig(card_img, image=back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, show_answer)

# Canvas for front and back of cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)

# Add text directly on canvas rather than using the Label class
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, columnspan=2)

# Buttons
# Every time you press the ❌ or ✅ buttons, it should generate a new random word to display
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_button_is_clicked)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=create_new_word)
wrong_button.grid(row=1, column=0)

# Call the create new word function to show the word and title right after the program runs
create_new_word()

window.mainloop()