#SET---? unordered collection of data type that is iterable, mutable and has no duplicate element
obj1=set()
obj2=set("Test")
# Creating a Set with the use of a List
obj3=set(["test","one day","t20"])
for i in range (1,5):
    print (obj3)

#ADD
obj3.add("limited over")
obj3.add((6,7))
for i in range (1,2):
    print (obj3)

#UPDATE -->For addition of two or more elements Update() method is used.
set1 = set([ 4, 5,45,44,332,3,4, (6, 7)])
set1.update([10, 11])
print(set1)


#Accessing a Set
# Accessing element using for loop
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
    
# Checking the element using in keyword
print(5 in set1)   

#remove() method or discard() method
#Delete->KeyError arises if element doesn’t exist in the set.
#discard -> no error is returned if element is not found
#pop()
set1.remove(5)
set1.discard(10)
for i in set1:
    print(i, end=" ")
print("\n")
set1.pop()   
set1.pop()   
for i in set1:
    print(i, end=" ")

print("\n")

#clear() ->clear set
set1.clear()
print(set1, end="\n")

#Frozen sets in Python are immutable objects
test="a","b","c"
fSet=frozenset(test)
print(fSet, end="\n")