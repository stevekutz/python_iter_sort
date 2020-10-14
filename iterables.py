# An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method.
# Iterable object types includes lists, strings, dictionaries and sets.


# You can loop over an iterable, but you cannot access individual elements directly.
# It’s a container object: it can only return one of its element at the time. 

my_list = [10, 20, 30, 40, 50]
print(f' my_list = {my_list}')   # my_list = [10, 20, 30, 40, 50]

my_set = set('12345')
print(f' my_set   {my_set}')     #  my_set   {'5', '3', '2', '1', '4'}

# merge values from my_set & my_list in my_dict
#### first we create an iterable of tuples using zip
zip_tuples = zip(my_set, my_list)
print(f' zip_tuples  {zip_tuples} ')  # zip_tuples  <zip object at 0x7f81ae725380>

my_tuples = tuple(zip_tuples)
print(f' my_tuples  {my_tuples}')
#  my_tuples  (('5', 10), ('4', 20), ('3', 30), ('1', 40), ('2', 50))

# or do this one step with a dict 
my_dict = dict(zip(my_set, my_list))
print(f' my_dict  {my_dict}')     
#  my_dict  {'1': 10, '4': 20, '3': 30, '2': 40, '5': 50}

###############################################################
# Looping over iterable with for loop

for item in my_list:
    print(f' item in my_list is {item} ')
#  item in my_list is 10 
#  item in my_list is 20 
#  item in my_list is 30 
#  item in my_list is 40 
#  item in my_list is 50


for item in my_set:
    print(f' item in my_set is  {item} ')
#  item in my_set is  5 
#  item in my_set is  4 
#  item in my_set is  3 
#  item in my_set is  2 
#  item in my_set is  1


for item in my_tuples:
    print(f' item in my_tuples is {item} ')        
#  item in my_tuples is ('5', 10) 
#  item in my_tuples is ('4', 20) 
#  item in my_tuples is ('3', 30) 
#  item in my_tuples is ('2', 40) 
#  item in my_tuples is ('1', 50)    

###############################################################
# finding next value using an iterator obj

my_iterator = iter(my_list)
next_val = next(my_iterator)
print(f' my_iterator   {my_iterator}')   # my_iterator   <list_iterator object at 0x7fdeb7ec0250>
print(f' next_val   {next_val}')  # next_val   10
next_val = next(my_iterator)
print(f' next_val   {next_val}')  # next_val   20



################################################################
#  creating an iterable class
##   the __iter__() and __next__() methods must be declared in the class

class Iter_Class:

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < 10:
            self.x += 1
            return self.x
        else:
            raise StopIteration   # exit iteration to next


iter_class = Iter_Class()
my_iter = iter(iter_class)
# print(next(iter_class)) # 1
# print(next(iter_class)) # 2

for i in my_iter:
    print(i)