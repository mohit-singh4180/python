list = [1, 2,3, 4,5, 6,7,8, 9]
#print method

print(' '.join(map(str, list)))
#print using *
print(*list, sep = ", ")

#ITERATION
#using for loop
for i in list:
    print(i)
    
#using length of list
for i in range(len(list)):
    print(list[i])
    
#using while loops
i=0
while (i<len(list)):
    print(list[i])
    i+=1;

list = [1, 2,3, 4,5, 6,7,8, 9]
#using comprehension []
[print(i) for i in list]

#using enumerate-store index-If we want to convert the list into an iterable list of tuples
for i, val in enumerate(list):
    print(i, " ",val)
