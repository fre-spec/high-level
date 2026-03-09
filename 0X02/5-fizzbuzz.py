#!/usr/bin/py
"a module that display from 1 t0 100"

for x in range(1, 101):
    print(x, end=" ")
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz", end=", " )
    elif x % 3 == 0:
        print("fizz", end=", ")
    elif x % 5 == 0:
        print("buzz", end=", ")
    else:
        print(x, end=", ")