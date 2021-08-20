#Ternary Operator
#Conditional expressions have the lowest priority amongst all Python operations.
a,b=10,20
min =a if a<b else b
print(min)

# if [a<b] is true it return 1, so element with 1 index will print
print( (b, a) [a < b] )

print({True: a, False: b} [a < b])

 
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")