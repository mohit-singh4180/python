#datatypes

a="this is a string"

#list 

listHeterogeneous=["test",1,3+2]
#add element
listHeterogeneous.append("added string")
listHeterogeneous.append("removed string")
#remove element
listHeterogeneous.pop()
#replace at index
#print one element
# listHeterogeneous[2]="rest"
print(listHeterogeneous[2])
#print list
print(listHeterogeneous)

#tuple-? immutable Python objects.

tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])