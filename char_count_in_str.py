import random
from collections import defaultdict, Counter
import time, math

# generate random letters
# letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(100)])
letters = ''.join([random.SystemRandom().choice('abcde') for i in range(2000000)])
# print(f' \nletters  {letters}\n')



# print(f' {my_dict}') 


##################################   using dictionary    >> count with dictionary   took 0.26717114448547363
t1 = time.time()
my_dict = {}

for item in letters:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1

print(f' count with dictionary   took {(time.time() - t1)}')

print(f' {my_dict}') 


##################################   using defaultdict   >> count with defaultdict   took 0.21307921409606934
t1 = time.time()
i_dict = defaultdict(int)

for v in letters:
    i_dict[v] += 1

print(f' count with defaultdict   took {(time.time() - t1)}')    
print(f' {i_dict}') 


##################################   using defaultdict   >> count with defaultdict   took 0.21307921409606934
t1 = time.time()
count = Counter(letters)
print(f' count with Counter   took {(time.time() - t1)}') 
print(f' using Count  {count}')


##################################   using .get   >> count with .get   took 0.2888298034667969
t1 = time.time()
count_dict = dict()

for ch in letters:
    count_dict[ch] = count_dict.get(ch, 0) + 1

print(f' count with .get   took {(time.time() - t1)}') 
print(f' count_dict  {count_dict}')    


##################################   using .count  >>  super long, minutes
t1 = time.time()
count_dict_2 = {x:letters.count(x) for x in letters}

print(f' count with .count   took {(time.time() - t1)}') 
print(f' count_dict  {count_dict_2}')    