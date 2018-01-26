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

numint = 10
numlong = 3685974589764576458976457
numfloat = 3.1415926535897932384626433835729
numfloat2 = 123453.0
numcomp = 5 + 4j
numexp1 = 4**10
numexp2 = pow(4,10)
numsci = 97439e12

print(numint,numlong,numfloat,numfloat2,numcomp,numexp1,numexp2,numsci)

nnumint = -10
nnumlong = -3685974589764576458976457
nnumfloat = -3.1415926535897932384626433835729
nnumfloat2 = -123453.0
nnumcomp = -(5 + 4j)
nnumexp1 = -4**10
nnumexp2 = -pow(4,10)
nnumsci = -97439e12

print(nnumint,nnumlong,nnumfloat,nnumfloat2,nnumcomp,nnumexp1,nnumexp2,nnumsci)

print(12*84/7-9)
print( (

print(numint + numint)
print(numint / (numint - numint + 1))
print(int( numint / (numint - numint + 1) ))
print(numint % 3)
print(numint % numint)



print('----------------- STRING PLAYING ----------------')

string1 = 'Now is the time for 111 @@@ *&$(^$#*(#@&$(@#& 0123456789 '
string2 = 'Yes Ariel? What is Nic doing?'
string3 = 'Umm... I "dunno". '
string4 = 'He\'s doing other stuff'
binarynum = '01010011'
hexnum = '0xff'

print(int(binarynum,2))
print(int(hexnum,16))
print(int('1f',16))
print(int('0x1f',16))

print(string4)


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
#set3 = 

people = set(['Peter','Barbara','Sasha','Duncan'])
natnum = set(range(50))
listset = set(list1)

if people.issubset(natnum):
    print('not a subset')

print(natnum)

print(listset)




print('----------------- TUPLE PLAYING ----------------')

tuple1 = (1,3,65,543)











print('----------------- DICTIONARY PLAYING ----------------')

dict1 = {'Mon': 1, 'day': 2}


