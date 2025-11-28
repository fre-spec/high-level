#!/usr/bin/python
"""a module that handels mutiple conditional statement"""


age = int(input("Enter your age: "))

if age > 10 and age <= 17:
    print("you are a teenager")
elif age > 17 and age <=50:
    print("you are an adult")
elif age >= 50:
    print("you are a senior citizen")
else:
    print("you are a child")