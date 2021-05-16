'''
28. Write a Python program to find the second largest number in a list.
'''

list1 = [2,12,4,6,2,8,10,3,8,10,1,2,1]

largest = list1[0]
largestIndex = 0

for item in list1:
    if(item > largest):
        largest = item
        largestIndex = list1.index(item)

secondLargest = largest

for item in list1:
    if(item < largest):
        secondLargest = item
        break

for item in list1:
    if(list1.index(item) == largestIndex):
        continue
    if(item > secondLargest):
        secondLargest = item

print(list1)        
print(f"Largest is {largest}")
print(f"Second largest is {secondLargest}")

