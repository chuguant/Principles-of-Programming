# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

'''
L = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
ele_to_keep = [0, 5, 7]
L_1_r = [0, 7, 7, 5]
L_2_r = [0, 7, 5]
L_3_r = [4, 8, 7, 6, 4, 7, 5]
'''

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

# Replace this comment with your code
'''
print('\nThe generated list L is:', L)
print('elements_to_keep:',ele_to_keep)
print('right_L1:',L_1_r)
print('right_L2:',L_2_r)
print('right_L3:',L_3_r)
'''

#element_to_keep
L_etk = sorted(list(set(L)))
#L_cp = L_etk
#print('L_etk is ',L_etk)
#print('L_cp is ',L_cp)
#L_no_dup = sorted(list(L_set))
for i in range(len(L_etk)):
    if i%2 == 0:
        elements_to_keep.append(L_etk[i])
        
'''
        print()
        L_cp.remove(L_etk[i])
        print('',L_etk)
'''
#elements_to_keep = L_etk
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)

#L1
#print('L=',L)
#L_del = []
L_cp1 = L[:]
for i in range(len(L)):
    #print(i,L[i], L)
    if L[i] not in elements_to_keep:
        L_cp1.remove(L[i])
        #L_del.append(L[i])
#print('L_del = ', L_del)
#L_cp1 = L[:]
'''
for i in L:
    if i in L_del:
        L_cp1.remove(i)
        #print('L_del', L_del)
        print('L',L)
'''
L_1 = L_cp1
print('\nHere is L_1:')
print('  ', L_1)
#L_2_s = set(L1)

#L2
L_2 = list(set(L_1))
L_2.sort (key = L_1.index)
print('\nHere is L_2:')
print('  ', L_2)
#L3
'''
L_slice = L
for i in range(len(L)):
    for n in range(len(L)):
        L_slice[i:n+1]
        print('L_slice',L_slice)
L_slice = [L[i:i+3] for i in range(len(L))]
print('L_slice',L_slice)
for i, value in enumerate(L):
    print(i, value)
    '''
'''
L_t = [1,2,3,4,5]
L_slice_5_t = [L_t[i:i+5] for i in range(len(L_t)-4)]
print('\nL_slice 5 pic:',L_slice_5_t)
L_slice_4_t = [L_t[i:i+4] for i in range(len(L_t)-3)]
print('\nL_slice 4 pic:',L_slice_4_t)
L_slice_3_t = [L_t[i:i+3] for i in range(len(L_t)-2)]
print('\nL_slice 3 pic:',L_slice_3_t)
L_sorted = sorted(list(set(L)))
L_slice_2_t = [L_t[i:i+2] for i in range(len(L_t)-1)]
print('\nL_slice 2 pic:',L_slice_2_t)
'''
#print('\n',L.index(7))
#print('\n', L_sorted)

def if_l_sequ(L_x):
    L_x_s = sorted(list(set(L_x)))
    if max(L_x_s) - min(L_x_s) == len(L_x_s) - 1:
        return 1
    else:
        return 0
L_cp2 = L
L_3_candidate = []
for n in range(len(L_cp2),1,-1):
    L_slice = [L_cp2[i:i+n] for i in range(len(L_cp2)+1-n)]
#    print('\nL_slice pic:',L_slice)
    '''
#   for i in range(len(L_cp2) - len_slice - 4):
#        L_slice = [L_cp2[i:i+n]
#    x = len(L_slice)
'''
    #print('\nn =',n)
    #print('\ni =',i)
    
    for m in range(len(L_slice)):
        #print('\nif n =',n)
        #print('\nif i =',i)
        #print('\nif m =',m)
        #print('\nL_slice[m] =',L_slice[m])
        if if_l_sequ(L_slice[m]) == 1:
            L_3_candidate.append(L_slice[m])
            #print('\nright slice: ',L_slice[m])

#print('\nL_3_candidate: ',L_3_candidate)
L_3 = L_3_candidate[0]
        
    
'''
   if if_l_sequ(L) == 1:
        L_3 = L
        break
   else:
'''
#        for n in range(len(L_cp2),2,-1):
#            o_len_slice = len(L_cp2)
#           m = o_len_slice * (o_len_slice - 1) / 2
#           print(o_len_slice, m)
#            L_slice = [L_cp2[i:i+n-1] for i in range(len(L_cp2)-)]
#            for i in range(len(L_cp2)):
#            print('\nL_slice pic:',L_slice)
            
'''
            for i in range(len(L_slice)):
                if if_l_sequ(L_slice[i]) == 1:
                    L_3 = L_slice[i]
                    break
'''
#            print('L_slice',slice)
print('\nHere is L_3:')
print('  ', L_3)


