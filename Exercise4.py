'''
4. Write a Python program to get the smallest number from a list.
'''

my_list = [1,5,2,6,7,1,2]

smallest = my_list[0]

for item in my_list:
    if(item < smallest):
        smallest = item

print(smallest)