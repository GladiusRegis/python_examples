import tkinter as tk
from tkinter import messagebox


def send_name():
    # print(first_name.get())
    # print('click')
    if first_name.get() == 'Arkadiusz':
        messagebox.showinfo(title='OK', message='Hello!')
    else:
        messagebox.showinfo(title='Something went wrong', message='I do not know you')


window = tk.Tk()
window.title('PyStart')

label = tk.Label(window, text="What's your name?")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()
