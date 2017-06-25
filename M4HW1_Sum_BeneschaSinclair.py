#M4HW1 Sum of Numbers (Exercise #8, pg 162)
#06/25/17
#CTI-110 M4HW1 Sum of Numbers
#Benescha Sinclair

#Write a program with a loop that asks the user to enter a series positive numbers.
#The user will enter a negative number to signal the end of series.
#The program should display a sum for the positive numbers entered.

#Loop
Sum = 0

#Assign UserNumber
UserNumber = float(input("Enter a number to calculate and press ENTER or a negative number to end series: "))

#Calculation
while UserNumber > -1:
    Sum = Sum + UserNumber
    UserNumber = float(input("Enter a number to calculate and press ENTER or a negative number to end series: "))

#Enter space before results
print()

#print series of number total
print("The sum of the numbers entered is", Sum )

