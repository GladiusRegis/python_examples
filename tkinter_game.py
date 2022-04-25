from random import randint
import tkinter as tk


def guess_number():
    diff = abs(target - int(guess.get()))
    if diff == 0:
        tip.configure(text=f'Congratulations, you guessed it. The result is {len(guesses)}')
        return

    guesses.append(diff)
    if len(guesses) == 1:
        return
    if guesses[-1] > guesses[-2]:
        tip.configure(text='Worm...')
        # odwołanie się do label tip
    if guesses[-1] < guesses[-2]:
        tip.configure(text='Cold...')
    if guesses[-1] == guesses[-2]:
        tip.configure(text='Neither cold nor warm...')

    # print('Zgadula!') # dodajemy aby sprawdzić czy działa


target = randint(1, 50)
print(target)

guesses = []

window = tk.Tk()
window.title('Play the game.')
window.minsize(width=250, height=250)
window.geometry("250x250")

label = tk.Label(window, text='Guess the drawn number!')
label.pack()

guess = tk.Entry(window)
guess.pack()

button = tk.Button(text="Check!", command=guess_number)
button.pack()

tip = tk.Label(window, text='')
tip.pack()

window.mainloop()
