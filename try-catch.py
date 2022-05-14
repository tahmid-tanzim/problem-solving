#!/usr/bin/python3

valid_number_range = list(range(11))
while True:
    value = input("Enter an integer between 1 to 10: ")
    try:
        int_value = int(value)
        valid_int_value = valid_number_range[int_value]
        reciprocal_value = 1 / valid_int_value
        print(f"The Reciprocal of your number is {reciprocal_value}.")
        break
    except ValueError:
        print("You did not enter an integer!!!")
    except IndexError:
        print("You did not enter a number between 1 and 10!!!")
    except ZeroDivisionError:
        print("Opps, you entered zero.")
    print("Please, try again.\n")

