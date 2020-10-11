import random
from collections import defaultdict
import time, math

# generate random letters
# letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(100)])
letters = ''.join([random.SystemRandom().choice('abcde') for i in range(20)])
# print(f' letters  {letters}')





n_letters = 'abcdef'
start = 0
end = len(n_letters)
step = 1

my_dict = {}

for item in letters:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 0

print(f' {my_dict}')        



# for i in range(end):
#     value = (start,end, step + i)
#     if my_dict[value]:


# print(f' my_dict   {my_dict}')
