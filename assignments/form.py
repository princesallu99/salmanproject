__author__ = 'PrinceSallu'
from tkinter import *
import tkinter.messagebox

def main():
    # Create a window
    window = Tk()
    window.title("Information")

    # Put labels in the first row column0
    label_name = Label(window, text="NAME", font=("Helvitica", 16))
    label_name.grid(row=0, column=0, padx="20", pady="5", sticky=W)

    label_address = Label(window, text="ADDRESS", font=("Helvitica", 16))
    label_address.grid(row=1, column=0, padx="20", pady="5", sticky=W)

    label_city = Label(window, text="CITY", font=("Helvitica", 16))
    label_city.grid(row=2, column=0, padx="20", pady="5", sticky=W)

    label_state = Label(window, text="STATE", font=("Helvitica", 16))
    label_state.grid(row=3, column=0, padx="20", pady="5", sticky=W)

    label_nation = Label(window, text="NATION", font=("Helvitica", 16))
    label_nation.grid(row=4, column=0, padx="20", pady="5", sticky=W)

        # Typing the name. create text fields in column 1
    global NAME_VARIABLE
    NAME_VARIABLE = StringVar()
    Entry(window, textvariable=NAME_VARIABLE, justify=RIGHT).\
        grid(row=0, column=1, padx="20", pady="5")

    global ADDRESS_VARIABLE
    ADDRESS_VARIABLE = StringVar()
    Entry(window, textvariable=ADDRESS_VARIABLE, justify=RIGHT).\
        grid(row=1, column=1, padx="20", pady="5")

    global CITY_VARIABLE
    CITY_VARIABLE = StringVar()
    Entry(window, textvariable=CITY_VARIABLE, justify=RIGHT).\
        grid(row=2, column=1, padx="20", pady="5")

    global STATE_VARIABLE
    STATE_VARIABLE = StringVar()
    Entry(window, textvariable=STATE_VARIABLE, justify=RIGHT).\
        grid(row=3, column=1, padx="20", pady="5")

    global NATION_VARIABLE
    NATION_VARIABLE = StringVar()
    Entry(window, textvariable=NATION_VARIABLE, justify=RIGHT).\
        grid(row=4, column=1, padx="20", pady="5")

    # Put three buttons in row 4
    bt_add = Button(window, text="QUIT", bg="RED", fg="GREEN", font=("Helvitica", 10), command=window.destroy)
    bt_add.grid(row=5, column=0, padx=3, pady=1, sticky=E)

    bt_delete = Button(window, text="DELETE", font=("Helvitica", 10), command=DELETE_INFO)
    bt_delete.grid(row=5, column=1, padx=3, pady=1, sticky=E)

    bt_quit = Button(window, text="ADD", font=("Helvitica", 10), command=ADD_INFO )
    bt_quit.grid(row=5, column=4, padx=3, pady=1, sticky=E)

    window.mainloop()

def ADD_INFO():
    global dic
    dic = {'name': NAME_VARIABLE.get(), 'address': ADDRESS_VARIABLE.get(), 'city': CITY_VARIABLE.get(),
           'state': STATE_VARIABLE.get(), 'nation': NATION_VARIABLE.get()}

def DELETE_INFO():
    global dic
    dic = {'name': NAME_VARIABLE.get(), 'address': ADDRESS_VARIABLE.get(), 'city': CITY_VARIABLE.get(),
           'state': STATE_VARIABLE.get(), 'nation': NATION_VARIABLE.get()}
    #delete every keys and values
    dic.clear()
    tkinter.messagebox.showinfo("Address", "Information is successfully deleted")
main()