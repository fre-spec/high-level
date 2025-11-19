#!/usr/bin/python
"""a module that uses f-spring"""

# store product name and price 
product = "laptop"
price = 750.5

#use an f-string with two decimal places 
message = f"the price of {product} is ${price:.2f}"
print(message)