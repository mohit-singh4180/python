import math

def Main(): 
    num=-85
    num=math.fabs(num)
    print(num)

if __name__=="__main__":
    Main()
    
#Boolean operation
print (False == 0)
print (True == 1)

#True=1 and False=0
print (True + True + True)
print (True + False + False)

num4=80 or 50 or 30 or 10 or 70 or 40
print(num4)

num5=10 and 20 and 30 and 10 and 70 and 85
print(num5)

trueValue=True
falseValue=False
stringNames="Mohit"
print(stringNames)

if(stringNames == "Mohit" and stringNames != None):
    print("Values did matched")
elif(stringNames == "Mohit" or stringNames == "Rohit"):
    print("Exact Values matched")
else:
    print("Values didn't matched")



nullValue=None;
print(nullValue)
print (None == 0)





