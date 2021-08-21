#Dictionary holds key:value pair.

# Creating an empty Dictionary
Dict = {}
Dict1={"Name": "Mohit", "EMPID":122333, "test_values":[1,2,3,4,5,6,7,8,9,10]}
print(Dict)
# Creating a Dictionary
# with each item as a Pair
Dict3 = dict([(1, 'Name'), (2, 'Age')])
print(Dict)

# Creating a Nested Dictionary
# as shown in the below image
Dict2 = {1: 'Test', 2: 'abc',
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Python'}}

#ADD/Update
Dict5={}
Dict5[0]="Name"
Dict5[1]="age"
Dict5[2]="company"
Dict5[3]="Address"
Dict5['Mul_val'] = 2, 3, 4
print(Dict5)
#Update
Dict5[2]="address"
print(Dict5)

#access
print(Dict5[2])
print(Dict5['Mul_val'])
print(Dict5.get(3))
#Nested dictionary

# Creating a Dictionary
Dict6 = {'Dict1': {1: 'Python'},
        'Dict2': {'Name': 'Lang'}}
#Accessing nested dictionary
print(Dict6['Dict2']['Name'])

#DEL
del Dict5[2]
print(Dict5)

del Dict6['Dict1'][1]
print(Dict6)
#Using pop() method with index/key

Dict5.pop(3)

print(Dict5)
# Deleting an arbitrary key
# using popitem() function
pop_ele = Dict5.popitem()

print(Dict5)
Dict5.clear()

print(Dict5)


