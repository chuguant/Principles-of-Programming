# Written by Chuguan Tian for COMP9021


# Insert your code here
import sys
##from collections import defaultdict

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
##print('data',data)

#read data
d = []
sub = []
towns = []
for i in range(len(data)):
    d.append(data[i].split())
##print('d',d)
for i in range(len(d)):
    towns.append([int(j) for j in d[i]])
##towns = [[5,20],[15,100],[195,70]]
##towns = [[5,70],[15,100],[1200,20]]
##towns = [[20,30],[40,40],[340,70],[360,60],[720,20],[740,90]]
for i in range(len(towns)-1):
    towns[i].append(towns[i+1][0] - towns[i][0])
sub_fish = towns[0][1]
sub_dis = towns[0][2]
fish_sub_dis = 0
for i in range(1,len(towns)-1):
    sub_fish = sub_fish + towns[i][1]
    fish_sub_dis = sub_fish - sub_dis
    towns[i].append(fish_sub_dis)
    sub_dis = sub_dis + towns[i][2]
##print('towns',towns)

dis = []
fish = []
dis_gap = []
fish_sub_dis_list = []
for i in range(len(towns)):
    dis.append(towns[i][0])
    fish.append(towns[i][1])
for i in range(len(towns)-1):
    dis_gap.append(towns[i][2])
for i in range(1,len(towns)-1):    
    fish_sub_dis_list.append(towns[i][3])
##print('dis',dis)
##print('fish',fish)
##print('dis_gap',dis_gap)
##print('fish_sub_dis_list',fish_sub_dis_list)
#total distance
total_dis = 0
for i in range(len(towns)-1):
    total_dis = towns[i][2] + total_dis
##print('total_dis',total_dis)

#total fish
total_fish = 0
for i in range(len(towns)):
    total_fish = total_fish + towns[i][1]
##print('total_fish',total_fish)

#fish for each town
exp = []
max_q_each = 0
summ_dic = 0
if total_dis >= total_fish:
    m = fish.index(min(fish))
    n = fish_sub_dis_list.index(max(fish_sub_dis_list)) + 2
##    print('\nm',m)
##    print('\nn',n)
    if m == n:
        max_q_each = min(fish)
    else:
        max_q_each = max(fish_sub_dis_list)/n
else:
    max_q_each = (total_fish-total_dis)/len(towns)
print(f'The maximum quantity of fish that each town can have is {int(max_q_each)}.')

