orig_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

# function to get keys
# def get_keys(**kw):
#     print(f' kw.keys {kw.keys()} ')

# get_keys( a=1, b=2)  # kw.keys dict_keys(['a', 'b'])


#### SHALLOW COPY method to copy by VALUE
dict_sc = orig_dict.copy()  # makes SHALLOW copy
dict_sc['first'] = 100  # changed value at key 'first'
print(f'  orig_dict >> {orig_dict}')   #  orig_dict >> {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
# print(f'  dict_2 >> {dict_sc} ')       #  dict_2 >> {'first': 100, 'second': 2, 'third': 3, 'fourth': 4}

#### DICT COMPREHENSION method to copy by VALUE
# copy dict using dict comprehension
dict_c = dict( (k,v) for k,v in orig_dict.items() )
print(f' orig orig_dict mem  {id(orig_dict)}  AND copied dict_c mem {id(dict_c)}')  
# ex . . note different mem addresses     
# orig orig_dict mem  140401682401920  AND copied dict_c mem 140401693896064
dict_c['second'] = "TWO" 
print(f' NOW dict_c is {dict_c}')   #  NOW dict_c is {'first': 1, 'second': 'TWO', 'third': 3, 'fourth': 4}

# Function to iterate through k,v tuple pairs
def get_kv(dict_kw):
    # kv_pairs = dict(kv.items())
    for kv_pair in dict_kw.items():
        print(f' key >> {kv_pair[0]} \t value >> {kv_pair[1]}')

    print('')
    for k,v in dict_kw.items():
        print(f' key >> {k}\t:  \tvalue >> {v}')

get_kv(dict_c)
# key >> first    value >> 1
# key >> second   value >> 2
# key >> third    value >> 3
# key >> fourth   value >> 4

# key >> first   :       value >> 1
# key >> second  :       value >> 2
# key >> third   :       value >> 3
# key >> fourth  :       value >> 4