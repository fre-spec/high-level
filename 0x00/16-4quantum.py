#!/usr/bin/python
"""Evaluate a simple arithmetic expression without using eval()"""

expr = input("Enter expression (example: 3 + 5 *2):")

token = expr.split()
#Extract parts
num1 = float(token[0])
op = token[1]
num2 = float(token[2])

#do it manually 
if op =="+":
    result = num1 + num2 
elif op == "-":
    result = num1 - num2 
elif op == "*":
    if num2 == 0:
        result = " Error: Division by zero "
    else:
        result = num1 / num2
else:
    result = "invalid operator"
print("Result:", result)