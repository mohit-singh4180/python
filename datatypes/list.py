
# Creating a List of numbers
List = [10, 20, 14]
# Creating a List of strings and accessing
# using index
List = ["Homes", "For", "Poor"]
print("\nList Items: ")
print(List[0]) 
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Homes', 'For'] , ['Poor']]
print("\nMulti-Dimensional List: ")
print(List)

print(len(List))

# Creating a List with 
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Homes', 4, 'For', 6, 'Poors']

#size of list

print(len(List))

#ADD
List.append(1)
List.append(2)
List.append(4)
#using loop
for i in range(1, 4):
    List.append(i)
    
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print(List)

#Insert at a position in the list
List = [1,2,3,4]
print("Initial List: ")
print(List)
  
# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Test')

print(List)

#extend()

List.extend([8, 'Truth', 'Always'])

print(List)

#Access element of a list
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Test', 'For'] , ['Students']]
# accessing an element from the 
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])

print(List[0]) 
#negative index
List = [1, 2, 'first', 5, 'value',65,66,54,33,6, 'test']
print(List[-1])
print(List[-3]) 

#delete/remove elements from list
List.remove(5)
List.remove(66)
List.remove(List[len(List)-1])
print(List)

#using pop() function
List.pop()
#remove 3rd last value from back
List.pop(3)
print(List)


#slicing a list
List = ['T','E','A','M','S','F',
        'O','R','R','O','M','A','N']
print("Initial List: ")
print(List)
slicedList=List[:5]
print (slicedList)
slicedList=List[8:]
print (slicedList)
slicedList=List[5:8]
print (slicedList)
slicedList=List[-6:-1]
print (slicedList)

#create new list from list
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square)

#Length of list 
from operator import length_hint
# find length/size of list using operator package
length=length_hint(slicedList)
print(length)
#or
print(len(slicedList))