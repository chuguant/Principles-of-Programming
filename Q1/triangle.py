# Written by Chuguan Tian for COMP9021


# Insert your code here
import sys
from collections import defaultdict
import copy

file_name = input('Which data file do you want to use?')
try:
    data_file = open(file_name)
    data = data_file.readlines()
    if data == []:
        raise ValueError
        sys.exit()
except IOError:
    print('Incorrect input!')
    sys.exit()
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
data_file.close()
        
#read data
s = []
triangle = defaultdict(list)
for i in data:
    s.append(i.split())

for i in range(len(s)):
    for j in range(len(s[i])):
        triangle[i].append(int(s[i][j]))

##print(data)
##print(s)
##print(triangle)
##print(len(triangle))

'''
defaultdict(<class 'list'>,
{0: [7], 1: [3, 8], 2: [8, 1, 0], 3: [2, 7, 4, 4], 4: [4, 5, 2, 6, 5]})
'''

#get all path[i]
sub_path = []
summ = 0
for i in range(len(triangle)-1,-1,-1):
    rev = len(triangle)-i-1
    path = defaultdict(list)
    for j in range(0,len(triangle[i])):
##        print('\n(i,j)',(i,j))
##        print('rev',rev)
        if  i+1 == len(triangle):
            path[i].append([triangle[i][j],1,[triangle[i][j]]])
        if  i+1 < len(triangle) and sub_path[rev-1][j][0] == sub_path[rev-1][j+1][0]:
            summ = triangle[i][j] + sub_path[rev-1][j][0]
            path[i].append([summ,sub_path[rev-1][j][1]+sub_path[rev-1][j+1][1],copy.deepcopy(sub_path[rev-1][j][2])])
            path[i][j][2].append(triangle[i][j])
        if  i+1 < len(triangle) and sub_path[rev-1][j][0] < sub_path[rev-1][j+1][0]:
            summ = triangle[i][j] + sub_path[rev-1][j+1][0]
            path[i].append([summ,sub_path[rev-1][j+1][1],copy.deepcopy(sub_path[rev-1][j+1][2])])
            path[i][j][2].append(triangle[i][j])
        if  i+1 < len(triangle) and sub_path[rev-1][j][0] > sub_path[rev-1][j+1][0]:
            summ = triangle[i][j] + sub_path[rev-1][j][0]
            path[i].append([summ,sub_path[rev-1][j][1],copy.deepcopy(sub_path[rev-1][j][2])])
            path[i][j][2].append(triangle[i][j])
    sub_path.append(copy.deepcopy(path[i]))
##    print('sub_path',sub_path)
##    print('path',path)
    
#largest sum
'''
sum_list = []
largest_sum = 0
max_x = 0
'''
largest_sum = path[0][0][0]
##sum_list.append(triangle[0][0])
print('The largest sum is:',largest_sum)

#num of path[i]
num_path = path[0][0][1]
print('The number of paths yielding this sum is:',num_path)

#leftmost path[i]
path[0][0][2].reverse()
left_path = path[0][0][2]
print('The leftmost path yielding this sum is:',left_path)

