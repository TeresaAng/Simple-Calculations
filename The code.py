#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:28:59 2020

@author: teresaangelopoulos
"""
import random

print("Here is a small numbers game with some easy calculations.")

number = "No number"

while number == "No number":
    number = input("Please enter a number in order to begin: ") or "No number"
    try:
        int(number)
        print("\nThank you! You entered the number:", number)
    except:
        try:
            float(number)
            print("\nThank you! You entered the number:", number, "\nIt "
                  "might be rounded for some calculations.")
        except:
            print("\nYou entered a string. A random number will be generated "
                  "for you instead. Do you accept the following number?")
            generated_number = random.randint(0,100)
            print("The number generated for you is: " + str(generated_number) + ". y or n?")
            answer = input()
            if answer == "n":
                number = "No number"
                continue
            else:
                if answer == "y":
                    print("\nThank you!")
                else:
                    print("\nOops! I think you meant to type 'yes'.")
                number = generated_number
                print ("Your number is", number)
                break
                
number = round(float(number)) #???
binumber = bin(number) # binär
octnumber = oct(number) #oktale
print("You entered the number", number, ":", binumber, "/", octnumber, ".")




number_1 = int(binumber[2:])
number_2 = int(octnumber[2:])
print("The results of the above numbers are:", number_1, "and", number_2)
operations_list = ["addition", "subtraction", "multiplication", "division"]
symbols_list = ["+", "-", "*", "/"]
calculate_list = [number_1+number_2, number_1-number_2, number_1*number_2, number_1/number_2]
for operations_list, symbols_list, calculate_list in zip(operations_list, 
                                                         symbols_list, calculate_list):
    print(operations_list, ":", number_1, symbols_list, number_2, "=", calculate_list)






