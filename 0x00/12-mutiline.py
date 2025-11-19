#!/usr/bin/python
"""a module that """

# store receipt details
item = "Book"
quantity = 3
total = 45.00

# use a multi-line string with formatting
receipt = f"""
receipt:
Item: {item}
Quantity: {quantity}
total: ${total:.2f}
"""

print(receipt)