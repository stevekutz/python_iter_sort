import random

list_n = []


############# generate list of random nums
### for loop
list_n = []
for i in range(0,6):
    list_n.append(random.randint(0, 10)) 
print(f' list_n {list_n}')   # list_n [4, 5, 6, 5, 9, 4]

### list comprehension
list_n2 = list( random.randint(0,10) for val in range(0,6))
print(f' list_n2 {list_n2}  ')  # list_n2 [6, 4, 9, 3, 1, 2] 

list_n3 = [( random.randint(0,10) for val in range(0,6))]
print(f' list_n3 {list_n3}  ')  # NOPE, creates a generator obj

# list comprehension NO REPEATS


###############  find even nums
my_list = [10, 0, 4, 9, 4, 7]
even_nums = []
### for loop
for i in my_list:
    if i % 2 == 0:
        even_nums.append(i)
print(f' even_nums {even_nums}')     

### list comprehension
even_list = list(val for val in my_list if val % 2 == 0)
print(f' even_list {even_list}')


# print identity matrix
list_m = [ [ 1 if item_idx == row_idx else 0 for item_idx in range(0, 3) ] for row_idx in range(0, 3) ]
for i in list_m:
    print(i)

# [1, 0, 0]
# [0, 1, 0]
# [0, 0, 1]

# given mixed list, find squares of numerical values
mixed_list = ['p', 1, '4', 9, 'a', 0, 4, 3.2] 
squared_vals = [x*x for x in mixed_list if type(x) != str]
# squared_vals = [x**2 for x in mixed_list if type(x)== 'int']
print(f' squared_vals  {squared_vals} ')
#  squared_vals  [1, 81, 0, 16, 10.240000000000002]