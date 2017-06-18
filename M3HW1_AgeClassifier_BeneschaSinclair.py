#M3HW1 Age Classifier (Exercise #3, pg 115)
#06/18/17
#CTI-110 M3HW1 Age Classifier
#Benescha Sinclair

#Write a program that asks the user to enter a person's age.
#The program should display a message indicating whether the person is a infant, a child, a teenager, or an adult.

#Infant is 1 yr old or less
#Child is 13 yrs old or less, (but older than 1 yrs old)
#Teenage is less than 20 yrs old (but older than 13yrs old)
#Adult is 20 yrs old and older

#Ask the user for the person's age
PersonAge = int(input(" Please enter a person's age: "))

#To classify as an infant
if PersonAge <= 1:
    print ("This person is an infant")

#To classify as a child
elif PersonAge < 13:
    print ("This person is a child")

#To classify as a teenager
elif PersonAge <20:
    print ("This person is a teenager")

#To classify as an adult
elif PersonAge >= 20:
    print ("This person is an adult")
