''' 
Write a Python program to get a list, sorted in increasing order by the last
 element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

my_list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sort_list_last(my_list1))

my_list2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for index in range(len(my_list2)):
    for index2 in range(len(my_list2)):
        if(my_list2[index][1] < my_list2[index2][1]):
            temp = my_list2[index]
            my_list2[index] = my_list2[index2]
            my_list2[index2] = temp

print(my_list2)

