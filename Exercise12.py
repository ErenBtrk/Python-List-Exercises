'''
Write a Python program to print a specified list after removing the 0th,
 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

'''

del_index =[0,4,5]

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

while len(del_index) != 0:
    index = del_index[0]
    my_list.remove(my_list[index])
    del del_index[0]
    for item in range(len(del_index)):
        del_index[item] -= 1

print(my_list)

################################################################################################

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

