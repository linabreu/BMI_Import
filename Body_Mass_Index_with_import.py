#!/usr/bin/env python3

import validation

def main():
#display welcome message
    print("Welcome to the Body Mass Index Caclulator")
    print()

    print("Please note this BMI calculator uses the American System")
    print()

#set boolean to true so the program starts by entering the loop
    answer = "y"

#use while loop to allow for repeated entries
    while answer == "y" or answer.upper()== "Y": #so answer isnt case sensitive


    #get user input
        height = validation.get_height("Please enter your height in inches: ")
        weight = validation.get_weight("Please enter your weight in pounds: ")
        print()


        BMI = round(float((weight/height/height) * 703),2)
        print("Your BMI is: ", BMI)

        if BMI < 18.5:
            print("You are considered underweight")
        elif BMI >= 18.5 and BMI < 25:
            print ("You are considered normal weight")
        elif BMI >= 25 and BMI < 30:
            print ("You are considered overweight")
        else:
            print ("You are considered obese")
    

    #give chance to exit loop or go again
        print()
        answer = input("Do you want to perform another BMI calculation? Type Y or Q to quit:  ")
        print()

    print("Thank you for using the BMI Calculator")

if __name__ == "__main__":
    main()



