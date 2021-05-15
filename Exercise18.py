'''
18. Write a Python program to generate all permutations of a list in Python.
'''

# n! / (n-r)!

import itertools
print(list(itertools.permutations(["ali","veli","isa","musa"],2)))

