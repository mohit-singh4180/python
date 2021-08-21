#Tuple-->>>>  ()
#Creating an empty Tuple
firstTuple = ()

Tuple1 = (5, 'Welcome', 7, 'Geeks')
print(tuple(Tuple1))

# Creating a Tuple using list
tuple1=tuple("TEST")
print(tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'test')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

Tuple1=("Test "*5)
print(Tuple1)
for i in range(0,5):
    Tuple1=(Tuple1,)
    print(Tuple1)
    
#ACCESS a Tuple
Tuple1 = (0, 1, 2, 3)
print(Tuple1[1])

Tuple2 = ('python', 'test')
a,b,c,d=Tuple1
print(a)
print(b)
print(c)
print(d)

#Concatenation
Tuple3=Tuple1+Tuple2
print(Tuple3)

#Slicing
Tuple4=('TESTING SLICING FUNCTIONALITY')
print(Tuple4[1:])
print(Tuple4[:-1])
print(Tuple4[8:-14])

#Delete -->uples are immutable and hence they do not allow deletion of a part of it.
# #Printing of Tuple after deletion results in an Error.
Tuple1 = (0, 1, 2, 3, 4)
print(Tuple1.index(3))
print(Tuple1.count(3))
del Tuple1
#print (Tuple1)<-- retunr error
