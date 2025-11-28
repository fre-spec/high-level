#!/usr/bin/python
"""a module that performs assignment operations"""
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

 
num1 += num2
print(f"add and assign: {num1} ")
num1 -= num2
print(f"sub and assign: {num1}")
num1 *= num2
print(F"mutiply and assign: {num1}")
num1 /= num2
print(f"division and assign: {num1}")
num1 //= num2
print(f"floor division and assign: {num1}")
num1 %= num2
print(f"modulus and assign: {num1} ")