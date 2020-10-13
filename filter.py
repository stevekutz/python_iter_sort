import random
from collections import defaultdict
import time, math


# .join takes item from an iterable and returns a string,   >>>     ''.join(iterable)    '' jujst indicates intial string is empty
# generate random letters
#####   Create list of random chars
rand_chars_list = [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(10)]
letters = ''.join(rand_chars_list)
print(f" inside is a list of random chars  >> {rand_chars_list}")
print(f' letters is list items joined into a string  >>>>>  {letters}')

#########################################################
######     filter  >>>     filter(function, iterable)    returns in iterator object
# An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method.
# Iterable object types includes lists, strings, dictionaries and sets.


# You can loop over an iterable, but you cannot access individual elements directly.
# It’s a container object: it can only return one of its element at the time. 





num_list = [2, 3, 4, 5, 6, 7, 8]
import numbers

def is_odd(val):

    while type(val) == int:

        if val % 2 == 0:
            return True
        elif val % 2 != 0:
            return False

    return f' non-integer value provided'
    

num_val = '2'
print(f' {is_odd(num_val)}')

### returns iterator obj
sol = filter(is_odd, num_list)
print(f' sol is {sol}')   # sol is <filter object at 0x7fd8ed7698b0>

#### returns tuple
sol_tup = tuple(sol)
print(f' sol_tup   {sol_tup}')  # (2, 4, 6, 8)

sol_set = set().update('123')
print(f' sol_set returns    {sol_set} ')



#############
#####   create very long string of random characters
letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(10)])

# for i, item in enumerate(letters):
#     print(f' {i} {item} ')

####################################################################
#####    filter function  typically faster   e.g. filter   took 0.0364832878112793
def vowels(char):
    vowels = set('aeiou')

    if char in vowels:
        # print(f' True ')
        return True
    
    return False    

t1 = time.time()
filtered_vals = list(filter(vowels, letters))
print(f' filter   took {(time.time() - t1)}')


####################################################################
#####    remove is uusally slow for large lists   e.g. filter   took 0.0364832878112793
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



