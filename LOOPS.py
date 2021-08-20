#LOOPS

count=10;

while(count>0):
    print(count)
    count=count-2

print("list iteration")
listItem=["list1","list2","list3","list4"]
for item in listItem:
    print(item)
    
# Iterating over a tuple (immutable)
print("tuple iteration")
tupleItem=("tuple1","tuple2","tuple3","tuple4")
for item in tupleItem:
    print(item)
    
# Iterating over a String over characters
print("\nString Iteration")    
s = "TestString"
for i in s :
    print(i)

# Iterating over a dictionary
print("\ndictionary Iteration")    
testdictionary=dict()
testdictionary['x']=123
testdictionary['y']=456
testdictionary['z']=789

if item in testdictionary:
    print("%s %d" %(item, testdictionary[item]))


#Nested LOOPS
for i in range(1,5):
    for j in range(i):
        print(i , end=" ")
    print()


for char in 'mohitsingh':
    if(char=='i' or char=='s'):
        continue
    if(char=='n'):
        break
    print("Current letter ", char)
   
   

# var1 is in the global namespace
var1 = 5
def some_func():
 
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():
 
        # var3 is in the nested local
        # namespace
        var3 = 7

count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()


# Python program showing
# a scope of object
var1=80
def some_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
        global var1 
        var1=var1+10
        print("Inside inner function, value of global var:",var1)
    some_inner_func()
    print("Try printing var from outer function: ",var1)
some_func()


# taking multiple inputs at a time
# and type casting using list() function
x=list(map(int,input("Enter multiple value : ").split()))
print("List of students: ", x)
abcList=list(x)
print(abcList)
for i in range(len(abcList)):
    print(abcList[i])