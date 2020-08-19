def multiply_by():
    return [lambda x: i*x for i in range(5)]


for func in multiply_by():
    print(func(2))    

# 8
# 8
# 8
# 8
# 8    


# Python’s closures are late binding. This means that the values of 
# variables used in closures are looked up at the time the inner function is called

def multiply_by_fixed():
    return [lambda x, i=i  : i * x for i in range(5)]


for func in multiply_by_fixed():
    print(func(2))

# 0
# 2
# 4
# 6
# 8    