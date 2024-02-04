##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 3 - Algorithms Using Conditional Execution and Looping Constructs
#  Application: Generating Mathematical Sequences
#  Description: Compute a hailstone sequence of 'length' steps beginning with a
#     given 'start' value. Validate that the start value is a positive integer. 
#  Testing Validation: vincenthsiaoLab3Test.py
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab3.py
#  Date: 9/11/2021
##

#hailstone(start Int, length Int): used to implement the Hailstone function
#algorithm into the assignment
def hailstone(start,length):
    result = [start]
    for i in range(length-1):
        prev = result[-1]
        if(prev % 2 == 1):
            result.append((3*prev) + 1)
        else:
            result.append(int(prev/2))
    print("Min: {}, Max: {}".format(min(result),max(result)))
    return result