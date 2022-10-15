import random
from tkinter import *

first = []
with open('first.txt', 'r') as f1:
    for line in f1:
        firstnames = line.strip()
        first.append(firstnames)

second = []
with open('second.txt', 'r') as f2:
    for line in f2:
        secondnames = line.strip()
        second.append(secondnames)

def generate():
    randname = random.choice(first)+random.choice(first)
    name.delete(0, 'end')
    name.insert('end', randname)

root = Tk()
root.geometry('200x70')
root.resizable(False, False)
root.title('name generator')

title = Label(root, text='name generator')
button = Button(root, text='generate', command=generate)
name = Listbox(root)

title.pack()
button.pack()
name.pack()

root.mainloop()