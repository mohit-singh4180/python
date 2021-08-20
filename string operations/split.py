#SPlit
line1 = "Geek1 \nGeek2 \nGeek3";
print (line1.split())
print (line1.split(' ', 1))

#slice to check if a string can become empty by recursive deletion

def findPattern(input, pattern):
    if(len(pattern)==0 or len(input)==0):
        return 'true'
    if(len(pattern)==0):
        return 'true'
    
    while(len(input)>0):
        index=input.find(pattern);
        if(index==-1):
            return 'false'
        input=input[0:index]+input[index+len(pattern):]
        return 'true'
    

if __name__ == '__main__':
    input='MOHMOHITIT'
    pattern='MOHIT'
    print(findPattern(input, pattern))

= 