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

print("\nDo you know how this number is written in binary?")
number = round(float(number))
binumber = bin(number)                 
   
guess = input("Enter the number "+str(number)+" in binary: ")
if guess == binumber:
    print("correct!")
else:
    print("Sorry, wrong. The correct answer would be:", binumber)

print("\nWhat about the octal number? Can you write it?")
octanswer = input()
octnumber = oct(number)
if octanswer == octnumber:
    print("correct!")
else:
    print("Sorry, wrong. The correct answer would be:", octnumber)

print("\nNow, let us practise some simple math. Do you want to pick the numbers yourself?" 
      " y or n?")
pickYourself = input("You said: ") or "No answer"
if pickYourself == "y":
    try:
        number_1 = float(input("Enter the first number: "))
    except:
        print("You didn't enter a number, that is why your number will be picked for you")
        number_1 = random.randint(0,100)
    try:
        number_2 = float(input("Enter the second number: "))
    except:
        print("You didn't enter a number, that is why your number will be picked for you")        
        number_2 = random.randint(0,100)
else:
    number_1 = random.randint(0,100)
    number_2 = random.randint(0,100)

print("The numbers are:", number_1, "and", number_2)
operations_list = ["\naddition", "subtraction", "multiplication", "division"]
symbols_list = ["+", "-", "*", "/"]
calculate_list = [number_1+number_2, number_1-number_2, number_1*number_2, number_1/number_2]
for operations_list, symbols_list, calculate_list in zip(operations_list, 
                                                         symbols_list, calculate_list):
    print(operations_list, ":", number_1, symbols_list, number_2, "=", calculate_list)





   
