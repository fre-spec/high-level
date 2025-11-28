#!/usr/bin/python
"""a module that performs bitwise operation"""

num = int(input("Enter a number:"))

print(f"bitwise shift left {num << 1}")
print(f"bitwise shift right {num >> 1}")
print(f"bitwise and {num & 1}")
print(f"bitwise or {num^1}")