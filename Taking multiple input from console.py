#Taking input from console using split() function input().split(separator, maxsplit)

name= input()
print(name)

# type casting to string
name= str(input())


# type casting to int
abc=10
integerValue=int(abc)
print('type of abc is ',type(abc))
floatValue=float(abc)
print('type of abc is ',type(abc))

# Taking multiple input from user

x,y= input('Enter 2 values').split() #splits with space key
# printing values in same line
print("x  value= {}and y value is  {}".format(x,y))
print("value of x", x)
print("value of y", y)

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking multiple inputs at a time
# and type casting using list() function
x=list(map(int,input("Enter multiple value : ").split()))
print("List of students: ", x)
abcList=list(x)
print(abcList)
for i in range(len(abcList)):
    print(abcList[i])
    
#Using List comprehension 
# taking 2 values
m,n=[int(m) for m in input("Enter multiple value : ").split(",") ]
print("value of m", m)
print("value of n", n)

#Taking multiple values at a time and printing it a s a list
x=[int(x) for x in input("Enter multiple value : ").split() ]
print(x)
#cast as a list
abcList=list(x)
print(abcList)
for i in range(len(abcList)):
    print(abcList[i])

#input multiple string values
x=[str(x) for x in input("Enter multiple value : ").split() ]
print(x)