'''
30. Write a Python program to get the frequency of the elements in a list.
'''

list1 = [1,2,3,1,2,1,3,2,1,4,5,7,6,5,4,3,2]
frequencyList = [0 for i in range(8)]

for index in range(len(list1)):
    frequencyList[list1[index]] += 1

for index in range(len(frequencyList)):
    print(f"{index} : {'*'*frequencyList[index]}")
        

