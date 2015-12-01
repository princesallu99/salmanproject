from tkinter import *
import tkinter.messagebox

__author__ = 'PrinceSallu'

# Create the text field objects
tb_name = StringVar
tb_address = StringVar
tb_city = StringVar
tb_state = StringVar
tb_Zip = StringVar

# create an empty dictionary
information_form = {}

def main():

    # Create a window
    window = Tk()
    window.title("Information Form")

    # Use the grid manager to create labels in column 0
    Label(window, text="Name"). \
        grid(row=1, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="Address"). \
        grid(row=2, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="City"). \
        grid(row=3, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="State") \
        .grid(row=4, column=0, sticky=W, padx="5", pady="5")
    Label(window, text="Zip") \
        .grid(row=5, column=0, sticky=W, padx="5", pady="2")

    # Create text fields in column 1
    global tb_name
    tb_name = StringVar()
    Entry(window, textvariable=tb_name, justify=RIGHT).grid(row=1, column=2, padx="5", pady="2")

    global tb_address
    tb_address = StringVar()
    Entry(window, textvariable=tb_address, justify=RIGHT). \
        grid(row=2, column=2, padx="5", pady="2")

    global tb_city
    tb_city = StringVar()
    Entry(window, textvariable=tb_city, justify=RIGHT). \
        grid(row=3, column=2, padx="5", pady="2")

    global tb_state
    tb_state = StringVar()
    Entry(window, textvariable=tb_state, justify=RIGHT). \
        grid(row=4, column=2, padx="5", pady="5")

    global tb_zip
    tb_zip = StringVar()
    Entry(window, textvariable=tb_zip, justify=RIGHT). \
        grid(row=5, column=2, padx="5", pady="2")

    # Create five buttons in row 6
    Button(window, bg="White", fg="Black", text="Quit", command=window.destroy) \
        .grid(row=6, column=0, pady=10)

    Button(window, bg="White", fg="Black", text="ADD", command=add_info) \
        .grid(row=6, column=1, pady=11)

    Button(window, bg="White", fg="Black", text="DELETE", command=del_info) \
        .grid(row=6, column=2, pady=12)

    Button(window, bg="White", fg="Black", text="FIND", command=find_info) \
        .grid(row=6, column=3, pady=10)

    Button(window, bg="White", fg="Black", text="MODIFY", command=mod_info) \
        .grid(row=6, column=4, pady=10)

    window.mainloop()


def add_info():
    name = str(tb_name.get())
    address = tb_address.get()
    city = tb_city.get()
    state = tb_state.get()
    zip_code = tb_zip.get()

    # if the information is not exist, add it.
    if name not in information_form:
        information_form[name] = [str(address), str(city), str(state), str(zip_code)]
    else:
        tkinter.messagebox.showinfo("!", "That entry already exists")
    print(information_form)


def del_info(information_form):
    name = input(tb_name)
    address = input(tb_address)
    city = input(tb_city)
    state = input(tb_state)
    zip_code = input(tb_Zip)

    # if the information is found, delete the entry.
    if name in information_form:
        del information_form[name]
    elif address in information_form:
        del information_form[address]
    elif city in information_form:
        del information_form[city]
    elif state in information_form:
        del information_form[state]
    elif zip_code in information_form:
        del information_form[zip_code]
    else:
        tkinter.messagebox.showinfo("!", "That entry is not exists")


def find_info(information_form):
    name = input(tb_name)
    address = input(tb_address)
    city = input(tb_city)
    state = input(tb_state)
    zip_code = input(tb_Zip)
    # find information in dictionary
    information_form.get(name, address, city, state, zip_code)


def mod_info(information_form):
    name = input(tb_name)
    address = input(tb_address)
    city = input(tb_city)
    state = input(tb_state)
    zip_code = input(tb_Zip)

    if name in information_form:
        # get new name
        new_name = input(tb_name)
        # update the name
        information_form[name] = new_name
    elif address in information_form:
        # get new address
        new_address = input(tb_address)
        # update the address
        information_form[address] = new_address
    elif city in information_form:
        # get new city
        new_city = input(tb_city)
        # update the city
        information_form[city] = new_city
    elif state in information_form:
        # get new state
        new_state = input(tb_state)
        # update the state
        information_form[state] = new_state
    elif zip in information_form:
        # get new zip
        new_zip = input(tb_Zip)
        # update the zip
        information_form[zip] = new_zip
    else:
        tkinter.messagebox.showinfo("!", "That entry is not exists")


main()
