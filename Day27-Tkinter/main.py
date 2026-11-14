from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

my_label = Label(text="This is a label text.", font=("Arial", 25, "bold"))
my_label.pack()
my_label.config(text="New text")

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()