#M6HW2 - Random Number File Reader #8
#July 14, 2017
#CTI110 M6HW2 - Random Number File Reader
#Benescha Sinclair


RandomFile = open("randomnumbers.txt", "r")

#Read the first line
line = RandomFile.readline()

#Read rest of the lines
while line != "":
    #Read the quantity
    qty = float(RandomFile.readline())
    

    for line in RandomFile:
        print(line, end="")

    #line = line.rstrip("\n")

    line = RandomFile.readline()
    
def main():
    total = 0.0

    try:
        #open the file
        RandomFile = open("randomnumbers.txt", "r")

        #read the values
        #calculate
        for line in RandomFile:
            amount = float(line)
            total += amount
        print(qty)

        #close the file
        RandomFile.close()

        #print the total
        print("The total of the numbers is")
        print(format(total, ',.2f'))

    except IOError:
        print("An error occured trying to read the file.")

    except ValueError:
        print("Non-numeric data found in the file.")

    except:
        print("An error occured.")

main()
