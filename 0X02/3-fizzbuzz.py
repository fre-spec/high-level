#!/usr/bin/python 
"""a module that displays result in a single line"""

for x in range(1, 51):
    print(x,end=" ")
if x % 3 == 0 and x % 5 == 0:
    print("fizzbuzz", end=", ")
elif x % 3 == 0:
    print("fizz", end=", ")
elif x % 5 == 0:
    print("buzz", end=", ")
else:
    print(x, end=", ")