#!/usr/bin/python 
"""Detect data type of input"""

user_input= input("Enter something: ")
#Try int
try:
    int(user_input)
    print("You enetered an integer")
except:
    try:
        float(user_input)
        print("You enetered a float")
    except:
        print("You enetered a string")
