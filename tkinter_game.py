from random import randint
from math import fabs
import tkinter as tk
from tkinter import messagebox


def guess_number(number_choice: int) -> int:

    rand_number = randint(1, 100)
    counter = 1

    while number_choice != rand_number:
        counter += 1
        print(f"That's not the number. This is the {counter} try .")
        next_try = int(input('Try again:'))
        if fabs(next_try - rand_number) < fabs(number_choice - rand_number):
            print('Warm')
        else:
            print('Cold')
        number_choice = next_try

    return counter


# you_win = guess_number(int(input('Guess what number was drawn: ')))
# if you_win > 0:
#     print(f'Congratulations, you guessed it the {you_win} time')


window = tk.Tk()
window.title('Play the game.')

label = tk.Label(window, text='Guess the drawn number!')
label.pack()

number = tk.Entry()
number.pack()

button = tk.Button(text="Check!", command=guess_number)
button.pack()

window.mainloop()
