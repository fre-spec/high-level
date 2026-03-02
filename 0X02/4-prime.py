#!/usr/bin/py
"""a module displays prime number from 1, 100"""
for num in range(2, 101):
   
    prime = True

    for x in range(2, num):
        if num % x == 0:
            prime = False
            break
    if prime:
      print(num, end=", ")