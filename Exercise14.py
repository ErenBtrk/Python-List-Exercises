'''
14. Write a Python program to print the numbers of a specified list
 after removing even numbers from it.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]

for item in list1:
    if(item % 2 == 0):
        list1.remove(item)

print(list1)

########################################################################

num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)