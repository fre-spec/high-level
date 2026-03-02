#!/usr/bin/python
""" a module that calculates for discount"""

def apply_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    if discount_percent > 50:
    
        print("high discount applied!")
    return discount_amount 
if __name__ == "__main__":
    price = float(input("Enter original price: "))
    discount = float(input("Enter discount percentage: "))

    final_price = apply_discount( price, discount)
    print("Final price:", final_price)
