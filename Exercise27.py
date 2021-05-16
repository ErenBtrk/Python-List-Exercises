'''
27. Write a Python program to find the second smallest number in a list.
'''

import random

list1 = [2,4,6,2,8,10,3,1,2,1]

smallest = list1[0]
smallestIndex = 0

for item in list1:
    if(item < smallest):
        smallest = item
        smallestIndex = list1.index(item)

secondSmallest = smallest
print(smallestIndex)

for item in list1:
    if(item > smallest):
        secondSmallest = item

for item in list1:
    if(list1.index(item) == smallestIndex):
        continue
    if(item < secondSmallest):
        secondSmallest = item 

print(list1)        
print(f"Smallest is {smallest}")
print(f"Second smallest is {secondSmallest}")


#################################################################################

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2,2]))
print(second_smallest([2]))