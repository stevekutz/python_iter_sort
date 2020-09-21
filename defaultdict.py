from collections import defaultdict

vals =  [[1, 2],[1, 3],[1, 4],[2,1],[3,4],[4,1]]
trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]

s_vals = [1,2,3,4]
sol = sum(s_vals)     #  sol   10 
print(f' sol   {sol} ')   

d_sum = [ [], []]

################################  setting to list
l_dict = defaultdict(list)
# sum_val = sum(vals)



#######  list of lists
# create defaultdict from list of lists
for item in vals:
    l_dict[item[0]].append(item[1])

    
print(l_dict)  # defaultdict(<class 'list'>, {1: [2, 3, 4], 2: [1], 3: [4], 4: [1]})

#####   ITERATING
# iterate through defaultdict & find sum of values for each key
for k,v in l_dict.items():
    print(f' k {k}    v {v}  sum is {sum(v)}')

#  k 1    v [2, 3, 4]  sum is 9
#  k 2    v [1]  sum is 1
#  k 3    v [4]  sum is 4
#  k 4    v [1]  sum is 1


print(f'\n l_dict.items()   {l_dict.items()}')
print(f' l_dict.keys()   {l_dict.keys()} \n')
# l_dict.items()   dict_items([(1, [2, 3, 4]), (2, [1]), (3, [4]), (4, [1])])
#  l_dict.keys()   dict_keys([1, 2, 3, 4])



##################################  setting to int 
str_val = ' Connecticut'
i_dict = defaultdict(int)

###### ITERATING    through string for k
for k in str_val.upper():
    i_dict[k] += 1

print(f' i_dict.items()   {i_dict.items()} ')
print(f' i_dict.keys()     {i_dict.keys()}\n\n')
#  i_dict.items()   dict_items([(' ', 1), ('C', 3), ('O', 1), ('N', 2), ('E', 1), ('T', 2), ('I', 1), ('U', 1)]) 
#  i_dict.keys()     dict_keys([' ', 'C', 'O', 'N', 'E', 'T', 'I', 'U'])


# str_val = ' Connecticut'
str_val = ' Mississippi'
i_dict2 = defaultdict(int)
###### ITERATING   throught string for v
for v in str_val.upper():
    i_dict2[v] += 1

print(f' i_dict2.items()   {i_dict2.items()}') 
print(f' i_dict2.keys() {i_dict2.keys()} \n\n')
#  i_dict2.items()   dict_items([(' ', 1), ('M', 1), ('I', 4), ('S', 4), ('P', 2)])
#  i_dict2.keys() dict_keys([' ', 'M', 'I', 'S', 'P']) 

##################################  setting to set
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
s_dict = defaultdict(set)

### builds dictionary of sets
for k,v in s:
    s_dict[k].add(v)



print(f' s_dict.items()  {s_dict.items()}')  # s_dict.items()  dict_items([('red', {1, 3}), ('blue', {2, 4})])