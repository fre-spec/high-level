#!/usr/bin/python
""" keep asking until user enters 1-100"""
while True:
    n = int(input("Enter a number between 1 and 100: "))
    if 1 <= n <= 100:
        print("valid input:", n)
        break
    else:
        print("Invalid. try again.")