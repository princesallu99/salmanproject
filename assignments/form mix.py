from tkinter import *
import tkinter.messagebox

__author__ = 'PrinceSallu'

# Create the text field objects
tb_name = StringVar
tb_address = StringVar
tb_city = StringVar
tb_state = StringVar
tb_zip = StringVar

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

    Button(window, bg="White", fg="Black", text="MODIFY", command=modi_info) \
        .grid(row=6, column=4, pady=10)

    window.mainloop()

def add_info():
    global dic
    dic = {'name': tb_name.get(), 'address': tb_address.get(), 'city': tb_city.get(),
           'state': tb_state.get(), 'zip': tb_zip.get()}

def del_info():
    global dic
    dic = {'name': tb_name.get(), 'address': tb_address.get(), 'city': tb_city.get(),
           'state': tb_state.get(), 'zip': tb_zip.get()}
    #delete every keys and values
    dic.clear()
    tkinter.messagebox.showinfo("Address", "Information is successfully deleted")

def find_info():
   dic.get('name': tb_name.get(), 'address': tb_address.get(), 'city': tb_city.get(),
           'state': tb_state.get(), 'zip': tb_zip.get())

def mod_info():
    global dic
    if name in dic:
     dic = {'name': tb_name.get(), 'address': tb_address.get(), 'city': tb_city.get(),
           'state': tb_state.get(), 'zip': tb_zip.get()}

main()