#comments
"""comments
    in multi line"""
num12 = 34
if(num12>12):
    print("Num is good")
elif(num12>35):
    print("Num is not good....")
else:
    print("Num is great")
    
# Python program to illustrate
# getting input from user
"""name = input("Enter your name: ")
print("hello", name)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = num1 * num2
print("Product is: ", num3)"""

def functionName():
    print("inside function body")
functionName()

def getInteger():
    result=int(input("Enter Integer"))
    return result

def Main():
    print("Started")
    output=getInteger()
    print(output)

# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()

# Python program to illustrate
# a simple for loop
for step in range(5): 
    print(step)


