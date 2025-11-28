#!/usr/bin/python
""" check if three numbers form a strictly increasing sequence"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 < num3:
    print("strictly increasing")
else: 
    print("not stritly increasing")
