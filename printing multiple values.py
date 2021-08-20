#output/printing multiple values
# taking multiple inputs at a time
# and type casting using list() function
x=list(map(int,input("Enter multiple value : ").split()))
print("List of students: ", x,sep="#")
abcList=list(x)
print(abcList)
for i in range(len(abcList)):
    print(abcList[i])
    
   # This line will automatically add a new line before the
# next print statement
print ("Printing operation 1")
 
# This print() function ends with "**" as set in the end argument.
print ("Printing operation 2 with end parameter", end= "**")

import time
count_second=3
for i in reversed(range(count_second+1)):
    if(i>0):
        print(i, end=">>>",flush=True)
        time.sleep(1)
    else:
        print("start")
        
#Remove soft spaces
print('G', 'F', 'G', sep ='')
print('G', 'F', 'G')

#print in same line

print("1st line ", end=" ")
print("2nd line ")

a =[1,2,3,4,5,6,7,8,9]

for i in range(9):
    print(a[i],end = " ")
#convert into list and iterate and print in  same line
b=list(a)
for i in range(len(b)):
    print(b[i],end = " ")


l=[1,2,3,4,5,6]
# using * symbol prints the list
# elements in a single line
print(*l)
 #Sep parameter
print('A','B', sep='', end='')
print('C')
#\n provides new line after printing the year
print('09','12','2016', sep='-', end='\n') 
print('Mohit','Singh', sep='', end='@')
