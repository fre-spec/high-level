#!/usr/bin/python
"""a module that handels password check"""

password = input("Enter your password here: ")
if len(password) < 8:
    print("password must be at least 8 character long")
else:
    print("password is valid")




