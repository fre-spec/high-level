#!/usr/bin/python
"""a module that performs logical operations"""
num = int(input("Enter a numeber:"))

print(f"LOGICAL AND  {num > 5 and num < 10}")
print(f"LOGICAL OR {num > 5 or num < 10}")
print(f"LOGICAL NOT { not(num > 5)}")