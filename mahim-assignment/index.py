#!/usr/bin/python3
from tkinter import *

banks = [
    {
        "name": "Standard Chartered Bank",
        "interestRate": 4,
        "compoundingPeriods": 3
    },
    {
        "name": "Brac Bank",
        "interestRate": 3,
        "compoundingPeriods": 4
    },
    {
        "name": "City Bank",
        "interestRate": 5,
        "compoundingPeriods": 6
    },
]


def calculateBalance(depositedAmount, interestRate, compoundedTimes):
    value = 1 + (interestRate / 100) / compoundedTimes
    interest = 1
    while compoundedTimes > 0:
        interest = interest * value
        compoundedTimes = compoundedTimes - 1
    balance = depositedAmount * interest
    return round(balance, 2)


def calculateAnnualPercentageYield(interestRate, compoundedTimes):
    value = 1 + (interestRate / 100) / compoundedTimes
    interest = 1
    while compoundedTimes > 0:
        interest = interest * value
        compoundedTimes = compoundedTimes - 1
    APY = interest - 1
    return APY


def showBankInterestRates():
    inputFile = open('Input.txt', 'r')
    lines = inputFile.readlines()
    for line in lines:
        print(line, end="")
    inputFile.close()


def writeFile(message):
    outputFile = open('Output.txt', 'w')
    outputFile.writelines(message)
    outputFile.close()


def getFavourableBank():
    APY = []
    favourableBank = {}
    for bank in banks:
        currentAPY = calculateAnnualPercentageYield(bank['interestRate'], bank['compoundingPeriods'])
        APY.append(currentAPY)

    if APY[0] > APY[1]:
        if APY[0] > APY[2]:
            favourableBank = banks[0]
        else:
            favourableBank = banks[2]
    elif APY[0] > APY[2]:
        if APY[0] > APY[1]:
            favourableBank = banks[0]
        else:
            favourableBank = banks[1]
    return favourableBank


def getDepositedAmountFromUser():
    menuMessage = "Please enter your deposited amount:\n"
    return int(input(menuMessage))


def showAllYearEndBalance():
    amount = getDepositedAmountFromUser()
    print(f"Initially deposited amount ${amount}")
    for bank in banks:
        balance = calculateBalance(amount, bank["interestRate"], bank["compoundingPeriods"])
        message = f"Year end balance will be ${balance} in {bank['name']} after one year"
        print(message)
    print("\n")


def showAPY():
    for bank in banks:
        APY = calculateAnnualPercentageYield(bank['interestRate'], bank['compoundingPeriods'])
        message = f"Annual Percentage Yield ${APY} in {bank['name']} after one year"
        print(message)
    print("\n")


def getRecommendedBank():
    bank = getFavourableBank()
    amount = getDepositedAmountFromUser()
    balance = calculateBalance(amount, bank["interestRate"], bank["compoundingPeriods"])
    message = f"Initially deposited amount ${amount}, will result to ${balance} in {bank['name']} after one year"
    print(message)
    writeFile(message)
    print("\n")


def showCommandLineMenu():
    menuMessage = "\n-------------------------------------------------------\nPlease choose your option:\nOption {0}: Show Bank Interest Rate\nOption {1}: Calculate Year End Balance\nOption {2}: Show APY\nOption {3}: Recommended Bank\nOption {4}: Exit\n" \
        .format(1, 2, 3, 4, 0)
    option = int(input(menuMessage))
    while option != 0:
        if option == 1:
            showBankInterestRates()
        elif option == 2:
            showAllYearEndBalance()
        elif option == 3:
            showAPY()
        elif option == 4:
            getRecommendedBank()
        option = int(input(menuMessage))
    print("You have exited", option)


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))


def showGraphicalUserInterface():
    window = Tk()
    window.title("Assignment 4")
    window.geometry('350x200')
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Click Me")
    btn.grid(column=1, row=0)

    # mywin = MyWindow(window)
    # window.title('Hello Python')
    # window.geometry("400x300+10+10")

    window.mainloop()


if __name__ == "__main__":
    # showCommandLineMenu()
    showGraphicalUserInterface()
