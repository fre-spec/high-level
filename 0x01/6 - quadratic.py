#!/usr/bin/python
"""a module that uses function to calculate quadratic equation"""

import math

def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) /(2*a)
        return x1, x2

    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        return complex(real, imag), complex(real, -imag)

if __name__ == "__image__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    result = quadratic(a, b, c)
    print(f"solution(s): {result}")