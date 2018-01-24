import math


################# NOT PLAYING ###############
propa = False
propb = False

if not propa:
        print('hello')

if not ( propa or propb  ):
        print('demorgan11',True)
else:
        print('demorgan12',False)

        
if ( not propa ) and ( not propb ):
        print('demorgan21',True)
else:
        print('demorgan22',False)


propc = True

print('Next two negation laws')

if propc or not propc:
        print(True)
else:
        print(False)


if propc and not propc:
        print(True)
else:
        print(False)


############### NEGATE HEAPS ##############
        
def manynegs(prop,num):
        for i in range(num):
                prop = not prop
        return prop


print('Multiple negations')

print(manynegs(True, 101))


################ NUMBER 8 EQUIVALENCE ON WIKIPEDIA ################





#################  DATA TYPE PLAYING  ################
print('----------------------------------------')

number = 10
numberint = 128
numberlong = 3685974589764576458976457
numberfloat = 3.1415926535897932384626433835729
numbercomp = 5 + 4j



string = 'Now is the time for'
list = [1,'N','I','C',2]
print(list*3)
tuple = (1,3,65,543)
dict = {'Mon': 1, 'day': 2}



        
################ IS PLAYING ####################


if 1 is 1:
        print('not equal')
else:
        print('equal')


print('str' is 'str')
print('stri' is 'str')


print(1 == 1)
print(1 == 2)





############ IS EQUAL DIFFERENCE ################

number2 = number
number3 = number - 1 + 1
number4 = abs(number)

if number is number2:
        print('clone so the same')



if number is number3:
        print('not based on each other')

if number == number3:
        print('equality condition means same')

# FUNCTION DIFFERENCE #
        
if number is number4:
        print('stuff')

if number == number4:
        print('more stuff')




if list is list:
        print('equal lists')



if list is list.append(1):
        print('the same')
else:
        print('not the same')

verity = list.append(4)
if list is verity:
        print('the same')
else:
        print('not the same')



