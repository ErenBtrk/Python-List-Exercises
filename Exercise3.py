'''
3.Write a Python program to get the largest number from a list. 

'''

my_list = [1,5,2,6,7,1,2]

largest = my_list[0]

for item in my_list:
    if(item > largest):
        largest = item

print(largest)
