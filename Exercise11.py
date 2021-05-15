'''
11. Write a Python function that takes two lists and returns 
True if they have at least one common member. 

'''

def function(list1,list2):
    for item in list1:
        if(item in list2):
            return True
    return False

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
list3 = [1,2]

print(function(list1,list2))
print(function(list1,list3))