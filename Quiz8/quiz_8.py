# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange
from collections import defaultdict
from queue_adt import *
import copy


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
##    path_sub = [(0,0)]
    direction = {'N': (-1, 0),'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    next_directions_first = ['S', 'E']
    next_directions_N = ['E', 'N', 'W']
    next_directions_S = ['W', 'S', 'E']
    next_directions_E = ['S', 'E', 'N']
    next_directions_W = ['N', 'W', 'S']
    Q = Queue(10)
    Q.enqueue(([(0,0)],''))
    if grid[0][0] == 0:
        return None
##    if grid[0][0] == 1 and grid[0][1] == 0 and grid[1][0] == 0:
##        return Q
    while not Q.is_empty():
        (path, previous_direction) = Q.dequeue()
##        print('\n(path, previous_direction)', (path, previous_direction))
##        print('while Q',Q._data)
        cur_posi = path[-1]
##        if len(path) == 1:
##            direction = 'E'
##        elif path[-1][0] == path[-2][0] and path[-1][1] - path[-2][1] == 1:
##            direction = 'E'
##        elif path[-1][0] - path[-2][0] == 1 and path[-1][1] == path[-2][1]:
##            direction = 'S'
##        elif path[-1][0] == path[-2][0] and path[-1][1] - path[-2][1] == -1:
##            direction = 'W'
##        elif path[-1][0] - path[-2][0] == -1 and path[-1][1] == path[-2][1]:
##            direction = 'N'
        if previous_direction == '':
##            print('start')
            for new_direction in next_directions_first:
                new_posi = (cur_posi[0] + direction[new_direction][0],
                                cur_posi[1] + direction[new_direction][1])
                if new_posi[0] not in range(len(grid)) or\
                   new_posi[1] not in range(len(grid)) or\
                   new_posi in path or\
                   not grid[new_posi[0]][new_posi[1]]:
                    continue
                sub_path = list(path)
                sub_path.append(new_posi)
                Q.enqueue((sub_path, new_direction))
##                print(Q._data)
        #E
        if previous_direction == 'E':
##            print('E')
            #up (i-1,j)
            for new_direction in next_directions_E:
                new_posi = (cur_posi[0] + direction[new_direction][0],
                                cur_posi[1] + direction[new_direction][1])
                if new_posi[0] not in range(len(grid)) or\
                   new_posi[1] not in range(len(grid)) or\
                   new_posi in path or\
                   not grid[new_posi[0]][new_posi[1]]:
                    continue
                sub_path = list(path)
                sub_path.append(new_posi)
                Q.enqueue((sub_path, new_direction))
##                print(Q._data)
##            if grid[path[-1][0]-1][path[-1][1]] and\
##               (path[-1][0]-1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]-1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('E 1')
##                print(Q._data)
##            #right (i,j+1)
##            if grid[path[-1][0]][path[-1][1]+1] and\
##               (path[-1][0],path[-1][1]+1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]+1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('E 2')
##                print(Q._data)
##            #down (i+1,j)
##            if grid[path[-1][0]+1][path[-1][1]] and\
##               (path[-1][0]+1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]+1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('E 3')
##                print(Q._data)
        #S
        if previous_direction == 'S':
##            print('S')
            for new_direction in next_directions_S:
                new_posi = (cur_posi[0] + direction[new_direction][0],
                                cur_posi[1] + direction[new_direction][1])
                if new_posi[0] not in range(len(grid)) or\
                   new_posi[1] not in range(len(grid)) or\
                   new_posi in path or\
                   not grid[new_posi[0]][new_posi[1]]:
                    continue
                sub_path = list(path)
                sub_path.append(new_posi)
                Q.enqueue((sub_path, new_direction))
##                print(Q._data)
##            #left (i,j-1)
##            if grid[path[-1][0]][path[-1][1]-1] and\
##               (path[-1][0],path[-1][1]-1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]-1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('S 3')
##                print(Q._data)
##            #down (i+1,j)
##            if grid[path[-1][0]+1][path[-1][1]] and\
##               (path[-1][0]+1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]+1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('S 2')
##                print(Q._data)
##            #right (i,j+1)
##            if grid[path[-1][0]][path[-1][1]+1] and\
##               (path[-1][0],path[-1][1]+1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]+1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('S 1')
##                print(Q._data)
        #W
        if previous_direction == 'W':
##            print('W')
            for new_direction in next_directions_W:
                new_posi = (cur_posi[0] + direction[new_direction][0],
                                cur_posi[1] + direction[new_direction][1])
                if new_posi[0] not in range(len(grid)) or\
                   new_posi[1] not in range(len(grid)) or\
                   new_posi in path or\
                   not grid[new_posi[0]][new_posi[1]]:
                    continue
                sub_path = list(path)
                sub_path.append(new_posi)
                Q.enqueue((sub_path, new_direction))
##                print(Q._data)
##            #up (i-1,j)
##            if grid[path[-1][0]-1][path[-1][1]] and\
##               (path[-1][0]-1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]-1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('W 3')
##                print(Q._data)
##            #left (i,j-1)
##            if grid[path[-1][0]][path[-1][1]-1] and\
##               (path[-1][0],path[-1][1]-1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]-1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('W 2')
##                print(Q._data)
##            #down (i+1,j)
##            if grid[path[-1][0]+1][path[-1][1]] and\
##               (path[-1][0]+1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]+1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('W 1')
##                print(Q._data)
        #N
        if previous_direction == 'N':
##            print('N')
            for new_direction in next_directions_N:
                new_posi = (cur_posi[0] + direction[new_direction][0],
                                cur_posi[1] + direction[new_direction][1])
                if new_posi[0] not in range(len(grid)) or\
                   new_posi[1] not in range(len(grid)) or\
                   new_posi in path or\
                   not grid[new_posi[0]][new_posi[1]]:
                    continue
                sub_path = list(path)
                sub_path.append(new_posi)
                Q.enqueue((sub_path, new_direction)) 
##            #right (i,j+1)
##            if grid[path[-1][0]][path[-1][1]+1] and\
##               (path[-1][0],path[-1][1]+1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]+1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('N 3')
##                print(Q._data)
##            #up (i-1,j)
##            if grid[path[-1][0]-1][path[-1][1]] and\
##               (path[-1][0]-1,path[-1][1]) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0]-1,path[-1][1]))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('N 2')
##                print(Q._data)
##            #left (i,j-1)
##            if grid[path[-1][0]][path[-1][1]-1] and\
##               (path[-1][0],path[-1][1]-1) not in path:
####                path = copy.deepcopy(path)
##                path.append((path[-1][0],path[-1][1]-1))
##                Q.enqueue(path)
##                Q.dequeue()
##                print('N 1')
##                print(Q._data)
##        print(Q._data)
    return path
    # Replace pass above with your code

provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           

