######   set CANNOT have mutable elements such as dict, set or lists

# create a set  
my_dict = {"one": 1}
print(f'type(my_dict)  {type(my_dict)}  ')

my_list = [10, 20]

test_set = {100, 200}

# my_set = { 1, 2, 3, 4, 'a', 'b', my_dict}  
# print(f' my_set  {my_set}')  # ERROR   >>    TypeError: unhashable type: 'dict'

# my_set = { 1, 2, 3, 4, my_list}
# print(f' my_set  {my_set}')   # TypeError: unhashable type: 'list'

# my_set = { 1, 2, 3, 4, test_set}
# print(f' my_set  {my_set}')   # TypeError: unhashable type: 'set'

# create a set with nums, tuple, and str
my_set = {1, 2, 3, (100, 200), 'apple'}
print(f' my_set is {my_set} ') #  my_set is {1, 2, 3, (100, 200), 'apple'}

# list_set = [ type(val) for val in set]
# print(list_set)  # TypeError: 'type' object is not iterable

# list_set_type = []
# for val in my_set:
#     list_set_type.append(type(val))

# print(list_set_type)    # <class 'int'>, <class 'int'>, <class 'int'>, <class 'str'>, <class 'tuple'>]