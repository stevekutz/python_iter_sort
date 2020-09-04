###########################
# a lambda in Python is just an anonymous function that has one or more arguments, but only one expression.
###########################
# Syntax:
# lambda arguments : expression
# Example
add_ten = lambda a : a + 10
print(type(add_ten))
# Prints <class 'function'>
print(add_ten(5))
# Prints 15


my_list = [1, 8, 5, 2]
sort_list = lambda x : sorted(x)
result = sort_list(my_list)

my_list.sort()
print(my_list)  # [1, 2, 5, 8]
print(result)   # [1, 2, 5, 8]