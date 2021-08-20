#is(compare memory location) and ==

list1=[]
list2=[]
list3=list1

print(list1==list2)
print(list1 is list2)
print(list1 == list3)
print(list1 is list3)

#check memory location of lists

print(id(list1))
print(id(list2))
print(id(list3))