#Please Replace: Lab 3
##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 3 - Algorithms Using Conditional Execution and Looping Constructs test
#  Application: Lab #3 Test Driver
#  Description: Run arguments through the hailstone function from the main module
#  with an automated test function testFunct()
#  Testing Validation: Program output
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab3Test.py
#  Date: 9/11/2021
##
from vincenthsiaoLab3 import hailstone

#testFunct(args List[Tuple(int,int)])
#Used to run a list of test cases through the algorithm with one call
def testFunct(args):
    for arg0,arg1 in args:
        print(f"Running {arg0}, {arg1} into hailstone()")
        print(f"Result: {hailstone(arg0,arg1)}\n")
        
testFunct([(7,10),(7,20)])






#In the two results, the second result builds off of the first one with additional
# numbers. 

"""
Running 7, 10 into hailstone()
Min: 7, Max: 52
Result: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20]

Running 7, 20 into hailstone()
Min: 1, Max: 52
Result: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1]

[Finished in 46ms]
"""