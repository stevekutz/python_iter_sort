
list_orig = [0, 3, "string", {'one': 'first', 'second': 2}, {10,20,30}, ("tup_1", "tup_2")]
print(f' list-ref >> {list_orig}')
# list-ref >> [0, 3, 'string', {'one': 'first', 'second': 2}, {10, 20, 30}, ('tup_1', 'tup_2')]


### COPY by REFERENCE copies same mem location
# changing one list affects other list
list_c_ref = list_orig
print(f' id list_org >> {id(list_orig)}  id list_c_ref >> {id(list_c_ref)} ')
# SAME mem location
# ex id list_org >> 140302118063744  id list_c_ref >> 140302118063744

list_c_ref[0] = 100
print(f' \t list_orig {list_orig} \n\t list_c_ref  {list_c_ref}')
#       list_orig [100, 3, 'string', {'one': 'first', 'second': 2}, {10, 20, 30}, ('tup_1', 'tup_2')] 
#       list_c_ref  [100, 3, 'string', {'one': 'first', 'second': 2}, {10, 20, 30}, ('tup_1', 'tup_2')]


###  COPY by VALUE creates NEW mem location
# use copy() method
list_2c = list_orig.copy()
print(f'\n\t id list_orig {id(list_orig)}   \t id list_2c {id(list_2c)}')
#       id list_orig 140312154017408            id list_2c 140312155994112

# use list method
list_lm = list(list_orig)
print(f'\n\t id list_orig {id(list_orig)}   \t id list_lm {id(list_lm)}')
#       id list_orig 140312154017408            id list_lm 140312155995264

# use slice method
list_slice_m = list_orig[:]
print(f'\n\t id list_orig {id(list_orig)}   \t id list_slice_m{id(list_slice_m)}')
#       id list_orig 140312154017408            id list_slice_m140312155993024