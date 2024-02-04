##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 2 - The statistics and decimal Modules
#  Application: Validating User Input of Monetary Amounts, 
#				Generating Measures of Central Tendency 
#  Description: This program grabs 7 inputs from the user, and then
#		calculates the standard deviation, median and mode of the values 
#  Testing Validation: Program output
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab1.py
#  Date: 9/5/2021
#  Big Data Project of Interest:  COVID Cases Growth
##

import statistics
from decimal import *

#numberInputValidation(Str message), used as a quick way to 
#	ask users for a number and validate it as a number
def numberInputValidation(message: str):
	while True:
		try:
			num = input(message)
			num = int(num)
			if(num <= 0):
				print("Invalid Value")
			return num
		except (ValueError, TypeError):
			print("Invalid Value")
			continue

#format2(Float/Int flt), used to round a float to two decimal places
format2 = lambda flt: "{:.2f}".format(flt)

#Main method
def main():
	NUM_RUNS = numberInputValidation("Enter number of runs: ")
	for run_no in range(1,NUM_RUNS+1):
		print(f"Test run {run_no}")
		acceptedInput = 0
		revenue_data = []
		while (acceptedInput < 7):
			try:
				user_input = Decimal(
					input(f"[{acceptedInput+1}] Enter a revenue value (>= 0): ")
				).quantize(Decimal(".01"),rounding=ROUND_UP)
				if(user_input > 0):
					acceptedInput += 1
					revenue_data.append(user_input)
			except InvalidOperation:
				continue

		median = statistics.median(revenue_data)
		mean = statistics.mean(revenue_data)
		standard_deviation = statistics.stdev(revenue_data)
		print(f"Revenues: {[float(x) for x in revenue_data]}\n\
Mean: {format2(mean)}\nMedian: {median}\n\
Standard Deviation: {format2(standard_deviation)}")

if __name__ == '__main__':
	main()

"""
Test run:

Enter number of runs: 2
Test run 1
[1] Enter a revenue value (>= 0): 239.5
[2] Enter a revenue value (>= 0): 53.9
[3] Enter a revenue value (>= 0): 211.5
[4] Enter a revenue value (>= 0): 11..98
[4] Enter a revenue value (>= 0): 11.98
[5] Enter a revenue value (>= 0): 5.98
[6] Enter a revenue value (>= 0): 23.95
[7] Enter a revenue value (>= 0): 115.2
Revenues: [239.5, 53.9, 211.5, 11.98, 5.98, 23.95, 115.2]
Mean: 94.57
Median: 53.90
Standard Deviation: 96.97
Test run 2
[1] Enter a revenue value (>= 0): 1898
[2] Enter a revenue value (>= 0): 435
[3] Enter a revenue value (>= 0): 2331
[4] Enter a revenue value (>= 0): 628
[5] Enter a revenue value (>= 0): 332.5
[6] Enter a revenue value (>= 0): 800
[7] Enter a revenue value (>= 0): 2553
Revenues: [1898.0, 435.0, 2331.0, 628.0, 332.5, 800.0, 2553.0]
Mean: 1282.50
Median: 800.00
Standard Deviation: 946.42
"""