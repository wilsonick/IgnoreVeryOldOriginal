
import math

#################  DATA TYPE PLAYING  ################
print('----------------- DATA TYPE PLAYING -----------------------')

print('----------------- BOOLEAN PLAYING -------------------')

bools1 = True  # LOL
bools2 = True

if bools1:
    print('boolean')

# Logical operations

def nand(bool1,bool2):
    return not (bool1 and bool2)

def nor(bool1,bool2):
    return not (bool1 or bool2)

def xor(bool1,bool2):
    return ( (bool1 or bool2) and ( not(bool1 and bool2) ) )

print(nand(bools1,bools2))

print(True + False + True + False - False - True)

print('----------------- NUMBER PLAYING ----------------')

# Positives

numint = 10
numlong = 3685974589764576458976457
numfloat = 3.1415926535897932384626433835729
numfloat2 = 123453.0
numcomp = 5 + 4j
numexp1 = 4**10
numexp2 = pow(4,10)
numexp3 = 4**4.5
numsci = 97439e12

print(numint,numlong,numfloat,numfloat2,numcomp,numexp1,numexp2,numsci)

# Negatives

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


# If two are different, 

if numexp1 == numexp2:
    print('pow does nothing different with not is')

if numexp1 is numexp2:
    print('pow does nothing different with is')



# Floor detection

def floorsame(x,y):
    if (x / y == x // y):
        return [True, x/y]
    else:
        return [False, x/y]

print('The answer to floorsame is', floorsame(8,2))


# Various arithmetic using a single variable. 

print(numint + numint)
print(numint / (numint - numint + 1))
print(int( numint / (numint - numint + 1) ))
print(numint % 3)
print(numint % numint)


# Implicit definition. 

numint2 = numint + 1

print(numint2)

print(numfloat + 2 / numint + numint2 - 43)

# It changes the type when combined so it is the most general

print(numint + numfloat)   # Returns a float
print(numint + numfloat2)   # Returns a float
print(numint * numcomp)  # Returns a complex number
print(numsci * numcomp) # Returns a complex number
print(numint + numsci) # Returns ten more than a massive number


print(numfloat > 3)
print( (numint > 3) or (numint < 3) )
print(10 & 4)


# Print out 3 times the powers of 2
shift = 3
for i in range(7):
    print(shift<<i)


sup = 2
sup /= 3

print(sup)

sup *= 4

print(sup)

del sup


numval1 = 5
numval2 = 6
print(numval1 ** numval2)

numval1 **= numval2
print(numval1)

numb = 6
print(numb.bit_length())

print(1.4.is_integer())

print(340.903.hex())


print('----------------- STRING PLAYING ----------------')

string1 = 'Now is the time for all good men to come to the aid of the party. '
string2 = 'Yes Ariel. What is Nic doing?'
string3 = 'Umm... I "dunno". '
string4 = 'He\'s doing other stuff'
string5 = ' 111 @@@ *&$(^$#*(#@&$(@#& 0123456789 '
string6 = '||| -- Start and end -- |||'
string7 = 'hello\b\b'
string8 = '\\ Prog \'hello\' \" hello \"'
string9 = 'Nic was like: FUCK OFF FUCK OFF FUCK OFF'
string10 = 'Peter is a good person. ' * 5
binarynum = '01010011'
binarynum2 = '00101100'
hexnum = '0xff'
notacomment = '''Hello'''
usingperc1 = '%s is a string that is used. ' % ('This')
usingperc2 = '%d is a number that is used. ' % (numint)

# Find the lengths of various strings and do hex and binary. 

print(int(binarynum,2))
print(int(binarynum2,2))
print(int(hexnum,16))
print(int('1f',16))
print(int('0x1f',16))

# Print, slice and so forth. 

print(string4)
print(string1[1:5])
print(string1[10:])
print(string1*2)
print(string3*(len(string3) - 10))
print(string3*(len(string3) - 10))

# Identity test
print(string1)
print(string1[:10] + string1[10:])

# Negative slices. 
print(string1[-14])
print('before' + string1[-4:-10] + 'after') # Wrong way around! New Compiler addition! 
print('before' + string1[-5:-5] + 'after') #Empty slice
print(string1[-10:-4])
print(string1[-5:])
print(string1[:-5])


print(string3*2)  # Pre and post multilying of stings is identical!!!11 
print(2*string3)

print(string1 + string2 + '\n' + 2*(string1 + string2))

print(string1 + string2 + '\n' + 2*(string1 + string2)*2)

print(usingperc1)
print(usingperc2)

print(string7)
print(string8)
print(string9)
print(string10)
print(5 * string10)

print(string2.upper())
print(bin(3).upper())
print(string1.replace('Now','Immediately'))
print('hello'.upper())
print(string1.find('time') + 1)
print('time'.find('time'))




if string1 != string2:
    print('Distinct strings!')


for i in 'halo':
    print(i)
    for j in 'hal':
        print('yo')




print('----------------- LIST PLAYING ----------------')

list1 = [1,'N','I','C',2]
list2 = []
list3 = [[]] * 5
list4 = [] + []
list5 = [1,'N','I','C',2]*4
list6 = ['E','l','l','i','e']
list7 = ['Jules','Ellie','Peter']
list8 = [1,2,4,8,16,32]
list9 = list8
list10 = ['Jules',5,'Barbara',10,'Peter',15]
list11 = [[1,2,3],[4,5,6],[7,8,9]]
list12 = []*10

matrix1 = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],]


