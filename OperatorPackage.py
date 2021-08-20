import operator

a,b=12,3

print(operator.add(a,b))
print(operator.sub(a,b))
print(operator.mul(a,b))
print(operator.truediv(a,b))
print(operator.floordiv(a,b))
print(operator.pow(a,b))
print(operator.mod(a,b))
print(operator.lt(a,b))
print(operator.gt(a,b))
print(operator.eq(a,b))
print(operator.le(a,b))
print(operator.ge(a,b))
print(operator.ne(a,b))

#LIST functions
list1=[2,4,6,7,8,9,12,14,15,16]
for i in range(0,10):
    print(list1[i],end = " ")
print()
   
operator.setitem(list1,3,5)

for i in range(0,len(list1)):
    print(list1[i],end = " ")
operator.delitem(list1,2)
print()
for i in range(0,len(list1)):
    print(list1[i],end = " ")
    
print()
#print(operator.getitem(list1,3))
operator.setitem(list1,slice(1,4),[12,23,14])
for i in range(0,len(list1)):
    print(list1[i],end = " ")

# using delitem() to delete value at 3rd and 4th index
print()
operator.delitem(list1,slice(2,4))
for i in range(0,len(list1)):
    print(list1[i],end = " ")

#access item at specific by location in list
print()
print(operator.getitem(list1,slice(2,4)))

list2 = [1,2,3,4,5,6,7]

print(operator.concat(list1,list2))

s1="Mohit Singh"
s2="Singh"

print(operator.contains(s1,s2))