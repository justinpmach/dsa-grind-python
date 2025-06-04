# Playground
# Personal REPL for testing syntax, functions, and tricks.
# Use print() like a microscope

# List comprehension
print('List comprehension: ')
nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
print(squares)  # [1, 4, 9, 16, 25]

# enumerate()
print('enumerate(): ')
names = ['alice', 'bob', 'charlie']
for i, name in enumerate(names):
    print(i, name)
    # 0 alice
    # 1 bob
    # 2 charlie

# zip()
print('zip(): ')
nums = [1, 2, 3]
letters = ['a', 'b', 'c']
for n, l in zip(nums, letters):
    print(n, l)

# sorted() with lambda
print('sorted() with lambda: ')
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_by_key = sorted(pairs, key=lambda x: x[0])
print(sorted_by_key) # [(1, 'a'), (2, 'b'), (3, 'c')]

# String slicing and tricks
# s[start:stop:step]
print('String slicing and tricks: ')
s = "racecar"
print(s[::-1]) # reverse string
print(s[:3]) # 'rac'

# Sets and Dictionaries
print('Sets and Dictionaries: ')
nums = [1, 2, 3, 4]
unique = set(nums)
print(unique) # {1, 2, 3, 4}

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print(freq) # {1: 1, 2: 1, 3: 1, 4: 1}

# collections.Counter and defaultdict
print('collections.Counter and defaultdict: ')
from collections import Counter, defaultdict

cnt = Counter("aabbbc")
print(cnt) # Counter({'b': 3, 'a': 2, 'c': 1})

dd = defaultdict(int)
dd["a"] += 1
print(dd) # defaultdict(<class 'int'>, {'a': 1})

# Sorting with custom logic
print('Sorting with custom logic: ')
words = ["car", "apple", "banana"]
print(sorted(words, key=lambda w: (len(w), w))) # sort by length, then lex -- lexicographical order, which is basically dictionary order