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
######     filter  >>>     filter(function, iterable)    returns in iterator object of values that test True via a testing function passed in as first argument
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

### filter functions returns iterator obj, assigned to sol here
sol = filter(is_odd, num_list)
print(f' sol is {sol}')   # sol is <filter object at 0x7fd8ed7698b0>
print(f' sol converted to list is   {list(sol)}')
# sol converted to list is   [2, 4, 6, 8]


from itertools import filterfalse
sol_2 = filterfalse(lambda x: x % 2, num_list)
print(f' sol_2 is  {sol_2}')     # sol_2 is  <itertools.filterfalse object at 0x7f882c2ca0d0>
print(f' sol_2 converted to list is   {list(sol_2)}')
# sol_2 converted to list is   [2, 4, 6, 8]



#### convert items from returned iterator into a tuple
sol_tup = tuple(sol)
print(f' sol_tup   {sol_tup}')  # (2, 4, 6, 8)


#### convert items from returned iterator into a set
sol_set = set()
sol_set.update('123')
print(f' sol_set returns    {sol_set} ')    # sol_set returns    {'2', '1', '3'}   









#############
#####   create very long string of random characters
letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(10000)])

# for i, item in enumerate(letters):
#     print(f' {i} {item} ')

####################################################################
#####    filter method  typically faster  than string remove function  e.g. filter function  took 0.0364832878112793 for 1000000

def contains_vowels(char):
    contains_vowels = set('aeiou')

    if char in contains_vowels:
        # print(f' True ')
        return True
    
    return False    

t1 = time.time()
filtered_vals = list(filter(contains_vowels, letters))
print(f' filter method  took {(time.time() - t1)}')


####################################################################
#####    remove method is unusally slow for very large lists   e.g. filter function  ~ took 0.0364832878112793, this takes many minutes
#####    for 10000 chars, filter method  took 0.0036580562591552734 
#####                     remove method took  0.10220789909362793    


letters_2 = list(letters)

t1 = time.time()
for ch in letters_2:
    contains_vowels = set('aeiou')
    
    if ch in contains_vowels:
	    letters_2.remove(ch)

print(f' remove method took  {(time.time() - t1)}')

# print(f' filtered_vals   {filtered_vals} ')


# # for i, item in enumerate(filtered_vals):
# #     print(f' {i} item {item}')


# d_list = defaultdict(int)

# for k in filtered_vals:
#     d_list[k] += 1

# print(f' {sorted(d_list.items())} ')
# #  [('a', 379), ('e', 380), ('i', 381), ('o', 381), ('u', 330)] 



