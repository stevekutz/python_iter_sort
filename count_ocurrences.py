from collections import Counter, defaultdict
from random import randint

import time, math





## the _ is not important enough to define in a variable to be used 
# inside the for loop, therefore, loop just repeats 100 times



target_val = 1
list_nums = []    
    # create list of 50 random integers between 0 and 10
for _ in range(10000000):
        list_nums.append(randint(0, 10))

# print(f' list_nums >> {list_nums}  ')

def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])

def count_occurrences_2(list, val):
    return list.count(val)    

def count_occurrences_3(list, val):
    counted = 0
    i = 0
    
    while i < len(list) - 1:
        if val == list[i]:
            counted += 1
        i += 1    
    yield counted    

def count_occurrences_4(list, val):
    
    count = 0
    for val in filter(lambda x: x == val, list):
        count += 1

    return count    

def count_occurrences_5(list, val):
    
    count = 0
    for x in (y for y in list if y == val):
        count += 1

    return count 



print(f'Time to count specific occurence in list of 10 million integers betwen 0 and 10 using custom count_occurences function')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {count_occurrences(list_nums, target_val)}')
print(f' \t time to run test was {(time.time() - t1)}')

print(f'Time to count specific occurence in list of 10 million integers betwen 0 and 10 using custom count_occurences_2 function')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {count_occurrences_2(list_nums, target_val)}')
print(f' \t time to run test was {(time.time() - t1)}')

print(f'Time to count specific occurence in list of 10 million integers betwen 0 and 10 using count_occurences_3 generator function')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {sum(count_occurrences_3(list_nums, target_val))}')
print(f' \t time to run test was {(time.time() - t1)}')

print(f'Time to count specific occurence in list of 10 million integers betwen 0 and 10 using count_occurences_4 generator function')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {count_occurrences_4(list_nums, target_val)}')
print(f' \t time to run test was {(time.time() - t1)}')

print(f'Time to count specific occurence in list of 10 million integers betwen 0 and 10 using count_occurences_5 generator function')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {count_occurrences_5(list_nums, target_val)}')
print(f' \t time to run test was {(time.time() - t1)}')


print(f' Time to count specific occurences in list of 10 million integers between 0 and 100 using native .count() method')
t1 = time.time()
print(f' \t number of {target_val} in list >>  {list_nums.count(target_val)}')
print(f' \t time to run test was {(time.time() - t1)}')


print(f' Time to count specific occurences in list of 10 million integers between 0 and 100 using Counter')
t1 = time.time()
counted = Counter(list_nums)[1]
print(f' \t number of {target_val} in list >>  {counted}')
print(f' \t time to run test was {(time.time() - t1)}')

print(f' Time to count specific occurences in list of 10 million integers between 0 and 100 using Defaultdict')
t1 = time.time()
counted = defaultdict(int)
for i in list_nums:
    if i == 1:
        counted[1] += 1
print(f' \t number of {target_val} in list >>  {counted[1]}')
print(f' \t time to run test was {(time.time() - t1)}')