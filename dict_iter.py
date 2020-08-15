import math, random

list_nums = []

for i in range(6):
    list_nums.append(random.randrange(-20,21))

print(list_nums)    

test_dict = dict.fromkeys(list_nums, random.randrange(-6, 6))  # only will make one value for all keys created
print(test_dict)


for k,v in test_dict.items():
    print(f'key {k}: value {v} ')   # ex {-15: 4, -9: 4, 1: 4, 19: 4, 6: 4, -8: 4}

dict_nums = {i: list_nums[i] for i in range(0, len(list_nums))}    
print(dict_nums)    # ex  {0: -15, 1: -9, 2: 1, 3: 19, 4: 6, 5: -8}

for k in test_dict.keys():
    print(f' key: {k} ')

for v in test_dict.values():
    print(f' value: {v}')

# print out tuples of items
for i in dict_nums.items():
    print(i)
    print(f'i[0] {i[0]}  i[1] {i[1]}')


list_str = ['first', 'second', 'third', 'fourth']
list_nums2 = [0, 1, 2, 3]



# CREATE dict from 2 lists
zipObj = zip(list_str, list_nums2)   # iterates through list and returns tuples
dict_merge = dict(zipObj)
print(dict_merge)      # {'first': 0, 'second': 1, 'third': 2, 'fourth': 3}

dict_merge2 = dict(zip(list_str, list_nums2))
print(dict_merge2)     # {'first': 0, 'second': 1, 'third': 2, 'fourth': 3}


# CREATE dict from list of tuples
list_tuples = [("1st", 1), ("2nd", 2), ("3rd", 3) ]
dict_tuples = dict(list_tuples)
print(dict_tuples)

# function to get keys
# def get_keys(**kw):
#     print(f' kw.keys {kw.keys()} ')

# get_keys( a=1, b=2)  # kw.keys dict_keys(['a', 'b'])

dict_merge2 = dict_merge.copy()  # makes copy
print(dict_merge2)
dict_merge3 = dict( (k,v) for k,v in dict_merge.items() )


def get_kv(**kw):
    # kv_pairs = dict(kv.items())
    for k,v in dict(kv.items()):
        print(f' key {k} value {v}')

get_kv(dict_merge2)
        