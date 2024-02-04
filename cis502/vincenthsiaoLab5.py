##
#  Student Name:  Vincent Hsiao
#  Course: CIS 502 Applied Python Programming
#  Lab # 6 - Pandas: DataFrames
#  Application: Regulating Temperature
#  Description: Given some data, convert into dataframe and
#       run tests and generate results from dataframe
#  Testing Validation: below
#  Version: Python 3.9
#  Solution File:  vincenthsiaoLab6.py
#  Date: 10/10/2021
##

import pandas

temps = {
    'Maxine': [98.6, 96.9, 97.7], 
    'James': [98.9, 100.3, 101.1], 
    'Amanda': [98.5, 98.3, 98.7]
}

dataframe = pandas.DataFrame(temps)
dataframe2 = pandas.DataFrame(temps,["Morning","Afternoon","Evening"])
print("Original Dataframe: \n{}\n".format(dataframe))
print("New Dataframe: \n{}\n".format(dataframe2,"\n"))
print("Data from column 'Maxine'\n{}\n".format(dataframe2['Maxine']))
print("Data from row 'Morning'\n{}\n".format(dataframe2.loc['Morning']))
print("Data from rows 'Morning' and 'Evening'\n{}\n".
	format(dataframe2.loc[['Morning','Evening']]))
print("Data from columns 'Maxine' and 'Amanda'\n{}\n".
	format(dataframe2[['Maxine','Amanda']]))
print("Data for Maxine and Amanda in morning + evening\n{}\n".
	format(dataframe2[['Maxine','Amanda']].loc[['Morning','Evening']]))
print("Transposed\n{}\n".format(dataframe2.transpose()))
print("Sorted Dataframe\n{}\n".format(dataframe2.reindex(sorted(dataframe2.columns), axis=1)))

"""
Test output:

Original Dataframe: 
   Maxine  James  Amanda
0    98.6   98.9    98.5
1    96.9  100.3    98.3
2    97.7  101.1    98.7

New Dataframe: 
           Maxine  James  Amanda
Morning      98.6   98.9    98.5
Afternoon    96.9  100.3    98.3
Evening      97.7  101.1    98.7

Data from column 'Maxine'
Morning      98.6
Afternoon    96.9
Evening      97.7
Name: Maxine, dtype: float64

Data from row 'Morning'
Maxine    98.6
James     98.9
Amanda    98.5
Name: Morning, dtype: float64

Data from rows 'Morning' and 'Evening'
         Maxine  James  Amanda
Morning    98.6   98.9    98.5
Evening    97.7  101.1    98.7

Data from columns 'Maxine' and 'Amanda'
           Maxine  Amanda
Morning      98.6    98.5
Afternoon    96.9    98.3
Evening      97.7    98.7

Data for Maxine and Amanda in morning + evening
         Maxine  Amanda
Morning    98.6    98.5
Evening    97.7    98.7

Transposed
        Morning  Afternoon  Evening
Maxine     98.6       96.9     97.7
James      98.9      100.3    101.1
Amanda     98.5       98.3     98.7

Sorted Dataframe
           Amanda  James  Maxine
Morning      98.5   98.9    98.6
Afternoon    98.3  100.3    96.9
Evening      98.7  101.1    97.7

[Finished in 1.3s]
"""