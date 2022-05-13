#!/usr/bin/puthon3

while True:
    value = input("Enter an integer between 1 to 10: ")
    try:
        int_value = int(value)
        if int_value < 0:
            raise Exception("Opps, you entered negative number.")
        elif int_value == 0:
            raise Exception("Opps, you entered zero.")
        elif int_value > 10:
            raise Exception("You did not enter a number between 1 and 10!!!")
    except ValueError:
        print("You did not enter an integer!!!")
    except Exception as error:
        print(error)
    else:
        reciprocal_value = 1 / int_value
        print(f"The Reciprocal of your number is {reciprocal_value}.")
        break
    print("Please, try again.\n")
