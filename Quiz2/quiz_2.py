# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code

from fractions import Fraction
from decimal import*
#import time

#start = time.clock()

#from fractions import gcd

def is_finite(x,y):
    f = Fraction(x,y)
    nom_f = f.numerator
    dem_f = f.denominator
    dem_f_cp = dem_f
    devider = []
    
    for i in range(10000):
        if dem_f_cp % 2 == 0:
            dem_f_cp = dem_f_cp / 2

    for i in range(10000):
        if dem_f_cp % 5 == 0:
            dem_f_cp = dem_f_cp / 5

    #print('dem_f_cp',dem_f_cp)
    return int(dem_f_cp) == 1

    
'''    
    if int(dem_f_cp) == 1:
        print('has_finite_expansion:',has_finite_expansion)
        return has_finite_expansion == True       
    else:
        print('has_finite_expansion:',has_finite_expansion)
        return has_finite_expansion == False

    for i in range(1,dem_f+1):
        if dem_f % i == 0:
            devider.append(i)
    print('first devider:',devider)

    if len(devider) < 2:
        devider = []
        print('devider<2:',devider)
    else:
        devider.remove(devider[0])
        devider.remove(devider[len(devider)-1])
        if 5 in devider:
            devider.remove(5)
        if 2 in devider:
            devider.remove(2)
    print('end devider:',devider)


    for i in range(len(sigma_l)) and :
        if sigma_l[i] == 0:
            flg_sig_ 
'''

#**********************has_finite_expansion*****************
has_finite_expansion = is_finite(numerator,denominator)
#print('',has_finite_expansion)
#**********************integral_part************************
getcontext().prec = 100
res = Decimal(numerator)/Decimal(denominator)
#res = numerator / denominator
integral_part = numerator // denominator
#print('integral_part:',integral_part)
integral_part_str = str(integral_part)
#***********************sigma & tau************************* 
if has_finite_expansion:
    tau == False
    if res - integral_part == 0:
        sigma == False
    else:
        sigma = str(res - integral_part)[2:]
else:
    outcome = []
    remainder = {0}
    remainder_list = []
    numerator_cp = numerator
    rem = 0
    out_come = 0
    tau_flg = 0
    for i in range(1000000):
        rem = numerator_cp % denominator
        out_come = numerator_cp // denominator
        tau_flg = tau_flg + 1
        outcome.append(out_come)
        remainder_list.append(rem)
        remainder.add(rem)
        numerator_cp = rem * 10
        if tau_flg > len(remainder) - 1:
            index_tau = remainder_list.index(rem)
            num = outcome[index_tau] 
            break
        #print('out_come:',out_come)   

    integral_l = []
    sigma_l = []
    outcome_l = []
    tau_l = []

    #for i in str(integral_part):
#        integral_l.append(i)

    #num_integral = len(integral_l)
    sigma_l = outcome[1:index_tau + 1]
    tau_l = outcome[index_tau + 1:]
    #flg_sig_0 = 0
    if sigma_l != []:
        sigma_str = ''
        for i in sigma_l:
            sigma_str += str(i)
            sigma = sigma_str
#            sigma = int(sigma_str)
        #print('sigma_str=',sigma_str)

    tau_str = ''
    for i in tau_l:
        tau_str += str(i)
        tau = tau_str
#        tau = int(tau_str)
'''
print('\nrem:',rem)
print('num:',num)   
print('outcome:',outcome)
print('remainder:',remainder)
print('remainder_list:',remainder_list)
print('index_tau:',index_tau)
print('tau_flg:',tau_flg)
print('\nintegral_part:',integral_part)
print('Result:',res)
print('sigma:',sigma_l)
print('tau:',tau_l)
print('sigma:',sigma)
print('tau:',tau)
#
'''
if not tau:
    if not sigma:
        integral_part = integral_part_str
    
if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

#end = time.clock()
#print("read: %f s" % (end - start))

