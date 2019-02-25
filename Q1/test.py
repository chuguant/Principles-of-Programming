'''
for i in range(1,len(triangle)):
    max_num = 0
    for j in range(max_x,max_x + 2):
        print('The i is: ',i)
        print('The j is: ',j)
        if triangle[i][j] > max_num:
            max_x = j max_num = triangle[i][j] print('The max_x is:
            ',max_x) print('The max_num is: ',max_num)
        else:
            continue
    sum_list.append(max_num)
'''
'''
sub_sum_list = []
##for i in range(len(triangle)):

for e in sum_list:
    largest_sum = largest_sum + e
    larg
print(sum_list)
'''

'''
leftmost_path = []
for i in range(len(triangle)):
    leftmost_path.append(triangle[i][0])
'''
'''
for _ in range(2**(len(triangle)-1)):
    for i in range(len(triangle)):
        sub_path.append(triangle[i][0])
    print('sub_path',sub_path)
path.append(sub_path)
print('path',path)
'''
'''
        sum_left = triangle[i][j] + triangle[i+1][j]
        sum_right = triangle[i][j] + triangle[i+1][j+1]
        if sum_left >= value:
            summ = sum_left
            value = summ
            path[summ].append(triangle[i+1][j])
            path[summ].append(triangle[i][j])
        else:
            summ = sum_right
            value = sum_right
            path[summ].append(triangle[i+1][j+1])
            path[summ].append(triangle[i][j])
'''
from collections import defaultdict

triangle = {0: [7], 1: [3, 8], 2: [8, 1, 0], 3: [2, 7, 4, 4], 4: [4, 5, 2, 6, 5]}
path = defaultdict(list)
path_cp = defaultdict(list)
left_path = defaultdict(list)
right_path = defaultdict(list)
bot_layer = []
left_sub_path = []
right_sub_path = []
summ = 0
value = 0
count = 0
layer_num = len(triangle)
for i in range(layer_num-1,-1,-1):
    for j in range(len(triangle[i])):
        sub_path = []
        print('\n(i,j)',(i,j))
        if i == layer_num-1:
            sub_path.append(triangle[i][j])
            path[j].append(triangle[i][j])
            path[j].append(sub_path)
        else:
            if path[j][0] > path[j+1][0]:
                summ = triangle[i][j] + path[j][0]
                value = path[j][1]
                del path[j]
                path[j].append(summ)
                path[j].append(value)
                path[j][1].append(triangle[i][j])
            if path[j][0] < path[j+1][0]:
                summ = triangle[i][j] + path[j+1][0]
                path[j].append(summ)
                path[j].append(path[j+1][1])
                path[j][1].append(triangle[i][j])
            if path[j][0] == path[j+1][0]:
                summ = triangle[i][j] + path[j][0]
                value = path[j][1]
                del path[j]
                path[j].append(summ)
                path[j].append(value)
                path[j][1].append(triangle[i][j])
                path[j].append(path[j+1][1])
                path[j][2].append(triangle[i][j])
##        print('\nsub_path',sub_path)
##        print('\nleft_path',left_path)
##        print('\nright_path',right_path)              
##        print('path',path)

print(path)

