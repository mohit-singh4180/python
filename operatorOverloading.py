# Python program to show use of
# + operator for different purposes.
def operatorOverloading(): 
    print(1 + 2)
 
    # concatenate two strings
    print("Mohit"+" Singh")
    
    # Product two numbers
    print(3 * 4)
    
    # Repeat the String
    print("brothers "*4)

def Main():
    operatorOverloading()
    
if __name__=="__main__":
    Main()
    
    
#Override add method 

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False
obj1=A(1)
obj2=A(3)
obj3="Mohit"
obj4=" Singh"
print(obj1+obj2)
print(obj3+obj4)


        
        