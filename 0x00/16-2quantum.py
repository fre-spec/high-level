#!/usr/bin/python
""" truth table for two boolean variables"""
values = [0, 1]

print("A | B | AND | OR | NOT A | NOT B ")
print("-" * 30)

for A in values:
    for B in values:
        print(f"{A} | {B} | {A and B} | {A or B} | {int(not A)}  | {int(not B)}")