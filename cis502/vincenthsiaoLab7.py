##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 7 - Regular Expressions 
#  Application: Date Format Converter
#  Description: Given a string date, convert
#    it into a formatted date
#  Testing Validation: below
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab7.py
#  Date: 10/17/2021
##

import re


def convertDate(strDate):
	s = strDate
	DATEMAPPINGS = {"January": 31, "March": 31, "April": 30, 
	"May": 31, "June": 30, "July": 31, "August":31,
	 "September": 30, "October": 31,"November": 30, "December": 31}
	DATES = ["January","Feburary","March","April","May","June","July",
	    "August","September","October","November","December"]
	try:
		if(re.match(r"[0-9]{2}/[0-9]{2}/[0-9]{4}",s)==None):
			print("Invalid Date!")
			raise SystemExit
		m,d,y = tuple(s.split("/"))
		d,m,y=int(d),int(m),int(y)
		if(1000 > y or y > 2999 or 1 > m or m > 12):
			print("Invalid Year or Month!")
			raise SystemExit
		leapYear = y % 4 == 0
		mWord = DATES[m-1]
		if(m == 2):
			if(leapYear == True):
				maxDay = 29
			else:
				maxDay = 28
		else:
			maxDay = DATEMAPPINGS[mWord]
		if(1 > d or d > maxDay):
			print("Invalid Day!")
			raise SystemExit
		else:
			print("Converted Date: {} {}, {}".format(mWord,d,y))
	except Exception:
		print("Invalid Date! Exception occured.")
		raise SystemExit

if __name__ == '__main__':
	for i in range(5):
		try:
			date1 = input("Enter a date string (Format MM/DD/YYYY) >")
			convertDate(date1)
		except Exception:continue

"""
Test output:

Enter a date string (Format MM/DD/YYYY) >03/25/2021
Converted Date: March 25, 2021
Enter a date string (Format MM/DD/YYYY) >03/00/2021
Invalid Day!
SystemExit
Enter a date string (Format MM/DD/YYYY) >02/29/2020
Converted Date: Feburary 29, 2020
Enter a date string (Format MM/DD/YYYY) >02/29/2021
Invalid Day!
SystemExit
Enter a date string (Format MM/DD/YYYY) >01/01/0999
Invalid Year or Month!
SystemExit
Enter a date string (Format MM/DD/YYYY) >01/1/3000
Invalid Date!
"""