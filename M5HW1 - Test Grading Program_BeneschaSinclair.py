#M5HW1 - Test Grading Program
#July 10, 2017
#CTI110 M5HW1 - Test Grading Program
#Benescha Sinclair


#Write a program that ask to enter five test scores.
#Program will display a letter grade for each score and avg test score.

#Calc_Average Function should accept five test scores as arguments and return avg.
#determine_grade Function will accept test score argument and return letter grade.

#Score/Letter Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#Below 60 F

def calcA(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)/5
    return average

def determineGrade( userScore ):
    if( userScore < 60 ):
        return "F"
    elif( userScore < 70 ):
        return "D"
    elif( userScore < 80 ):
        return "C"
    elif( userScore < 90 ):
        return "B"
    elif( userScore < 101 ):
        return "A"

def askForScores():
    score1 = float( input( "Please enter score 1: "))
    score2 = float( input( "Please enter score 2: "))
    score3 = float( input( "Please enter score 3: "))
    score4 = float( input( "Please enter score 4: "))
    score5 = float( input( "Please enter score 5: "))

    return score1, score2, score3, score4, score5
    
def printTableOfResults(score1, score2, score3, score4, score5 ):
    print("Score\tLetter Grade" )
    print( str( score1) + "\t\t" + determineGrade( score1 ), \
           str( score2) + "\t\t" + determineGrade( score2 ),
           str( score3) + "\t\t" + determineGrade( score3 ),
           str( score4) + "\t\t" + determineGrade( score4 ),
           str( score5) + "\t\t" + determineGrade( score5 ), sep = "\n")

def main():
    score1, score2, score3, score4, score5 = askForScores()
    print()
    printTableOfResults(score1, score2, score3, score4, score5 )

main()
    
