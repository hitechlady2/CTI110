# Functions (Exercise#10 Pg 230)
# 07/02/17
# CTI-110 M5T2_FeetToInches 
# Benescha Sinclair

#One foot equals 12 inches.
#Write a function named feet_to_inches that
#accepts a number of inches in that many feet.
#Use the function in a program that prompts the user to enter a number
#of feet and then displays the number of inches in that many feet.

InchesPerFoot = 12

#Define main fuction and ask user to enter the number feet to convert into inches.
def main():
    feet = int(input("Please enter the number of feet you would like to convert into inches: "))
    print()
#Convert using calculations
    print("A measurement of", feet, "feet equals to", feet_to_inches(feet), "inches.")

#Converts feet to inches
def feet_to_inches(feet):
    return feet * InchesPerFoot

#Call main function
main()
    
