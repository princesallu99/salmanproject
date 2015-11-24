__author__ = 'sjaved'
from tkinter import *



def main():
    # Create a window
    window = Tk()

    # Create a label
    label1 = Label(window, text='Hello World!')

    # Create a label
    label2 = Label(window, text="I don't like spam!")

    # Put the labels in the window, packed from the top
    # (centered horizontally by default
    label1.pack(side=TOP)
    label2.pack(side=TOP)

    window.mainloop()


main()
