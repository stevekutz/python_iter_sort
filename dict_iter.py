import math, random

list_nums = []

# Create list with random ints from -20 to 20
for i in range(6):
    list_nums.append(random.randrange(-20,21))

print(list_nums)    # ex [-20, -3, 20, -11, -2, -20]

# test_dict = dict.fromkeys(list_nums, random.randrange(-6, 6))  # only will make one value for all keys created
# print(test_dict)


# for k,v in test_dict.items():
#     print(f'key {k}: value {v} ')   # ex {-15: 4, -9: 4, 1: 4, 19: 4, 6: 4, -8: 4}  NOTE value is same for all

# dict comprehension to build dict with values from list
dict_nums = {i: list_nums[i] for i in range(len(list_nums))}    
print(dict_nums)    # ex {0: 16, 1: 13, 2: -1, 3: -2, 4: 13, 5: -13}

# loop to do same thing as previous dict comprehension
dict_nums2 = {}
for i in range(len(list_nums)):
    dict_nums2[i] = list_nums[i]  
print(dict_nums2)    # ex {0: 16, 1: 13, 2: -1, 3: -2, 4: 13, 5: -13} 


# list comprehension to build list of keys
key_list = [ (f"key --> {k}") for k in dict_nums.keys()]
print(f' \t list COMP  key_list: {key_list} ')  # ex list COMP [' val = -18', ' val = 4', ' val = 12', ' val = 14', ' val = 20', ' val = 17']  

# loop to do same thing as previous list comprehension
key_list2 = []
for k in dict_nums.keys():
    key_list2.append(f"key >> {k}")
print(f' \t LOOP key_list: {key_list2} ')  # ex LOOP value_list: [' val== -18', ' val== 4', ' val== 12', ' val== 14', ' val== 20', ' val== 17']


# list comprehension to build list of values
value_list = [f" val = {val}" for val in dict_nums.values() ]
print(f' list COMP {value_list}')  # ex list COMP kv ['i[0] 0 , i[1] -18 ', 'i[0] 1 , i[1] 4 ', 'i[0] 2 , i[1] 12 ', 'i[0] 3 , i[1] 14 ', 'i[0] 4 , i[1] 20 ', 'i[0] 5 , i[1] 17 ']

# loop to do same as previous list  comprehension
value_list2 = []
for v in dict_nums.values():
    value_list2.append(f' val== {v}')
print(f' LOOP value_list: {value_list2}')    # ex LOOP kv pairs ['i[0] 0   i[1] -18', 'i[0] 1   i[1] 4', 'i[0] 2   i[1] 12', 'i[0] 3   i[1] 14', 'i[0] 4   i[1] 20', 'i[0] 5   i[1] 17']  


# list comprehension to capture kv pairs
kv_list = [ f'i[0] {i[0]} , i[1] {i[1]} ' for i in dict_nums.items()  ]
print(f' \t list COMP kv {kv_list}')    # ex list COMP kv ['i[0] 0 , i[1] 2 ', 'i[0] 1 , i[1] 12 ', 'i[0] 2 , i[1] -1 ', 'i[0] 3 , i[1] -16 ', 'i[0] 4 , i[1] -6 ', 'i[0] 5 , i[1] 3 ']

# loop to capture kv pairs
kv_list2 = []
for i in dict_nums.items():
    kv_list2.append(f'i[0] {i[0]}   i[1] {i[1]}')
print(f' \t LOOP kv pairs {kv_list2} ')   # LOOP kv pairs ['i[0] 0   i[1] -18', 'i[0] 1   i[1] 4', 'i[0] 2   i[1] 12', 'i[0] 3   i[1] 14', 'i[0] 4   i[1] 20', 'i[0] 5   i[1] 17'] 


# loop to print out tuples of items
# for i in dict_nums.items():
#     print(i)
#     print(f'i[0] {i[0]}  i[1] {i[1]}')


# CREATE dict from 2 lists
list_str = ['first', 'second', 'third', 'fourth']
list_nums2 = [1, 2, 3, 4]

zipObj = zip(list_str, list_nums2)   # iterates through list and returns tuples
dict_merge = dict(zipObj)
print(f' dict_merge {dict_merge}')      # dict_merge {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

dict_merge2 = dict(zip(list_str, list_nums2))
print(f' dict_merge2 {dict_merge2}')     # dict_merge2 {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}


# CREATE dict from list of tuples
list_tuples = [("1st", 1), ("2nd", 2), ("3rd", 3) ]
dict_tuples = dict(list_tuples)
print(f' dict_tuples  {dict_tuples}')

# function to get keys
# def get_keys(**kw):
#     print(f' kw.keys {kw.keys()} ')

# get_keys( a=1, b=2)  # kw.keys dict_keys(['a', 'b'])


        