# list of common collections
list = [0, 2, "apple", {"key_name": "first_value"}, {0, 1, 2}, ("zero", "one")]
for index, item in enumerate(list): # must have index first with enumerate
    print(f' index {index} contains {item} of type {type(item)}')
    

#  index 0 contains 0 of type <class 'int'>
#  index 1 contains 2 of type <class 'int'>
#  index 2 contains apple of type <class 'str'>
#  index 3 contains {'key_name': 'first_value'} of type <class 'dict'>
#  index 4 contains {0, 1, 2} of type <class 'set'>
#  index 5 contains ('zero', 'one') of type <class 'tuple'>   

# list of dictionaries, enumerate to get index
list_dict = [{"first": "one", "second": "two", "third": "three"}]
for item in list_dict:
    for index, (k,v) in enumerate(item.items()):
        print(f' at index {index:<5} key is \t {k:<15} value is \t {v:<10}')

#  at index 0     key is   first           value is        one       
#  at index 1     key is   second          value is        two       
#  at index 2     key is   third           value is        three