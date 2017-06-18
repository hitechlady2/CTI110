#M3LAB ROMAN NUMERALS (Exercise #4, pg 115)
#06/18/17
#CTI-110 M3LAB ROMAN NUMERALS
#Benescha Sinclair

#Write a program that prompts the user to enter a number within the range 1 -10
#Program will display the Roman number verison on that number entered
#If outside of the 1 -10 range then an error messages will display.

# Number 1 is Roman Number I
# Number 2 is Roman Number II
# Number 3 is Roman Number III
# Number 4 is Roman Number IV
# Number 5 is Roman Number V
# Number 6 is Roman Number VI
# Number 7 is Roman Number VII
# Number 8 is Roman Number VIII
# Number 9 is Roman Number IX
#Number 10 is Roman Number X

#Get a number from the user
UserNumber = int(input(" Please enter a number within the range of 1 to 10 and press enter. " ))

#Assign Roman numbers to number from 1 to 10
if UserNumber == 1:
    print("I" )
elif UserNumber == 2:
    print("II" )
elif UserNumber == 3:
    print("III" )
elif UserNumber == 4:
    print("IV" )
elif UserNumber == 5:
    print("V" )
elif UserNumber == 6:
    print("VI" )
elif UserNumber == 7:
    print("VII" )
elif UserNumber == 8:
    print("VIII" )
elif UserNumber == 9:
    print("IX" )
elif UserNumber == 10:
    print("X" )
else:
    print("Error Message: Please enter a number within the range of 1 to 10. " )
    

