'''
10. Write a Python program to find the list of words
 that are longer than n from a given list of words.
'''
import re





length = int(input("Please enter lenght of word : "))

string = "Hello.My Name is Yarasa Reis."
stringList = re.findall('\w+', string) #splitting with multiple separators
print(stringList)
longerWords = []


for item in stringList:
    if(len(item) > length):
        longerWords.append(item)

print(longerWords)
