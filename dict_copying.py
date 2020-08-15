new_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

# function to get keys
# def get_keys(**kw):
#     print(f' kw.keys {kw.keys()} ')

# get_keys( a=1, b=2)  # kw.keys dict_keys(['a', 'b'])

dict_2 = new_dict.copy()  # makes SHALLOW copy
print(dict_2)
dict_2['first'] = 100
print(new_dict)
print(dict_2)

dict_c = dict( (k,v) for k,v in dict_2.items() )


def get_kv(dict_kw):
    # kv_pairs = dict(kv.items())
    for k,v in dict_kw.items():
        print(f' key {k} value {v}')

get_kv(dict_c)