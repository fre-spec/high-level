#!/usr/bin/python
"""a module that print fizz or buzz"""

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)