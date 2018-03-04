import math


#################  DATA TYPE PLAYING  ################
print('----------------- DATA TYPE PLAYING -----------------------')

print('----------------- BOOLEAN PLAYING -------------------')

bools1 = True  # LOL
bools2 = True

if bools1:
    print('boolean')

def nand(bool1,bool2):
    return not (bool1 and bool2)

def nor(bool1,bool2):
    return not (bool1 or bool2)

def xor(bool1,bool2):
    return ( (bool1 or bool2) and ( not(bool1 and bool2) ) )

print(nand(bools1,bools2))

print('----------------- NUMBER PLAYING ----------------')

#Positives

numint = 10
numlong = 3685974589764576458976457
numfloat = 3.1415926535897932384626433835729
numfloat2 = 123453.0
numcomp = 5 + 4j
numexp1 = 4**10
numexp2 = pow(4,10)
numsci = 97439e12

print(numint,numlong,numfloat,numfloat2,numcomp,numexp1,numexp2,numsci)

#Negatives

nnumint = -10
nnumlong = -3685974589764576458976457
nnumfloat = -3.1415926535897932384626433835729
nnumfloat2 = -123453.0
nnumcomp = -(5 + 4j)
nnumexp1 = -4**10
nnumexp2 = -pow(4,10)
nnumsci = -97439e12

print(nnumint,nnumlong,nnumfloat,nnumfloat2,nnumcomp,nnumexp1,nnumexp2,nnumsci)


# Order of operations. 

print(12 * 84/ 7 - 9)
print( ( (3**2 + 5) * 3 ) - 6 + 5 )
print( ( ( 84 / 7 )**2 - 9) * 4 + 4)
print( (8*2**2 - 8) - 2 * 10 )
print( 3 - 10 * (4-3)**3 + 10)

# Basic operations. 
print(--numint)
print(-------numint)




# Various arithmetic using a single variable. 

print(numint + numint)
print(numint / (numint - numint + 1))
print(int( numint / (numint - numint + 1) ))
print(numint % 3)
print(numint % numint)


# Implicit definition

numint2 = numint + 1

print(numint2)

print(numfloat + 2 / numint + numint2 - 43)



print('----------------- BASIC CS PLAYING ----------------')

abc = 1

defg = abc

abc = abc + 1

print(defg)


defg = defg + 1

print(defg)



print('----------------- STRING PLAYING ----------------')

string1 = 'Now is the time for 111 @@@ *&$(^$#*(#@&$(@#& 0123456789 '
string2 = 'Yes Ariel? What is Nic doing?'
string3 = 'Umm... I "dunno". '
string4 = 'He\'s doing other stuff'
binarynum = '01010011'
binarynum2 = '00101100'
hexnum = '0xff'

print(int(binarynum,2))
print(int(binarynum2,2))
print(int(hexnum,16))
print(int('1f',16))
print(int('0x1f',16))

print(string4)
print(string1[1:5])
print(string1[10:])
print(string1*2)
print(string3*len(string3))
print(string3*(len(string3) - 4))


print('----------------- LIST PLAYING ----------------')

list1 = [1,'N','I','C',2]
list2 = []*10
list3 = [[]] * 5
list4 = [] + []
print(list1*3)

print([numint,numint])


print('----------------- SET PLAYING ----------------')

set1 = set(range(20))
set2 = set(['Talkers:','Luma','Ariel'])
set3 = set()
set4 = set(set())
set5 = set1
set6 = set(set())

people1 = set(['Peter','Barbara','Sasha','Duncan'])
natnum = set(range(30))
listset = set(list1)

if people1.issubset(natnum):
    print('not a subset')

print(natnum)

print(listset)


set1.add("SUP")
print(set1)


if (set5 == set1):
    print('It has changed!')

if (set4 == set6):
    print('Same set with equals')

if (set4 is set6):
    print('Same set with is')

print(set1,set4)






print('----------------- TUPLE PLAYING ----------------')

tuple1 = (1,3,65,543)











print('----------------- DICTIONARY PLAYING ----------------')

dict1 = {'Mon': 1, 'day': 2}
dict2 = {}
dict3 = {'red','green','blue'}

people1 = {'Peter','Barbara','Sasha','Duncan'}


print('----------------- LITTLE LAMBDA CALCULUS PLAYING ----------------')

v = lambda u,a,t : u + a*t
print(v(0,3e5,100))




print('----------------- COMBINED DATA TYPE PLAYING ----------------')


