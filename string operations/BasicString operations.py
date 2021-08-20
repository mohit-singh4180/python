#String operations

String1 = "MOHITSINGH"
print("Initial String: ")
print(String1)
 
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#slicing range of characters
print(String1[1:-1])

#In Python, Updation and deletion of characters from a String is not allowed.
#String1[0]='R'
del String1[0];
print(String1)

#we can update whole string with
String1='Rohit Sharma'
print(String1)
del String1

# Escape Sequencing of String
 
# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)
 
# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)
 
# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)
 
# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)




#Formatter

# Formatting of Strings
 
# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
 
# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life')
print("\nPrint String in order of Keywords: ")
print(String1)


#decimal to binary

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)
 
 
 
# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Test','our','Events')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)
 
# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("TestOurEvents", 2009)
print(String1)