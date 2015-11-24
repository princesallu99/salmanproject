__author__ = 'sjaved'

from tkinter import *

# Create the text field objects
annual_interest_rate = StringVar
number_of_years = StringVar
loan_amount = StringVar
monthly_payment = StringVar
total_payment = StringVar


def main():
    # Create a window
    window = Tk()
    window.title("Loan Calculator")

    # Use the grid manager to create labels in column 0
    Label(window, text="Annual Interest Rate").\
        grid(row=1, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="Number of Years").\
        grid(row=2, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="Loan Payment").\
        grid(row=3, column=0, sticky=W, padx="5", pady="2")
    Label(window, text="Monthly Payment", fg="BLUE")\
        .grid(row=4, column=0, sticky=W, padx="5", pady="5")
    Label(window, text="Total Payment", fg="BLUE")\
        .grid(row=5, column=0, sticky=W, padx="5", pady="2")

    # Create text fields in column 1
    global annual_interest_rate
    annual_interest_rate = StringVar()
    Entry(window, textvariable=annual_interest_rate, justify=RIGHT).\
        grid(row=1, column=1, padx="5", pady="2")

    global number_of_years
    number_of_years = StringVar()
    Entry(window, textvariable=number_of_years, justify=RIGHT).\
        grid(row=2, column=1, padx="5", pady="2")

    global loan_amount
    loan_amount = StringVar()
    Entry(window, textvariable=loan_amount, justify=RIGHT).\
        grid(row=3, column=1, padx="5", pady="2")

    global monthly_payment
    monthly_payment = StringVar()
    Entry(window, textvariable=monthly_payment, justify=RIGHT, state="disabled").\
        grid(row=4, column=1, padx="5", pady="5")

    global total_payment
    total_payment = StringVar()
    Entry(window, textvariable=total_payment, justify=RIGHT, state="disabled").\
        grid(row=5, column=1, padx="5", pady="2")

    # Create two buttons in row 6
    Button(window, bg="RED", fg="BLUE", text="Quit",
           command=window.destroy).grid(row=6, column=0, padx=20, pady=10, sticky=W)

    Button(window, bg="GREEN", fg="RED", text="Calculate", command=payment_calc)\
        .grid(row=6, column=1, padx=20, pady=10, sticky=E)

    window.mainloop()


def payment_calc():
    # Calculate the monthly payment and put it in the text field
    monthly_pay = get_monthly_payment(
        float(loan_amount.get()),
        float(annual_interest_rate.get()) / 1200,
        int(number_of_years.get()))
    monthly_payment.set(format(monthly_pay, "10.2f"))

    # Calculate the total payment and put it in the text field
    total = float(monthly_payment.get()) * 12 * int(number_of_years.get())
    total_payment.set(format(total, "10.2f"))


def get_monthly_payment(loan_amt, monthly_rate, years):
        return loan_amt * monthly_rate / (1 - 1 / (1 + monthly_rate) ** (years * 12))


main()

