import random
from collections import defaultdict
import time, math

# generate random letters
letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(100000)])

# for i, item in enumerate(letters):
#     print(f' {i} {item} ')


def vowels(char):
    vowels = set('aeiou')

    if char in vowels:
        # print(f' True ')
        return True
    
    return False    

t1 = time.time()
filtered_vals = list(filter(vowels, letters))
print(f' filter   took {(time.time() - t1)}')


letters_2 = list(letters)

t1 = time.time()
for ch in letters_2:
    vowels = set('aeiou')
    
    if ch in vowels:
	    letters_2.remove(ch)

print(f' remove  took {(time.time() - t1)}')

# print(f' filtered_vals   {filtered_vals} ')


# for i, item in enumerate(filtered_vals):
#     print(f' {i} item {item}')


d_list = defaultdict(int)

for k in filtered_vals:
    d_list[k] += 1

print(f' {sorted(d_list.items())} ')
#  [('a', 379), ('e', 380), ('i', 381), ('o', 381), ('u', 330)] 



