##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 4 - Functions, Passing Multiple Arguments
#  Application: Your Course Grade Calculator
#  Description: Read in an indefinite number of user inputs
#      until Enter is pressed using a iterator. Then, calculate the
#      average then chewck if the average is bigger than the lowest lab score.
#      If it is, then repalce the lowest lab score with the average.
#  Testing Validation: vincenthsiaoLab4Test.py
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab4.py
#  Date: 9/18/2021
##


#Imports
import statistics

#Constants
SPACE = ""

#Helper Functions
def validateNumber(num: str) -> bool:
       """
       Returns whether given number is valid or not

       :param num: number passed in for validation
       :type num: str
       :rtype: boolean
       :return: if passed in number passes all validation tests
       """
       return num.isnumeric() and 0 <= float(num) <= 20

round2 = lambda num: round(num,2) # -> Float

def avg(scores: list[int]=[0]) -> float: 
       """
       Returns average of given list

       :param scores: the list to find averages
       :type scores: List[int]
       :rtype: float
       :return: sum of the list divided by length of list
       """

       return sum(scores)/len(scores)

def get_scores():
       """
       Inputs user for scores, finds average, applies bonus and returns new score
       
       :rtype: fLoat
       :return: Scores total after bonus applied
       """
       #Variable Declarations
       scores = []

       #Get scores from user's keyboard input
       for a_score in \
              iter(lambda: input('Enter your lab score [0..20] <Press Enter to QUIT> '), SPACE):
              if(validateNumber(a_score)):
                     scores.append(float(a_score))

       #Calculate Variance and Standard Deviation with Statistics
       variance = round2(statistics.variance(scores))
       standard_dev = round2(statistics.pstdev(scores))

       
       LOWEST_SCORE = min(scores)
       LOWEST_IND = scores.index(LOWEST_SCORE)
       #Calculate Average
       average = round2(avg(scores))
       print(scores,average)
       
       #Apply bonus to lowest lab score if applicable
       if(LOWEST_SCORE < average):
              print("Bonus of {} applied to scores".format(average))
              scores[LOWEST_IND] = average
       
       #Recalculate Average after bonus applied
       average = round2(avg(scores))
       print(scores,average)

'''
Test Output:

Enter your lab score [0..20] <Press Enter to QUIT> 20
Enter your lab score [0..20] <Press Enter to QUIT> 20
Enter your lab score [0..20] <Press Enter to QUIT> 19
Enter your lab score [0..20] <Press Enter to QUIT> 19
Enter your lab score [0..20] <Press Enter to QUIT> 18 
Enter your lab score [0..20] <Press Enter to QUIT> 18
Enter your lab score [0..20] <Press Enter to QUIT> 19
Enter your lab score [0..20] <Press Enter to QUIT> 1
Enter your lab score [0..20] <Press Enter to QUIT> 19.5
Enter your lab score [0..20] <Press Enter to QUIT> 18
Enter your lab score [0..20] <Press Enter to QUIT> 20
Enter your lab score [0..20] <Press Enter to QUIT> 34.25
Enter your lab score [0..20] <Press Enter to QUIT> 
[20.0, 20.0, 19.0, 19.0, 18.0, 18.0, 19.0, 1.0, 18.0, 20.0] 17.2
Bonus of 17.2 applied to scores
[20.0, 20.0, 19.0, 19.0, 18.0, 18.0, 19.0, 17.2, 18.0, 20.0] 18.82

'''