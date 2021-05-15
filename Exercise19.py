'''
19. Write a Python program to get the difference between the two lists.
'''

list1 = [1,2,3,7,9]

list2 = [2,4,6,7,9,10]

diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)