def is_empty(container):
    
    if container:
        print(f' {type(container)} found with {len(container)} item(s)')
    else:
        print(f' empty {type(container)} ')    


# test ith empty containers
list_e = []
dict_e = {}
set_e = set()
tup_e = ()


list_ne = [1]
dict_ne = {1:1}
set_ne = set('1')
tup_ne = (1)

# is_empty(list_c)  #  empty <class 'list'> 
# is_empty(dict_c)  # empty <class 'dict'>
# is_empty(set_c)   # empty <class 'set'>
# is_empty(tup_c)   # empty <class 'tuple'>

def is_empty2(*container):
    for item in container:
        if item:
            print(f' {type(item)} found with {len(item)} item(s)')
        else:
             print(f' empty {type(item)} ')  


is_empty2(list_e, dict_e, set_e, tup_e)              
#  empty <class 'list'> 
#  empty <class 'dict'> 
#  empty <class 'set'> 
#  empty <class 'tuple'>

is_empty2(list_ne, dict_ne, set_ne, tup_ne)              
#  empty <class 'list'> 
#  empty <class 'dict'> 
#  empty <class 'set'> 
#  empty <class 'tuple'>