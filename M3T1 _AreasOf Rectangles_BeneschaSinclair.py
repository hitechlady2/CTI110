#M3T1 Areas of Rectangles (Exercise #2, pg 115)
#06/18/17
#CTI-110 M3T1 Areas of Rectangles
#Benescha Sinclair

#The area of a rectangle is the rectangle's lenght times its width.
#Write a program that asks for the lenght and width of two rectangles.
#The program should tell the user which rectangle has the greater area, or if areas are the same.

#Get lenght of rectangle 1
RectangleLenght1 = int(input("Please enter the lenght of rectangle #1 and press enter: "))

#Get width of rectange 1
RectangleWidth1 = int(input("Please enter the width of rectangle #1 and press enter1: "))

#Get lenght of rectangle 2
RectangleLenght2=int(input("Please enter the lenght of rectangle #2 and press enter : "))

#Get width of rectange 2
RectangleWidth2=int(input("Please enter the width of rectangle #2 and press enter : "))

#Calculate the area of rectangle 1
Rectangle1Area= RectangleLenght1 * RectangleWidth1

#Calculate the area of rectangle 2
Rectangle2Area= RectangleLenght2 * RectangleWidth2

if Rectangle1Area> Rectangle2Area:
    print("Rectangle #1 is bigger than Rectangle #2")

elif Rectangle2Area > Rectangle1Area:
    print("Rectangle #2 is bigger than Rectangle #1")

else:
    print ("Rectangle #1 and Rectangle #2 are equal")
