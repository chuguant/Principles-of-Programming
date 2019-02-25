import sys
import copy
##from collections import defaultdict

##file_name = input('Which data file do you want to use?')
try:
    data_file = open('frames_1.txt')
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
rectangle_list = []
for i in data:
    k = i.split()
    sub_rectangle = []
    for j in range(len(k)):
        k[j] = int(k[j])
    sub_rectangle.append([k[0],k[3]])
    sub_rectangle.append([k[2],k[3]])
    sub_rectangle.append([k[0],k[1]])
    sub_rectangle.append([k[2],k[1]])
    rectangle_list.append(sub_rectangle)
rectangle_list_cp = copy.deepcopy(rectangle_list)
delled_rec = []
print('previous rectangle_list',rectangle_list)
for i in range(len(rectangle_list)):
    x1 = rectangle_list[i][0][0]
    y1 = rectangle_list[i][0][1]
    x2 = rectangle_list[i][1][0]
    y2 = rectangle_list[i][1][1]
    x3 = rectangle_list[i][2][0]
    y3 = rectangle_list[i][2][1]
    x4 = rectangle_list[i][3][0]
    y4 = rectangle_list[i][3][1]
##    print('\nx1,y1,x2,y2,x3,y3,x4,y4',x1,y1,x2,y2,x3,y3,x4,y4)
    for j in range(len(rectangle_list)):
        a1 = rectangle_list[j][0][0]
        b1 = rectangle_list[j][0][1]
        a2 = rectangle_list[j][1][0]
        b2 = rectangle_list[j][1][1]
        a3 = rectangle_list[j][2][0]
        b3 = rectangle_list[j][2][1]
        a4 = rectangle_list[j][3][0]
        b4 = rectangle_list[j][3][1]
##        print('a1,b1,a2,b2,a3,b3,a4,b4',a1,b1,a2,b2,a3,b3,a4,b4)
        if rectangle_list[i] == rectangle_list[j]:
            continue
        else:
            if x1 >= a1 and x2 <= a2 and y1 <= b1 and y3 >= b3:
                del_red = rectangle_list[i]
                if del_red not in delled_rec:
                    delled_rec.append(del_red)
##                    print('del_red',del_red)
                    rectangle_list_cp.remove(del_red)
                else:
                    continue
rectangle_list = rectangle_list_cp
print('\nrectangle_list',rectangle_list)
##print('\ndelled_rec',delled_rec)

#Perimeter for one rectangle
def loc_rec(j,rectangle_list):
    a1 = rectangle_list[j][0][0]
    b1 = rectangle_list[j][0][1]
    a2 = rectangle_list[j][1][0]
    b2 = rectangle_list[j][1][1]
    a3 = rectangle_list[j][2][0]
    b3 = rectangle_list[j][2][1]
    a4 = rectangle_list[j][3][0]
    b4 = rectangle_list[j][3][1]
    
def count(rectangle,rectangle_list):
##    print('rectangle_list',rectangle_list)
    x1 = rectangle[0][0]
    y1 = rectangle[0][1]
    x2 = rectangle[1][0]
    y2 = rectangle[1][1]
    x3 = rectangle[2][0]
    y3 = rectangle[2][1]
    x4 = rectangle[3][0]
    y4 = rectangle[3][1]
    rec_count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if len(rectangle_list) == 1:
        return (x2-x1)*2 + (y1-y3)*2
    else:
####################### No.1 count x1 to x2 ########################
        for i in range(x2-x1):
            x = x1 + i
            y = y1
            print('\n(x,y)',(x,y))
            flag = True
            fflag = False
            ffflag = False
            for j in range(len(rectangle_list)):
                a1 = rectangle_list[j][0][0]
                b1 = rectangle_list[j][0][1]
                a2 = rectangle_list[j][1][0]
                b2 = rectangle_list[j][1][1]
                a3 = rectangle_list[j][2][0]
                b3 = rectangle_list[j][2][1]
                a4 = rectangle_list[j][3][0]
                b4 = rectangle_list[j][3][1]
##                print('\nj',j)
##                print('(a1,b1),(a2,b2),(a3,b3),(a4,b4)',(a1,b1),(a2,b2),(a3,b3),(a4,b4))
                if rectangle == rectangle_list[j]:
                    continue
                elif x >= a1 and x <= a2 and y <= b1 and y >= b3:
                    flag = False    
            if flag:
                count1 = count1 + 1
            if x1 >= a1 and x1 <= a2 and y1 <= b1 and y1 >= b3:
                fflag = True
            if not(x2 >= a1 and x2 <= a2 and y2 <= b1 and y2 >= b3):
                ffflag = True
            print('count1',count1)
        if (fflag and count1 != 0) or (count1 == 0 and ffflag):
            count1 = count1 + 1
            print('count11111',count1)
