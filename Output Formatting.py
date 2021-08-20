# using  %[flags][width][.precision]type 

print("printing number %3d"%(34))
print("printing number %4d"%(34))
print("printing number %5d"%(34))

#Floating formatting
print("printing number %2d and float %5.2f" %(34,1253.25681))
print("printing number %3d and float %5.3f" %(34,1253.25681))
print("printing number %4d and float %5.4f" %(34,1253.25681))


#format 
print("printing number {} and float {}".format(34,1253.25681))
print("printing number {0} and float {1}".format(34,1253.25681))
print("printing number {1} and float {0}".format(34,1253.25681))
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'.format('My', ' name', other =' is mohit'))
print("Print: {a:5d},  number: {p:8.2f}".format(a = 453, p = 59.058))
print("printing number {0:2d} and float {1:3.4f}".format(34,1253.25681))



#using f string
print(f"printing number {34} and float {1253.25681}")

# Printing the center aligned 
# string with fillchr

cstr = "I love python"
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))