
import string
#String in python//immutable / cannot be deleted/updated
# you can update entire string
name="Mohit Singh"
print(name[0])
print(name[-1])
print(name)

print(name[2:5])

print(name[2:-3])


# Python Program to Update
# entire String
 
String1 = "Hello, I'm a Mohit"
print("Initial String: ")
print(String1)
 
# Updating a String
String1 = "Welcome to the Mohit World"
print("\nUpdated String: ")
print(String1)

#deleting a character or entire string is not allowed

#del name[0]
#print(name)

#Returns the position of the first occurrence of substring in a string
print (name.index("i"))

#partition into tuple items
tupleEg=name.partition("Sin")
print((tupleEg))
print(max(name))

stringName="string@ my name @is @mohit"

# Here '@' is a separator
print(stringName.rpartition('@'))








'''
#Import string header file methods
#use with random to make alphanumeric password
# generate_pass = ''.join([random.choice( string.ascii_uppercase + 
                                            string.ascii_lowercase + 
                                            string.digits) 
                                            for n in range(size)]) '''
print (string.ascii_letters)
print (string.ascii_lowercase)
print (string.ascii_uppercase)
print (string.digits)
print (string.hexdigits)
print (string.punctuation)
print ("\n"+ string.printable)

text = "homes for mohit."
  
# start parameter: 10
result = text.endswith('mohit.', 10)
print(result)  
# start parameter: 10
result = text.startswith('homes')
print(result)

result=text.isalpha()
print(result)
text="1235685"
result=text.isdecimal()
print(result)

#indexof
initialString= "Hello brother how are you"
searchIndexString="how"
pos=initialString.index(searchIndexString)
print(pos)

# using isspace
value=initialString.isspace()
value2=initialString.swapcase()
print(value)
print(value2)
print(initialString.replace("H", "T"))








#find length of AC type bits 
voltages = ["001101 AC", "0011100 DC", "0011100 AC", "001 DC"] 
type="AC"
sum=0

for i in voltages:
    ch=i;
    if(ch[len(ch-2)]!="D"):
        bit_len=ch.index(type)-1
        sum=sum+bit_len
print("Total AC vol"+sum)
