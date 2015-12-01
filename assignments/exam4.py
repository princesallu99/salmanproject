from tkinter import *
import tkinter.messagebox

__author__ = 'PrinceSallu'

# Create the text field objects
tb_name = StringVar
tb_phone_number = StringVar

# create an empty dictionary
phone_directory = {}


def main():

    # Create a window
    window = Tk()
    window.title("Phone Directory")

    # Use the grid manager to create labels in column 0
    Label(window, text="Name"). \
        grid(row=1, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="Phone Number"). \
        grid(row=2, column=0, sticky=W, padx="5", pady="2")

    # Create text fields in column 1
    global tb_name
    tb_name = StringVar()
    Entry(window, textvariable=tb_name, justify=RIGHT).grid(row=1, column=1, padx="5", pady="2")

    global tb_phone_number
    tb_phone_number = StringVar()
    Entry(window, textvariable=tb_phone_number, justify=RIGHT). \
        grid(row=2, column=1, padx="5", pady="2")


# Create five buttons in row 6
    Button(window, bg="White", fg="Black", text="Quit", command=window.destroy) \
        .grid(row=3, column=0, padx=3, pady=1, sticky=E)

    Button(window, bg="White", fg="Black", text="ADD", command=add_info) \
        .grid(row=3, column=1, padx=3, pady=1, sticky=E)

    Button(window, bg="White", fg="Black", text="DELETE", command=del_info) \
        .grid(row=3, column=2, padx=3, pady=1, sticky=E)

    Button(window, bg="White", fg="Black", text="FIND", command=find_info) \
        .grid(row=3, column=3, padx=3, pady=1, sticky=E)

    Button(window, bg="White", fg="Black", text="MODIFY", command=mod_info) \
        .grid(row=3, column=4, padx=3, pady=1, sticky=E)

    window.mainloop()


def add_info():
    name = str(tb_name.get())
    phone_number = tb_phone_number.get()

    # if the information is not exist, add it.
    if name not in phone_directory:
        phone_directory[name] = [str(phone_number)]
        tkinter.messagebox.showinfo("!", "Entry added")
    else:
        tkinter.messagebox.showinfo("!", "Name already exists")
    print(phone_directory)


def del_info():
    name = str(tb_name.get())
    # if the information is found, delete the entry.
    if name in phone_directory:
        del phone_directory[name]
        tkinter.messagebox.showinfo("!", "Entry deleted")
    else:
        tkinter.messagebox.showinfo("!", "Name not found")
    print(phone_directory)


def find_info():
    name = str(tb_name.get())

    if name in phone_directory:
        # find information in dictionary
        phone_directory.get(name)
    else:
        tkinter.messagebox.showinfo("!", "Name not found")
    print(phone_directory)


def mod_info():
    name = str(tb_name.get())

    if name in phone_directory:
        # get new address
        new_name = str(tb_name.get())
        # update the address
        phone_directory[name] = new_name

        # get new name
        new_phone_number = str(tb_phone_number.get())
        # update the name
        phone_directory[name] = new_phone_number
    else:
        tkinter.messagebox.showinfo("!", "Name not found")


main()
