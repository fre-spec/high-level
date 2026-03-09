#!/usr/bin/py
def ussd():

    while True:
        print("select an option: ")
        print("1. check balance")
        print("2. buy airtime")
        print("3. exit")

        select = int(input("Pick between 1,2 and 3:"))
        if select == 1:
            print("your account balance is 1000,000")
        elif select == 2:
            airtime = int(input("How much is airtime do you want?: "))
            print(f"you have succesfully purchased ${airtime}")
        elif select == 3:
            print("Thank you for using our service. Goodbye!")
            break
ussd()