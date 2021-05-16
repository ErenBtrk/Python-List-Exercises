'''
24. Write a Python program to append a list to the second list.
'''

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for item in list2:
    list1.append(item)

print(list1)

########################################################################

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)
