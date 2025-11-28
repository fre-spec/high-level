#!/usr/bin/python
"""a module that calculates the area of a triangle"""

def triangle(base, height):
    """
    A function thta calculate the area of a triangle 
    base: Base of the triangle
    height: Height of the triangle 
    """

    return 0.5 * base * height

if __name__ == "__main__":
     base = int(input ("Enter the base of a triangle:"))
     height = int(input("Enter the height of triangle:"))


     result = triangle(base, height)
     print(f"Area of a triangle is {result}")
