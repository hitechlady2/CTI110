# Functions(Exercise #1 Page 229)
# 07/02/17
# CTI-110 M5T1_KilometerConverter 
# Benescha Sinclair
#
#Write a program that asks the user to enter a distance in Kilometers and then
#convert it into miles.

#Define Ask User for the Kilometers
def AskUserForKilometers():
    UserKilometers=float( input( "Please enter the distance in kilometers: "))
    return UserKilometers

#Define conversion by calculation
def ConvertKilometersToMiles( UserKilometers ):
    Miles=UserKilometers * 0.6214
    return Miles

#Define main
def Main():
    UserKilometersTyped=AskUserForKilometers() 
    ConvertedMiles=ConvertKilometersToMiles( UserKilometersTyped )

#Creating a space
    print()

#Print results of calculation from converting kilometers to miles
    print( UserKilometersTyped, "kilometers converted to miles is", \
           format( ConvertedMiles, ".2f" ), "miles" )

#Calling main
Main()
    





