######   set CANNOT have mutable elements such as dict, set or lists
##### Creat set using 
###   1) using curly braces   set_name = {iteratble items}
###   2) using set function   set_name = set(iteratable items)

# CREATE    EMPTY SET
new_set = set()
print(f' new_set is an empty set:  {new_set}')  # new_set is an empty set:  set()

# CREATE set using curly craces
my_dict = {"one": 1}
print(f'type(my_dict)  {type(my_dict)}  ')

my_list = [10, 20]

test_set = {100, 200}


###### These all create ERRORS
# CANNOT create set wtih dict item
# my_set = { 1, 2, 3, 4, 'a', 'b', my_dict}  
# print(f' my_set  {my_set}')  # ERROR   >>    TypeError: unhashable type: 'dict'

# CANNOT create set with list item
# my_set = { 1, 2, 3, 4, my_list}
# print(f' my_set  {my_set}')   # TypeError: unhashable type: 'list'

# CANNOT create set with another set within
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

# Create set using `set` function
set_f_1 = set("need")
print(f' set_f_1: {set_f_1}' )   # {'d', 'e', 'n'}

set_f_2 = set('122232344455431')   
print(f'  set_f_2 is {set_f_2} ' )   # {'4', '1', '3', '2', '5'}


# ERROR # set_f_3 = set(1122)
# print(f'  set_f_3 is {set_f_3} ')  # TypeError: 'int' object is not iterable

# ERROR
#  set_f_2 = set(1)   #     TypeError: 'int' object is not iterable

# ERROR
# set_f_2( (1,2,3) )    #     TypeError: 'set' object is not callable

# SET ITERATION
for item in set_f_1:
    print(item)
# d
# e
# n

# SET Iteration with ENUMERATE 
for index,item in enumerate(set_f_1):
    print(f'index {index}: item {item} ')
# index 0: item n 
# index 1: item e 
# index 2: item d

# using   'in' to verify if set contains a specific element
print(f" 'd' in set_f_1: {'d' in set_f_1} ")  # 'd' in set_f_1: True
print(f" 'a' in set_f_1: {'a' in set_f_1} ")  # 'a' in set_f_1: False

e_set = set()
print(f' e_set is an empty set {e_set} of type {type(e_set)} ')

# !!!!!! CANNOT   Add to empty set
e_set.add(88)
e_set = e_set.add(99)
print(f' ADD e_set {e_set}')  #  ADD e_set None


# !!!! Sets not iterable, what is returned by print CAN have different order, depends how it is hashed
set2 = set('1233')
set3 = {1,2,3,4,3,3}
print(f' set2 is {set2} ')  # ex set2 is {'1', '3', '2'}   OR  {'2', '1', '3'}   OR   {'2', '3', '1'}, etc.
print(f' set3 is {set3} ')  # set3 is {1, 2, 3, 4}
set2.add(88)
print(f' ADD   now set2 is {set2}')    # print(f' ADD   now set2 is {set2}')
# e_set.add(99)
# print(f' ADD set_list {set2}  e_set {e_set}')  #  ADD set_list None  e_set None

# !!!!!!  CANNOT    YOU can add list to empty set using update method
# set_list = e_set.update([11, 222])
# print(f' UPDATE set_list : {set_list} ')   # UPDATE set_list : None