print(list1*3)

print(list3)

print(list11)

print(list11[1][1])

print(2*list8)

print(2*list7*2)

print([numint,numint]) # Number variable usage for lists. 

print([1,2,3] + [1,2])

print('N' in list1)
print('K' in list1)

for i in range(len(list8)):
    list8[i] = pow(list8[i],2)
print(list8)


print([i**2 for i in list9])

list11.reverse()
print(list11)

list11.append([3,12,13])
print(list11)

print([1,2,3].reverse()) # Another compiler addition. Should I stop?


# Generate a list of tuples. 

emptylist1 = []
for i in [1,2,3]:
    for j in [3,1,4]:
        if i != j:
            emptylist1.append((i,j))

print(emptylist1)


print(matrix1)
print(matrix1[2][2])

del matrix1[3][2]

print(matrix1)

print(matrix1[3][:].append(1)) # Another use of the compiler addition. I definitely should stop! 

print(matrix1)






print('----------------- SET PLAYING ----------------')

set1 = set(range(20))
set2 = set(['Talkers:','Luma','Ariel'])
set3 = set()
set4 = set(set())
set5 = set1
set6 = set(['Steve','Mark','Peter'])
set7 = set2.copy()

setdiff1 = set(['Peter','will','love','me'])
setdiff2 = set(['Peter','will','always','cherish','me'])

people1 = set(['Peter','Barbara','Sasha','Duncan'])
natnum = set(range(30))
listset = set(list1)



# Using set operations and conditions

if people1.issubset(people1):
    print('proper or not proper?')   # All are subsets of themselves. 

if people1.issubset(natnum):
    print('not a subset')  # Completely different sets are not subsets. 

if setdiff1 <= setdiff1:      # Not proper subset!
    print('Not proper subset?')



# Print a few sets. 
print(natnum)
print(listset)


print('---------- SET OPERATIONS ----------')


set1.add("SUP") # Will print first 20 with sup at end
print(set1)


set2.clear()  # Will print out the empty set since cleared. 
print(set2)


print(set7) # OMG PRINTED OUT AS A DICTIONARY WHEN COPIED!!

print( setdiff1.difference(setdiff2) )  # Set difference one way
print( setdiff2.difference(setdiff1) ) # Set difference the other way

print( setdiff1.intersection(setdiff2) )  # What is shared in common between the sets? 
print(setdiff1 & setdiff2)

print( set6.issubset(set5) )


print('------------ CONDITIONAL SET STUFF  ------------------')

if (set5 == set1):
    print('It Dynamically Alters!')

'''
if (set4 == set6):
    print('Same set with equals')

if (set4 is set6):
    print('Same set with is')
'''

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




print('----------------- BASIC CS PLAYING ----------------')

abc = 1

defg = abc

abc = abc + 1

print(defg)


defg = defg + 1

print(defg)




print('----------------- COMBINED DATA TYPE PLAYING ----------------')


