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

    # Create a frame to hold the buttons
    frame1 = Frame(window)

    # Create a button, put it in frame1 with horizontal padding
    my_button = Button(frame1, text='Click Me', command=do_something)
    my_button.pack(side=LEFT, padx=10)

    # Create a quit button, put it in frame1 with horizontal padding
    quit_button = Button(frame1, text='QUIT', command=window.destroy)
    quit_button.pack(side=RIGHT, padx=10)

    # Put the labels and frame in the window, packed from the top,
    # centered horizontally by default, and expanded to fill the window
    label1.pack(side=TOP, expand=1)
    label2.pack(side=TOP, expand=1)
    frame1.pack(side=TOP, expand=1)

    window.mainloop()


def do_something():
    tkinter.messagebox.showinfo("Message Box", "You clicked the button")


main()