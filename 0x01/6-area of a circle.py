#!/usr/bin/python
"""a function that calculates the area of a circle"""
import math

def circle(radius):
    return math.pi * radius * radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))

    result = circle(radius)
    print(f"Area of the circle is {result}")