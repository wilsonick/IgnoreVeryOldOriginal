############## IMPORT PLAYING ##############
import math
#import pylab


############## GLOBAL PLAYING ###############


def globe():
        global yo
        global hi
        yo = 'sup'

globe()
hi = 'friend'
print(hi)
print(yo)

yo = 'pop'

print(yo)

############### FUNCTION DEFINITION PLAYING ###########
def func():
        return 100

def nothing():
        pass


############### FLOW CONTROL PLAYING #############

######## IF #######

if ((10 - 7) == 3) or (1==2):
        print('Wrong')

if ( ( 6 * 8 ) == 48 ) and ( ( 5 * 12 ) == 60 ):
        print('Sup')


if (func() * 3  == 300):
        print('Wow')


######## ELSE ############
        
if (10 == 8 + 3):
        print('not else')
else:
        print('else')


if (10 == 11):
        print('not elif')
elif (11 == 11):
        print('elif')
else:
        if (2==2):
                print('confusing')
                if (1==1):
                        print('even more confusing')


if (10 == 11):
        print('long elif')
else:
        if (9 == 11):
                print('elif sucks')

########### WHILE ##########
        
while 1==2:
        print('Hi')

i = 1
while (i < 5):
        i += 1
        print('Yay')

        

############# STRING PLAYING ############
print('Py' 'thon')
print('Py' + 'y')
print( 4 * 'SUP')

name = 'Barbara'
if (name[0] == 'B'):
        print('Cool')

print(name[2:6])

if (name[3:5] == 'ba'):
        print('Sliced!')




########### LIST PLAYING ##############
'''
initlist = [1,2,3]
for i in len(initlist):
        initlist[i] = (i**3)
print(initlist)
'''

natural = [1,2,3,4,5]
print([i**2 for i in natural])


for i in [1,2]:
        print('FOR LOOP')



'''        
listy = [[0 for i in range(13)] for j in range(13) ]

for i in range(13):
        for j in range(13):
                listy[i][j] = i*j
                #print(listy[i][j])
                print(str(listy[1][j]) + ' times ' + str(listy[i][1]) + ' = ' +  str(listy[i][j]) )
'''


########### PASS PLAYING ##############
pass
pass
pass
pass
pass
pass
pass

