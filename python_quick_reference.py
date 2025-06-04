# Python Quick Reference for DSA

# List comprehension
print('List comprehension: ')
nums = [1, 2, 3]
squares = [x*x for x in nums]
evens = [x for x in nums if x % 2 == 0]
print(squares) # [1, 4, 9]
print(evens) # [2]

# enumerate()
print('enumerate(): ')
for i, val in enumerate(['a', 'b']): print(i, val)
# 0 a
# 1 b

# zip()
print('zip(): ')
for x, y in zip([1, 2], ['a', 'b']): print(x, y)
# 1 a
# 2 b

# String Slicing
print('String Slicing: ')
s = "abcde"
print(s[::-1]) # reverse - edcba
print(s[:3]) # first 3 - abc

# Dictionaries & Frequency Maps
print('Dictionaries & Frequency Maps: ')
counts = {}
for c in "aabbc":
    counts[c] = counts.get(c, 0) + 1
print(counts) # {'a': 2, 'b': 2, 'c': 1}

# collections Module
print('collections Module: ')
from collections import Counter, defaultdict, deque

Counter("aabbc")      # {'a': 2, 'b': 2, 'c': 1}
d = defaultdict(int)  #default 0
q = deque([1, 2])     # O(1) pops from both ends

print(d)
print(q)

# Sorting
print("Sorting: ")
print(sorted([('a', 2), ('b', 1)], key=lambda x:x[1]))
print(sorted(["apple", "dog"], key=len))

# Sets
print("Sets: ")
set([1, 2, 2])        # {1,2}
1 in set([1, 2, 3])   # True

# Functions & Lambdas
print("Functions & Lambdas: ")
f = lambda x: x * 2
print(f(3))   # 6