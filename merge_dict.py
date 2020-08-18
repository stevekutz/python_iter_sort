dict_1 = {'a': 'A', 'b': 'B', 'one': 1}
dict_2 = {'two': 2, 'three': 3, 'one': "ONE"}

m_dict = {k:v for dict in (dict_1, dict_2) for k,v in dict.items()}    
print(f' merged dict is {m_dict}')  # merged dict is {'a': 'A', 'b': 'B', 'one': 'ONE', 'two': 2, 'three': 3}