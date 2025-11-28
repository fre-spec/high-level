#!/usr/bin/python 
# two integers print AND, OR, XOR,  and left shift by 2 
num1 = int(input("Enter the first numbers:"))
num2 = int(input("Enter the second number:"))

print(f"AND {num1 and num2}")
print(f"OR {num1 or num2}")
print(f"XOR {num1 ^ num2}")
print(f"BITWISE SHIFT {num1 << 2}")
print(f"BITWISE SHIFT {num2 << 2}")