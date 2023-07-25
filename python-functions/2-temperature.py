#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) / 1.8
    return celsius
fahrenheit = float(input("enter the temperature in fahrenheit: "))
print("Temperature in fahrenheit = {:.2f}".format(fahrenheit))
print("Temperature in celsius = {:.2f}".format(convert_to_celsius(fahrenheit)))

