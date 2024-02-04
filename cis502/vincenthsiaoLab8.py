##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 8 - Working with CSV Files
#  Application: Class Average
#  Description: Create a csv file given user
#    input and then create a grade report from
#    CSV data.
#  Testing Validation: below
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab8.py
#  Date: 10/24/2021
##

import re
import csv

#Defines number of exams (3)
numExams = 3
inputFormatting = "'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3'"
# Write to csv
def writeToGradeFile():
	with open("vhgrades.csv","w",newline='') as writer:
		csvwriter = csv.writer(writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for row in iter(lambda: \
			input("Enter student record in this format: {}, press -1 to stop > "\
				.format(inputFormatting)),
			"-1"):
			columns = row.split(" ")
			if(not re.match("[a-z]+ [a-z]+ [0-9]+ [0-9]+ [0-9]+",row.lower())):
				print("Invalid Row")
				continue
			csvwriter.writerow(columns)
	print("Grades written to vhgrades.csv")


#Generates grade report based on previous csv
def generateGradeReport():
	fileContent = []
	with open("vhgrades.csv","r") as reader:
	  csvReader = csv.reader(reader,delimiter=",")
	  for line in csvReader:
	    fileContent.append(line)

	grades = {}
	for person in fileContent:
	  numberedGrades = [int(x) for x in person[2:]]
	  grades[person[0] + " " + person[1]] = numberedGrades
	  grades[person[0] + " " + person[1]].append(sum(numberedGrades)/len(numberedGrades))

	examAverages = []
	examGrades = list(grades.values())
	for examNo in range(numExams):
		examScoreSum = 0
		for gradeList in examGrades:
			examScoreSum += gradeList[examNo]
		examAverages.append(examScoreSum/len(examGrades))
	for person, grades in grades.items():
		print("{}'s Exam Grades: {}. Average: {}".format(person,\
			" ".join([str(x) for x in grades[:-1]]),round(grades[-1],2)))
	print("\n")
	for examAverage in range(len(examAverages)):
		print("Class average for exam #{}: {}".format(examAverage,examAverages[examAverage]))

if __name__ == '__main__':
	writeToGradeFile()
	generateGradeReport()

"""
Testing output:

Enter student record in this format: 'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3', press -1 to stop > Vincent Hsiao 95 83 90
Enter student record in this format: 'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3', press -1 to stop > Bob Jones 86 75 84
Enter student record in this format: 'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3', press -1 to stop > Sue Smith 99 77 88
Enter student record in this format: 'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3', press -1 to stop > Karen Doe 83 88 92
Enter student record in this format: 'first SPACE last SPACE exam1 SPACE exam2 SPACE exam3', press -1 to stop > -1
Grades written to vhgrades.csv
Vincent Hsiao's Exam Grades: 95 83 90. Average: 89.33
Bob Jones's Exam Grades: 86 75 84. Average: 81.67
Sue Smith's Exam Grades: 99 77 88. Average: 88.0
Karen Doe's Exam Grades: 83 88 92. Average: 87.67


Class average for exam #0: 90.75
Class average for exam #1: 80.75
Class average for exam #2: 88.5

"""