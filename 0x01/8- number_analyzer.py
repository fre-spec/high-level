#!/usr/bin/python
"""a module that analysis number """
def analyze_number(num):
    if num % 2 == 0:
        result = "Even number"
    else:
        result = "Odd number"

        if num % 5 == 0:
            print("special number: divisible by 5")

        return result  
    if __name__ == "__main__":
        
        num = int(input("Enter a number: "))
        print(analyze_number(num))