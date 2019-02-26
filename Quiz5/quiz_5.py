# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint

dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(grid[i][j]) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
# Replace this comment with your code
import copy

grid_cp = copy.deepcopy(grid)

#area1
def replace_1_by_star(i,j):
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i:
            replace_1_by_star(i - 1, j)
        if i < dim - 1:
            replace_1_by_star(i + 1, j)
        if j:
            replace_1_by_star(i, j - 1)
        if j <  dim - 1:
            replace_1_by_star(i, j + 1)
            
def replace_0_by_star(i,j):
    if grid[i][j] == 0:
        grid[i][j] = '*'
        if i:
##            print('11111')
            replace_0_by_star(i - 1, j)
        if i < dim - 1:
##            print('22222')
            replace_0_by_star(i + 1, j)
        if j:
##            print('33333')
            replace_0_by_star(i, j - 1)
        if j <  dim - 1:
##            print('44444')
            replace_0_by_star(i, j + 1)

def count_star(dim,grid,count):
    for m in range(dim):
        for n in range(dim):
            if grid[m][n] == '*':
                count = count + 1
    return count

count1 = 0    
if grid[0][0] == 1:
    replace_1_by_star(0,0)
##    print()
##    display_grid()
##    print('grid',grid)
    count1 = count_star(dim,grid,count1)
##    print('count1_1',count1)
else:
    replace_0_by_star(0,0)
##    print()
##    display_grid()
##    print('grid',grid)
    count1 = count_star(dim,grid,count1)
##    print('count_1_0',count1)
size_of_largest_homogenous_region_from_top_left_corner = count1

print()
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
def count_chess_area_1(i,j):
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i:
            count_chess_area_0(i - 1, j)
        if i < dim - 1:
            count_chess_area_0(i + 1, j)
        if j:
            count_chess_area_0(i, j - 1)
        if j <  dim - 1:
            count_chess_area_0(i, j + 1)

def count_chess_area_0(i,j):
    if grid[i][j] == 0:
        grid[i][j] = '*'
        if i:
            count_chess_area_1(i - 1, j)
        if i < dim - 1:
            count_chess_area_1(i + 1, j)
        if j:
            count_chess_area_1(i, j - 1)
        if j <  dim - 1:
            count_chess_area_1(i, j + 1)

count2 = 0
count_2 = 0
for i in range(dim):
    for j in range(dim):
##        print('\n(i,j)',(i,j))
        grid = copy.deepcopy(grid_cp)
##        print()
##        display_grid()
        if grid[i][j] == 1:
            count_chess_area_1(i,j)
##            print()
##            display_grid()
        if grid[i][j] == 0:
            count_chess_area_0(i,j)
##            print()
##            display_grid()
##        print('count_star(dim,grid,count2)',count_star(dim,grid,count2))
        if count_star(dim,grid,count_2) > count2:
            count2 = count_star(dim,grid,count_2)
##            m = i
##            n = j

##        print('count2',count2)
##grid = copy.deepcopy(grid_cp)            
##if grid[i][j] == 1:
##    count_chess_area_1(i,j)
##if grid[i][j] == 0:
##    count_chess_area_0(i,j)
##print()
##display_grid()
##print('count2',count2)
max_size_of_region_with_checkers_structure = count2

print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )




        
    

