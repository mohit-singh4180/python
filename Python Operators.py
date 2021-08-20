# Examples of Arithmetic Operator 
a = 9
b = 4
# Addition of numbers 
add = a + b 
# Subtraction of numbers 
sub = a - b 
# Multiplication of number 
mul = a * b 
# Division(float) of number 
div1 = a / b 
# Division(floor) of number 
div2 = a // b 
# Modulo of both number 
mod = a % b 
# Power
p = a ** b
# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod)
print(p)

#relational operator
a = 13
b = 33  
# a > b is False
print(a > b)  
# a < b is True
# print(a < b)  
# a == b is False
print(a == b)  
# a != b is True
print(a != b)  
# a >= b is False
print(a >= b)  
# a <= b is True
print(a <= b)


# Examples of Logical Operator
a = True
b = False
  
# Print a and b is False
print(a and b)
  
# Print a or b is True
print(a or b)
  
# Print not a is False
print(not a)

#is and is not are the identity operators both are used 
# to check if two values are located on the same part of the memory.
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3]
b3 = [1,2,3]

print(a1 is not b1)
  
print(a2 is b2)
  
# Output is False, since lists are mutable.
print(a3 is b3)


# in and not in are the membership operators; used 
# to test whether a value or variable is in a sequence.
x = 'God is everywhere'
y = {3:'a',4:'b'}
  
  
print('G' in x)  
print('god' not in x)  
print('God' not in x)
print(3 in y) 
print('b' in y)

