# in operator

list1=[1,2,3,4,5,6]
list2=[1,2,3]
for i in list1:
    if(i in list2):
        print("Found")
    else:
        print("Not Found")
        
        
#not in 
for i in list1:
    if(i not in list2):
        print("Found")
    else:
        print("Not Found")

#is operator to check type

x=12
if(type(x) is int):
    print("type is integer")
else:
    print("Not integer")
    
#is not operator to check type

x=12
if(type(x) is not str):
    print("type is not string")
else:
    print("Type is string")
    
    