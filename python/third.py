import math


################# LOGIC PLAYING ###############
propa = False
propb = False
propc = True
propd = False
prope = False

if not propa:
        print('negation')


print('----------------- DE MORGANS LAWS------------')

if not ( propa or propb  ):
        print('demorgan11',True)
else:
        print('demorgan12',False)

        
if ( not propa ) and ( not propb ):
        print('demorgan21',True)
else:
        print('demorgan22',False)




print('---------------- Next two negation laws ----------------')

if propc or not propc:
        print(True)
else:
        print(False)


if propc and not propc:
        print(True)
else:
        print(False)





############### NEGATE MANY TIMES  ##############
        
def manynegs(prop,num):
        for i in range(num):
                prop = not prop
        return prop


print('--------------- Multiple negations ------------------')

print(manynegs(True, 101))


################ IMPLIES FUNCTION ATTEMPT ####################

print('------------------ BOTH IMPLIES ---------------')

def implies(p,q):
        return ( (not p) or (q) )

def implies2(p,q):
        if p and q:
                return True
        if p and not q:
                return False
        if not p and q:
                return True
        if not p and not q:
                return True

print(implies(propa,propb))

print(implies2(propa,propb))


################ IFF FUNCTION ATTEMPT ######################

print('--------------------- ALL iffs! ------------------')

def iff(p,q):
        return ( implies(p,q) and implies(q,p) )

def iff2(p,q):
        if p:
                if q:
                        return True
                else:
                        return False
        else:
                if q:
                        return False
                else:
                        return True

def iff3(p,q):
        if p and q:
                return True
        if p and not q:
                return False
        if not p and q:
                return False
        if not p and not q:
                return True


print(iff( propa , propb ) )

print(iff2( propa , propb ) )

print(iff3( propa , propb ) )

################ NUMBER 8 EQUIVALENCE ON WIKIPEDIA ################

print('----------------- NUMBER 8 TEST ------------------')


if implies(propa,propc) and implies(propb,propc):
        print(True)
else:
        print(False)

if implies( (propa or propb) , propc):
        print(True)
else:
        print(False)


################## NUMBER 3 EQUIVALENCE ON WIKIPEDIA ##################

print('-------------------- NUMBER 3 EQUIVALENCE -------------')


if iff(propa,propb):
        print(True)
else:
        print(False)


if ( propa and propb ) or ( not propa and not propb ):
        print(True)
else:
        print(False)






#################  DATA TYPE PLAYING  ################
print('----------------- DATA TYPE PLAYING -----------------------')

bools = True

number = 10
numberint = 128
numberlong = 3685974589764576458976457
numberfloat = 3.1415926535897932384626433835729
numbercomp = 5 + 4j
numberexp = 4**10
numbersci = 97439e12


string = 'Now is the time for 111 @@@ *&$(^$#*(#@&$(@#& 0123456789 '

list = [1,'N','I','C',2]
print(list*3)

people = set(['Peter','Barbara','Sasha','Duncan'])
natnum = set(range(200))

print(natnum)

tuple = (1,3,65,543)
dict = {'Mon': 1, 'day': 2}




################## PRIME NUMBER PLAYING ####################

print('DIVISOR')

def divis(n):
        divlist = []
        for i in range(1,n+1):
                if (n%i == 0):
                        divlist.append(i)
        return divlist


print(divis(50))

print('---------------------- PRIME NUMBERS ------------------')


def primes(n):
        primeslist = []
        for i in range(1,n):
                if ( divis(i) == [1,i] ):
               # if i % j != 0 and (i/j != 1 or i/j != i):       # If a multiple is found
               # if (i/j == 1) or (i/j == i) or (i/j == j):
                        primeslist.append(i) # Add a prime
        return primeslist

print(primes(30))

print('COMBINED DIVISOR')

def combprimes(n):
        divislist = []
        primeslist = []
        composlist = []
        for i in range(1,n+1):
                if (n%i == 0):
                        divislist.append(i)
        #if ( (n/i == 1) or (n/i == i) ):
        for i in divislist:
                if i == 
                        primeslist.append(i)
                else:
                        composlist.append(i)
        return [primeslist,composlist]

print(combprimes(15))

'''
def is_prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                        return False
        return True

print(is_prime(13))

numbs = 100
primal = []
for i in range(numbs):
        if is_prime(i):
                primal.append(i)

print(primal)
'''


################ IS PLAYING ####################

print('--------------- IS STUFF ---------------')

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



