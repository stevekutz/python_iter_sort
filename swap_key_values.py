my_dict = {1: 'one', 2: 'two', 3 : 'three'}

swapped_dict = {value: key for key, value in my_dict.items()}
print(f' swapped_dict  {swapped_dict}')