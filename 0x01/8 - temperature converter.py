#!/usr/bin/python
"""a module that converts temperature"""

def convert_temperature(temp, scale):
    if scale == "C":
        return (temp - 32) * 5/9
    elif scale == "F":
        return (temp * 9/5) * 32
    else:
        return None
    
if __name__=="__main__":
    temp = float(input("Enter temperature value: "))
    scale = input("Convert to celsuis (C) or fahrenheit (F)? ")

    result = convert_temperature(temp, scale)

    if result is None:
            print("invalid scale")
    else:
            print("Converted tempeature:", result)