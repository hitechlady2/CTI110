#M3HW2: Body Mass Index Page 118 Exercise# 14
#06/18/17 Sunday
#CTI-110 M3HW2: Body Mass Index
#Benescha Sinclair

#Write a program tha calculates and displays a person's BMI.
#Calculate BMI = weight * 703/(height * ^2)
#Weight is measured in lbs and height is measured in inches

#Ask the user to enter a weight and height to display BMI
#Optimal weight (BMI 18.5 - 25)
#Underweight (less than 18.5 BMI) 
#Overweight (greater than 25 BMI)

#Ask the user to enter a weight and height.
UserWeight = float(input("Please enter a weight(in pounds)and press enter. " ))
UserHeight = float(input("Please enter a height(in inches) and press enter. " ))

#Calculate the BMI
UserBMI = (UserWeight * 703)/(UserHeight ** 2)

# Create a space between lines.
print()

#Classify the BMI range
if UserBMI < 18.5:
    print("The person's BMI of " + format( UserBMI, ".1f" ) + " is underweight")
elif UserBMI < 26:
    print("The person's BMI of " + format( UserBMI, ".1f" ) + " is optimal weight")
elif UserBMI > 25:
    print("The person's BMI of " + format( UserBMI, ".1f" ) + " is overweight")


