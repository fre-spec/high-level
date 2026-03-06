#!/usr/bin/py
"a module that display from 1 t0 100"

for x in range(1,101):
    print(x, end=" ")
if x % 3 == 0 and x % 5 == 0:
    print("fizzbuzz", end=", " )