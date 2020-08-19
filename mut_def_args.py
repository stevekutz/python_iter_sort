# https://docs.python-guide.org/writing/gotchas/

def list_append(item, my_list = []):
    my_list.append(item)
    return my_list


list_1 = list_append(10)    
print(f' list_1  {list_1} ')   # list_1  [10]

list_2 = list_append(200)
print(f' list_2  {list_2} ')   # list_2  [10, 200]


# Python’s default arguments are evaluated once when the function is defined, not each time the function is called



def list_append_fix(item, my_list = None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

list_1 = list_append_fix(10)
print(f' FIXED list_1 {list_1}')  # FIXED list_1 [10]

list_2 = list_append_fix(200)
print(f' FIXED list_2  {list_2}')  # FIXED list_2  [200]
