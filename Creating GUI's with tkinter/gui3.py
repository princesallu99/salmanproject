__author__ = 'sjaved'
from tkinter import *
import tkinter.messagebox




def main():
    # Create a window
    window = Tk()

    # Create a label
    label1 = Label(window, text='Hello World!')

    # Create a label
    label2 = Label(window, text="I don't like spam!")

    # Create a button
    my_button = Button(window, text='Click Me', command=do_something)

    # Put the labels and button in the window, packed from the top,
    # centered horizontally by default, and expanded to fill the window
    label1.pack(side=TOP, expand=1)
    label2.pack(side=TOP, expand=1)
    my_button.pack(side=TOP, expand=1)

    window.mainloop()


def do_something():
    tkinter.messagebox.showinfo("Message Box", "You clicked the button")


main()