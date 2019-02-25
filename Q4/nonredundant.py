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
##print('data',data)

#read data
path = []
for i in data:
    path.append((i.replace('R','').replace('(','').replace(',',' ').replace(')','')).split())
##print('path',path)
for i in path:
    for j in range(len(i)):
        i[j] = int(i[j])
##print('path',path)

#get the number linked to each point
##path_each_point = defaultdict(list)
##for i in path:
##    path_each_point[i[1]].append(i[0])
##print('path_each_point',path_each_point)

##for i in path_each_point.keys():
##    print('i',i)
##    for j in path_each_point.keys():
##        print('j',j)
##        for k in range(len(j)):
##            if i == path_each_point[j][k]:
##                path_each_point[i].append
##                print(path_each_point[i][-1])

def path_f(M,L,P,count):
##    print('count',count)
    if P == []:
        P.append(M)
    for i in path:
##        print('\ni',i)
        if M[1] == i[0]:
            P.append(i)
##            print('P',P)
            return path_f(P[-1],L,P,count)
        if count > len(L)-len(P)-1:
            return P
        else:
            continue       
    if len(P) == 1:
        return P
    else:
##        flg = copy.deepcopy(P[-1])
##        print('P[-1]',P[-1])
##        P_cp = copy.deepcopy(P[-1])
        return path_f(P[-1],L,P,count+1)
    
path_each_point = []
for i in path:
    sub_path = []
    count = 0
    path_f(i,path,sub_path,count)
    path_each_point.append(sub_path)
##    print('sub_path',sub_path)
##print('path_each_point',path_each_point)
    
##path_cp = copy.deepcopy(path)
##path_list = []
##for i in path:
##    sub_path = []
##    sub_path.append(i)
##    print('\ni',i)
##    for j in path:
##        print('j',j)
##        if i == j:
##            continue
##        elif i[1] == j[0]:
##            sub_path.append(j)
##        else:
##            continue
##        print('sub_path',sub_path)
##    path_list.append(sub_path)
##print('path_list',path_list)
     
#sort the path
path_each_point_cp = copy.deepcopy(path_each_point)
length = 0
for i in range(len(path_each_point)):
    if len(path_each_point[i]) > length:
        length = len(path_each_point[i])
        longest_path = path_each_point[i]
##print('longest_path',longest_path)

longest_set = {-1}
#longest_path set
for i in longest_path:
    longest_set.add(i[0])
    longest_set.add(i[1])
##print('longest_set',longest_set)

for i in range(len(path_each_point_cp)):
##    print('i',i)
    if path_each_point_cp[i] != longest_path:
        for k in path_each_point_cp[i]:
##            print('k',k)
            if k in longest_path:
                path_each_point[i].remove(k)
    else:
        continue
##print('path_each_point',path_each_point)
for i in range(len(path_each_point_cp)):
##    print('i',i)
    if path_each_point_cp[i] != longest_path:
        for k in path_each_point[i]:
##            print('k',k)
            if k != [] and longest_path[-1][-1] == k[-1]:
                path_each_point[i].remove(k)
    else:
        continue
##print('path_each_point',path_each_point)
for i in range(len(path_each_point_cp)):
    if path_each_point_cp[i] != longest_path:
        for k in path_each_point[i]:
            if k[0] in longest_set and k[-1] in longest_set:
                path_each_point[i].remove(k)
    else:
        continue
##print('path_each_point',path_each_point)
for i in range(len(path_each_point_cp)):
    if [] in path_each_point:
        path_each_point.remove([])
##print('path_each_point',path_each_point)

#print the path
path_print_list = []
for i in path_each_point:
    for j in i:
        path_print_list.append(j)
##print('path_print_list',path_print_list)

path_print_list_sorted = []
for i in path:
    if i in path_print_list:
        path_print_list_sorted.append(i)
##print('path_print_list_sorted',path_print_list_sorted)

#transfer to print
print('The nonredundant facts are:')
for i in path_print_list_sorted:
    t = str(i).replace('[','').replace(']','').replace(' ','')
    print(f'R({t})')
