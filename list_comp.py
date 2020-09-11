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
