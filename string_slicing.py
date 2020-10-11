import random
from collections import defaultdict
import time, math

# generate random letters
# letters = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz') for i in range(100)])
letters = ''.join([random.SystemRandom().choice('abcde') for i in range(20)])
# print(f' letters  {letters}')





n_letters = 'abcdabc'
start = 0
end = len(n_letters)
step = 1

my_dict = {}

# for item in letters:
#     if item in my_dict:
#         my_dict[item] += 1
#     else:
#         my_dict[item] = 0

# print(f' {my_dict}')        




print(f' n_letters   {n_letters}')

substr_c = [n_letters[k: i] for k in range(len(n_letters))
            for i in range(k + 1, len(n_letters) + 1)]
print(f' substr_c {substr_c}    {len(substr_c)}')



substr_1 = list()


for k in range(len(n_letters)):
    for i in range(k + 1, len(n_letters) + 1):
        
        substr_1.append(n_letters[k:i])
        # print(f' {n_letters[k:i]}')


print(f' substr_1 {substr_1}    {len(substr_1)}')


s = "abcabcbb"

# def longest_substring_set(str):

#     list_str = []
#     max_len = 0

#     for ch in str:
#         if ch in list_str:
#             del list_str[0:list_str.index(ch) + 1]
        
#         list_str.append(ch)

#         if len(list_str) > max_len:
#             print(f' {list_str}')
#             max_len = len(list_str)

#     return max_len


# print(longest_substring_set(s))


# print(f' my_dict   {my_dict}')
