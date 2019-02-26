# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict

def is_ok(matrix,i,y,dim):
    size = 0
    exit_flg = False
    loop2_flg = False
    #size_num = []
    if i not in range(1,dim-1) or y not in range(0,dim-1) or matrix[y][i] == 0:
        #print(range(1,dim-1),range(1,dim-1),matrix[y][i])
        return False 
    else:
        for j in range(y,dim):
            if exit_flg == True:
                break
            else:
                size = size + 1
                col_range = size - 1
                '''
                print('\nsize loop:',size)
                print(f'\ncol_range:',col_range)
                print('\n22222')
                '''
                if i - col_range >= 0 and i + col_range <= dim-1:
                    for col in range(0,size):
                        '''
                        print('\n(i,j):',(i,j))
                        print(f'grid[{i}][{j}]:',matrix[j][i])
                        print('col:',col)
                        print(f'grid[{i}-{col}][{j}]:',matrix[j][i-col])
                        print(f'grid[{i}+{col}][{j}]:',matrix[j][i+col])
                        '''
                        if matrix[j][i-col] == 0 or\
                           matrix[j][i+col] == 0 or\
                           i not in range(0,dim) or\
                           i-col not in range(0,dim) or\
                           i+col not in range(0,dim) or\
                           j not in range(0,dim):
                            size = size - 1
                            exit_flg = True
                            #print('\n11111')
                            '''
                            print(f'matrix[{i}-{col}][{j}] == 0',matrix[j][i-col] == 0)
                            print(f'matrix[{i}+{col}][{j}] == 0',matrix[j][i+col] == 0)
                            print(f'{i} not in range(0,{dim})',i not in range(0,dim))
                            print(f'{i}-{col} not in range(0,{dim})',i-col not in range(0,dim))
                            print(f'{i}+{col} not in range(0,{dim})',i+col not in range(0,dim))
                            print(f'{j} not in range(0,{dim})',j not in range(0,dim))
                            '''
                            break
                else:
                    size = size - 1
                    #print('\n33333')
                    break
    #print('\nsize:',size)
    if size <= 1:
        #print('\nsize <= 1',size <= 1)
        return False
    else:
        if exit_flg == True or j == dim-1 or loop2_flg == False:
            return size
        else:
            return size-1
                                    
        
def convert_grid_90(old_grid):
    old_grid.reverse()
    new_grid = [[j[i] for j in old_grid] for i in range(len(old_grid[0]))]
    return(new_grid)
    
def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
        #print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid))))

def triangles_in_grid(matrix,dim):
    triangles_in_grid = {'N':[],'E':[],'S':[],'W':[]}

    #North
    transfer = []
    
    for i in range(0,dim):
        for j in range(0,dim):
            if is_ok(matrix,i,j,dim) != False:
                transfer.append(is_ok(matrix,i,j,dim))
                transfer_l = list(set(transfer))
                #print(f'\nsize(grid_north,{i},{j})',is_ok(matrix,i,j,dim))
                
    for item in transfer_l:
        if transfer.count(item) != 0:
            triangles_in_grid['N'].append([item,transfer.count(item)])
        
    #print('\ntransfer:',transfer)
    #print('transfer_l:',transfer_l)
    
    #West
    transfer = []
    grid_w = convert_grid_90(matrix)
    #print('grid_w',grid_w)
    #print('\n')

    '''
    for i in range(len(grid_w)):
        print('   ', ' '.join(str(grid_w[i][j]) for j in range(len(grid_w))))
    '''
    '''
    a = is_ok(grid_w,2,1,dim)
    print(a)
    '''
    
    for i in range(0,dim):
        for j in range(0,dim):
            if is_ok(grid_w,i,j,dim) != False:
                transfer.append(is_ok(grid_w,i,j,dim))
                transfer_l = list(set(transfer))
                #print(f'\nsize(grid_west,{i},{j})',is_ok(grid_w,i,j,dim))
                
    for item in transfer_l:
        if transfer.count(item) != 0:
            triangles_in_grid['W'].append([item,transfer.count(item)])

    #South
    transfer = []
    grid_s = convert_grid_90(grid_w)
    #print('grid_w',grid_w)
    #print('\n')
    '''
    for i in range(len(grid_s)):
        print('   ', ' '.join(str(grid_s[i][j]) for j in range(len(grid_s))))
    '''
    '''
    a = is_ok(grid_s,2,1,dim)
    print(a)
    '''
    for i in range(0,dim):
        for j in range(0,dim):
            if is_ok(grid_s,i,j,dim) != False:
                transfer.append(is_ok(grid_s,i,j,dim))
                transfer_l = list(set(transfer))
                #print(f'\nsize(grid_south,{i},{j})',is_ok(grid_s,i,j,dim))
                
    for item in transfer_l:
        if transfer.count(item) != 0:
            triangles_in_grid['S'].append([item,transfer.count(item)])

    #East
    transfer = []
    grid_e = convert_grid_90(grid_s)
    #print('grid_w',grid_w)
    #print('\n')
    '''
    for i in range(len(grid_e)):
        print('   ', ' '.join(str(grid_e[i][j]) for j in range(len(grid_e))))
    '''
    '''
    a = is_ok(grid_s,2,1,dim)
    print(a)
    '''
    for i in range(0,dim):
        for j in range(0,dim):
            if is_ok(grid_e,i,j,dim) != False:
                transfer.append(is_ok(grid_e,i,j,dim))
                transfer_l = list(set(transfer))
                #print(f'\nsize(grid_east,{i},{j})',is_ok(grid_e,i,j,dim))
                
    for item in transfer_l:
        if transfer.count(item) != 0:
            triangles_in_grid['E'].append([item,transfer.count(item)])
    
    return triangles_in_grid
    # Replace return {} above with your code

'''
list = [1,2,3,4,5,6,7,5,4,3,2,12]
set  = set(list)
dict = {}

for item in set:
    dict.update({item:list.count(item)})
'''    

# Possibly define other functions
try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()    
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
'''
grid = [[3, 4, 0, 2, 3], [3, 8, 5, 2, 1], [1, 6, 7, 3, 4], [1, 2, 6, 3, 2], [3, 0, 2, 3, 2]]
dim = 5
'''
print('Here is the grid that has been generated:')
display_grid()

# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
'''
b = []
for i in range(0,5):
    for j in range(0,5):
        c = {(i,j):is_ok(grid,i,j,dim)}
        b.append(c)
print(b)
'''

triangles = triangles_in_grid(grid,dim)

#print('\ntriangles:',triangles)

for d in 'NESW':
    triangles[d].reverse()

#print('\ntriangles:',triangles)

#triangles = {'N':[[3,2],[1,3]],'E':[[6,1],[8,2],[4,2]],'S':[[4,1]],'W':[[2,1]]}

for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    if triangles[direction] != []:
        print(f'\nFor triangles pointing {direction}, we have:')
        for size, nb_of_triangles in triangles[direction]:
            triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
            print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')


