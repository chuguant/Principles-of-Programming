# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os
import sys
from collections import defaultdict

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

'''
In terms of frequency, John was the most popular as a female name first in the year 1880.
  It then accounted for 0.05% of all female names.
In terms of frequency, John was the most popular as a male name first in the year 1880.
  It then accounted for 8.74% of all male names.
'''

# Replace this comment with your code
male_count_by_year = defaultdict(list)
female_count_by_year = defaultdict(list)
totalcount_by_year = defaultdict(list)
max_male_frequency = 0
max_female_frequency = 0

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
    #print('year',year)
    # Opening 1 file for reading purposes
    with open(directory + '/' + filename) as data_file:
        # Processing each line in file that I am reading
        maleCount = 0
        femaleCount = 0
        for line in data_file:
            # Extracting th 3 fields from the line
            name, gender, count = line.split(',')
            if gender == 'M':
                maleCount = maleCount + int(count)
            else:
                femaleCount = femaleCount + int(count)
            if name == first_name:
                if gender == 'M':
                    male_count_by_year[year].append(count.replace('\n',''))
                else:
                    female_count_by_year[year].append(count.replace('\n',''))                   
        totalcount_by_year[year].append(maleCount)
        totalcount_by_year[year].append(femaleCount)
        
'''
for year in count_by_year:
    if int(count_by_year[year][0]) > maxCount:
        maxCount = int(count_by_year[year][0])
        if 
    else:
        continue
'''
for year in male_count_by_year:
    f = int(male_count_by_year[year][0]) / int(totalcount_by_year[year][0])
    if f > min_male_frequency:
        min_male_frequency = f 
        male_first_year = year
    else:
        continue

for year in female_count_by_year:
    f = int(female_count_by_year[year][0]) / int(totalcount_by_year[year][1])
    if f > min_female_frequency:
        min_female_frequency = f
        female_first_year = year
    else:
        continue

'''
print('\nmale_count_by_year',male_count_by_year)
print('\nfemale_count_by_year',female_count_by_year)
print('\ntotalcount_by_year',totalcount_by_year)
print('\nmale_first_year',male_first_year)
print('\nfemale_first_year',female_first_year)
'''
'''
print('\nmax_male_frequency',min_male_frequency)
print('\nmax_female_frequency',min_female_frequency)
print('\n')
'''

min_male_frequency = min_male_frequency * 100
min_female_frequency = min_female_frequency * 100

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