####################### No.2 count x3 to x4 ######################          
        for i in range(x2-x1):
            x = x1 + i
            y = y3
            print('\n(x,y)',(x,y))
            flag = True
            fflag = False
            ffflag = False            
            for j in range(len(rectangle_list)):
                a1 = rectangle_list[j][0][0]
                b1 = rectangle_list[j][0][1]
                a2 = rectangle_list[j][1][0]
                b2 = rectangle_list[j][1][1]
                a3 = rectangle_list[j][2][0]
                b3 = rectangle_list[j][2][1]
                a4 = rectangle_list[j][3][0]
                b4 = rectangle_list[j][3][1]
##                print('\nj',j)
##                print('(a1,b1),(a2,b2),(a3,b3),(a4,b4)',(a1,b1),(a2,b2),(a3,b3),(a4,b4))
                if rectangle == rectangle_list[j]:
                    continue
                elif x >= a1 and x <= a2 and y <= b1 and y >= b3:
                    flag = False 
            if flag:
                count2 = count2 + 1
            if x3 >= a1 and x3 <= a2 and y3 <= b1 and y3 >= b3:
                fflag = True
            if not(x4 >= a1 and x4 <= a2 and y4 <= b1 and y4 >= b3):
                ffflag = True
            print('count2',count2)
        if (fflag and count2 != 0) or (count2 == 0 and ffflag):
            count2 = count2 + 1
            print('count22222',count2)
####################### No.3 count y1 to y3 ######################             
        for i in range(y1-y3):
            x = x1
            y = y1 - i
            print('\n(x,y)',(x,y))
            flag = True
            fflag = False
            ffflag = False            
            for j in range(len(rectangle_list)):
                a1 = rectangle_list[j][0][0]
                b1 = rectangle_list[j][0][1]
                a2 = rectangle_list[j][1][0]
                b2 = rectangle_list[j][1][1]
                a3 = rectangle_list[j][2][0]
                b3 = rectangle_list[j][2][1]
                a4 = rectangle_list[j][3][0]
                b4 = rectangle_list[j][3][1]
##                print('\nj',j)
##                print('(a1,b1),(a2,b2),(a3,b3),(a4,b4)',(a1,b1),(a2,b2),(a3,b3),(a4,b4))
                if rectangle == rectangle_list[j]:
                    continue
                elif x >= a1 and x <= a2 and y <= b1 and y >= b3:
                    flag = False 
            if flag:
                count3 = count3 + 1
            if x1 >= a1 and x1 <= a2 and y1 <= b1 and y1 >= b3:
                fflag = True
            if not(x3 >= a1 and x3 <= a2 and y3 <= b1 and y3 >= b3):
                ffflag = True
            print('count3',count3)
        if (fflag and count3 != 0) or (count3 == 0 and ffflag):
            count3 = count3 + 1
            print('count33333',count3)               
####################### No.4 count y2 to y4 ######################                 
        for i in range(y1-y3):
            x = x2
            y = y1 - i
            print('\n(x,y)',(x,y))
            flag = True
            fflag = False
            ffflag = False            
            for j in range(len(rectangle_list)):
                a1 = rectangle_list[j][0][0]
                b1 = rectangle_list[j][0][1]
                a2 = rectangle_list[j][1][0]
                b2 = rectangle_list[j][1][1]
                a3 = rectangle_list[j][2][0]
                b3 = rectangle_list[j][2][1]
                a4 = rectangle_list[j][3][0]
                b4 = rectangle_list[j][3][1]
##                print('\nj',j)
##                print('(a1,b1),(a2,b2),(a3,b3),(a4,b4)',(a1,b1),(a2,b2),(a3,b3),(a4,b4))
                if rectangle == rectangle_list[j]:
                    continue                
                elif x >= a1 and x <= a2 and y <= b1 and y >= b3:
                    flag = False
                if x2 >= a1 and x2 <= a2 and y2 <= b1 and y2 >= b3:
                    fflag = True
                if not(x4 >= a1 and x4 <= a2 and y4 <= b1 and y4 >= b3):
                    ffflag = True
            if flag:
                count4 = count4 + 1
            print('count4',count4)
        if (fflag and count4 != 0) or (count4 == 0 and ffflag):
            count4 = count4 + 1
            print('count44444',count4)

        rec_count = count1 + count2 + count3 + count4
        return rec_count

#Perimeter for all rectangles
Perimeter = 0
##for i in rectangle_list:
##    Perimeter = Perimeter + count(i,rectangle_list)
c = count([[0, 4], [16, 4], [0, -6], [16, -6]],rectangle_list)
print('\n周长＝34 ',c)
print('Perimeter',Perimeter)
    
