#IN keyword
list1=[1,2,3,4,5]
list2=[6,7,8,9]
for item in list1:
    if(item in list2):
        print("Found")
else:
    print("Not found")

#NOT IN
if(3 not in list1):
    print("Not found")
else:
    print("Found")

#IS
val=13
if(type(val) is int):
    print("Integer value")
if(type(val) is not float):
    print("Not float")
