# def check_type(*vals):
def check_type(vals):
    py_types = {
        bool: ("boolean", "Boolean variable", "an immutable"),
        int: ("integer", "numeric data type", "an immutable"),
        str: ("string", "ordered sequence", "an immutable"),  # Unicode strings
        float: ("float", "numeric data type", "an immutable"),
        complex: ("complex number", "numeric data type", "an immutable"),
        list: ("list", "ordered sequence", "a mutable"),
        tuple: ("tuple", "ordered sequence", "an immutable"),
        bytes: ("bytes", "ordered sequence", "an immutable"), # an an immutable sequence of small integers in the range 0 <= x < 256
        bytearray: ("bytearray", "ordered sequence", "a mutable"), # a mutable sequence of integers in the range 0 <= x < 256
        set: ("set", "unordered collection", "an immutable"),
        frozenset: ("frozens set", "unordered collection", "an immutable"),
        dict: ("dictionary", "unordered collection", "a mutable")
        
        
        }
    
    # sequence types: strings, byte sequences (bytes objects), byte arrays (bytearray objects), lists, tuples, and range objects

    for val in vals:
        # print(val)
        if type(val) in py_types:
            ind = py_types[type(val)]

            print(f' {val} is of type {ind[0]} and is {ind[2]} {ind[1]}')


bool_val = True
int_val = 10
string_val = "sdfsd" 
float_val = 3.14
complex_val = 3 + 4j
list_val = [ 1, "a", ]
tuple_val = (1, "3", True)
bytes_val = b'\x00\xAF' 
bytearray_val = bytearray([2, 3, 5])
set_val = set((11, 22))
frozenset_val = frozenset(set_val)
dict_val = {'a': 1, 'b': 2}

vals = [bool_val, int_val, string_val, float_val, complex_val, list_val, tuple_val, 
    bytes_val, bytearray_val, set_val, frozenset_val, dict_val ]


check_type(vals)
# check_type(bool_val, int_val, string_val)   # goes with def check_type(*vals):

