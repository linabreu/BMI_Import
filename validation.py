#!/usr/bin/env python3

##file contains the validation functions for the calculate BMI program

#function to get users height
def get_height(prompt):
    valid_height = False
    
    height = int(input(prompt))
    print()
    while height <= 0:
            print ("Error. Height cannot be less than or equal to 0")
            height = int(input("Please reenter height in inches: "))
            print()
            if height > 0:
                valid_height = True
                return height

#function to get users weight
def get_weight(prompt):
    valid_weight = False
    
    weight = int(input(prompt))
    print()
    while weight <= 0:
            print ("Error. weight cannot be less than or equal to 0")
            weight = int(input("Please reenter weight in pounds: "))
            print()
            if weight > 0:
                valid_weight = True
                return weight
