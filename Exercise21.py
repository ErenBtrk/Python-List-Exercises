'''
21. Write a Python program to convert a list of characters into a string.
'''

list1 = ["y","a","r","a","s","a"]
string = ""

for item in list1:
    string += item
print(string)

########################################################################

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)
