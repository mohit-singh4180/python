#ALL and ANY

list1=[]
list2=[]
for i in range(1,11):
    list1.append(i*4)
    print(list1[i-1])
for i in range(0,10):
    list2.append(list1[i]%5==0)
    print(list2[i])
#print true if atleast 1 true is found
print(any(list2))
#print true if all values are true
print(all(list2))