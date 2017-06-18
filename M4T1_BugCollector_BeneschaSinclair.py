#M4T1 Bug Collector (Exercise #1, pg 161)
#06/18/17
#CTI-110 M4T1 Bug Collector 
#Benescha Sinclair

#Write a program that keep track of bugs collected in five days.
#The loop ask for number of bugs each day
#Program will display the total number of bugs collected


TotalDays = 5
TotalBugs = 0

for CurrentDay in range(1, TotalDays +1 ):
    BugsCollected = int( input( "How many bugs were collected on day " + str(CurrentDay) +": "  ))
    TotalBugs = TotalBugs + BugsCollected
print()
print("The total number of bugs collected during", TotalDays, "days is", TotalBugs, "bugs." )

