###################
# list   .sort method only works for lists


print(f' .sort method only works for lists')
my_list = [2, 7, 6, 4, 9, 1 , 0]
print(f' Original list  {my_list}')
# Original list  [2, 7, 6, 4, 9, 1, 0]

my_list.sort()  # changes original list (modifies list IN_PLACE  & returns None)
print(f' AFTER calling .sort {my_list}' )
# AFTER calling .sort [0, 1, 2, 4, 6, 7, 9]

my_list.sort(reverse = True)  # changes original list (modifies list IN_PLACE  & returns None)
print(f' AFTER calling .sort  with reverse True {my_list}' )
# AFTER calling .sort  with reverse True [9, 7, 6, 4, 2, 1, 0]

###################
# sorted() function accepts ANY ITERABLE and returns sorted list
print(f' sorted handles any iterable and returns sorted list')
my_list  =  [2, 7, 6, 4, 9, 1 , 0]

sorted_my_list = sorted(my_list)
print(f' Original list  {my_list}')
print(f' sorted_my_list {sorted_my_list} \n')


######################   string items
str = '1 100 10 1000'
split_str = str.split()
print(f' split_str {split_str}')
#  split_str ['1', '100', '10', '1000']
sorted_str = sorted(split_str)
print(f' sorted_str  {sorted_str}')
#  sorted_str  ['1', '10', '100', '1000']

 




###############     dict sorting  by KEYS 
my_dict = {1 : "B", 2: 'E', 0 : 'G'}
sorted_dict_k = sorted(my_dict, reverse = True)
sorted_dict_k2 = sorted(my_dict.keys(), reverse = True)

print(f' *** return list of sorted dict keys in reverse, .keys() is optional')
print(f' my_dict  {my_dict}')
print(f' >> keys   sorted_dict_k {sorted_dict_k} ')
print(f' >> keys  sorted_dict_k2 {sorted_dict_k2} \n\n')

#  my_dict  {1: 'B', 2: 'E', 0: 'G'}
#  sorted_dict [2, 1, 0]

print(f' *** return list of sorted dict values ')
sorted_dict_values = sorted(my_dict.values())
print(f' my_dict  {my_dict}')
print(f' sorted_dict_values {sorted_dict_values} \n\n')
#  my_dict  {1: 'B', 2: 'E', 0: 'G'}
#  sorted_dict_values ['B', 'E', 'G']



sorted_dict_items = sorted(my_dict.items())
print(f' my_dict  {my_dict}')
print(f' sorted_dict_items {sorted_dict_items} \n\n')
#  my_dict  {1: 'B', 2: 'E', 0: 'G'}
#  sorted_dict_items [(0, 'G'), (1, 'B'), (2, 'E')]

# SORTING DICT using lambda  >>  SORT by KEY
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
print(f' my_dict  {my_dict}')
print(f' sorted_dict {sorted_dict} \n\n')
#  my_dict  {1: 'B', 2: 'E', 0: 'G'}
#  sorted_dict {0: 'G', 1: 'B', 2: 'E'} 

# SORTING DICT using lambda  >>  SORT by VALUE
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(f' my_dict  {my_dict}')
print(f' sorted_dict {sorted_dict} \n\n')
#  my_dict  {1: 'B', 2: 'E', 0: 'G'}
#  sorted_dict {1: 'B', 2: 'E', 0: 'G'} 


##########################################  sets
my_set = set('1572')
print(f' my_set {my_set}')

sorted_set = sorted(my_set)
print(f' sorted_set {sorted_set} ')

fl_list = [ '0.123', '4.239', '2.2093', '-.092']
my_f_set = set(fl_list)
print(f' my_f_set {my_f_set }')
sorted_f_set = sorted(my_f_set)
print(f' sorted_f_set { sorted_f_set}')


#########################################   list of tuples
my_list_tup = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('jackie', 'C', 10)
]
 # sort by tuple location in element          >>> sorted by name
sorted_my_list_tup = sorted(my_list_tup,  key = lambda  tup : tup[0])
print(f' sorted_my_list_tup  {sorted_my_list_tup} ')
# sorted_my_list_tup  [('dave', 'B', 10), ('jackie', 'C', 10), ('jane', 'B', 12), ('john', 'A', 15)]


 # sort by tuple location in element          >>> sorted by letter
sorted_my_list_tup = sorted(my_list_tup,  key = lambda  tup : tup[1])
print(f' sorted_my_list_tup  {sorted_my_list_tup} ')
#  sorted_my_list_tup  [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ('jackie', 'C', 10)] 

 # sort by tuple location in element          >>> sorted by letter then number
sorted_my_list_tup = sorted(my_list_tup,  key = lambda  tup : (tup[1], tup[2]) )
print(f' sorted_my_list_tup  {sorted_my_list_tup} \n')


####################   itemgetter
from operator import itemgetter   
# Return a callable object that fetches item from its operand using the operand’s __getitem__() method. 
# If multiple items are specified, returns a tuple of lookup values


# sort by 2nd tuple         sorts by letter
sorted_my_list_tup = sorted(my_list_tup, key = itemgetter(1))
print(f'>> sorted_my_list_tup    {sorted_my_list_tup}')
# >> sorted_my_list_tup    [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10), ('jackie', 'C', 10)]

# sort by 2nd then 3rd tuple
sorted_my_list_tup = sorted(my_list_tup, key = itemgetter(1,2))
print(f' >> sorted_my_list_tup   {sorted_my_list_tup} ')
# sorted_my_list_tup   [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12), ('jackie', 'C', 10)]

#######################################    obj with named attributes
class Student:    
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
    Student('todd', 'A', 14),
    Student('jackie', 'C', 10),
]

# sort objects by age property
sorted_obj = sorted(student_objects, key = lambda obj : obj.age)
print(f' sorted_obj  {sorted_obj}')
# sorted_obj [('dave', 'B', 10), ('jackie', 'C', 10), ('jane', 'B', 12), ('todd', 'A', 14), ('john', 'A', 15)]

# sort objects by grade, then age   
sorted_obj = sorted(student_objects, key = lambda obj : (obj.grade, obj.age) )
print(f' sorted_obj {sorted_obj}')
# sorted_obj [('todd', 'A', 14), ('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12), ('jackie', 'C', 10)]

# sort objects by age, then grade using    >>>>>>>>>>  attrgetter 
from operator import attrgetter

sorted_obj = sorted(student_objects, key = attrgetter('grade', 'age'))
print(f' sorted_obj {sorted_obj}')
# sorted_obj [('todd', 'A', 14), ('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12), ('jackie', 'C', 10)]


# ###########################
# # a lambda in Python is just an anonymous function that has one or more arguments, but only one expression.
# ###########################
# # Syntax:
# # lambda arguments : expression
# # Example
# add_ten = lambda a : a + 10
# print(type(add_ten))
# # Prints <class 'function'>
# print(add_ten(5))
# # Prints 15


# my_list = [1, 8, 5, 2]
# sort_list = lambda x : sorted(x)
# result = sort_list(my_list)

# my_list.sort()
# print(my_list)  # [1, 2, 5, 8]
# print(result)   # [1, 2, 5, 8]


# # build list of dict items
# def daily_activity(order, day, activity):
#          return {'order': order, 'day': day, 'activity': activity}

# mon_activity = daily_activity(0, 'Mon', 'Baseball')
# tue_activity = daily_activity(1, 'Tue', 'Swim')
# wed_activity = daily_activity(2, 'Wed', 'Soccer')
# thu_activity0 = daily_activity(3, 'Thu', 'Basketball')
# thu_activity1 = daily_activity(4, 'Thu', 'Dance')
# thu_activity2 = daily_activity(5, 'Thu', 'Football')
# activities = [mon_activity, tue_activity, wed_activity, thu_activity0, thu_activity1, thu_activity2]

# print(f' activities type:   type(activities)')
# print(activities)  # prints in one wrapable row
# #  [{'order': 0, 'day': 'Mon', 'activity': 'Baseball'}, {'order': 1, 'day': 'Tue', 'activity': 'Swim'}, {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}, {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}, {'order': 4, 'day': 'Thu', 'activity': 'Dance'}, {'order': 5, 'day': 'Thu', 'activity': 'Football'}]


# def print_nice(val):
#      for item in val:
#           print(item)

# print_nice(activities)
# # {'order': 0, 'day': 'Mon', 'activity': 'Baseball'}
# # {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# # {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# # {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# # {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# # {'order': 5, 'day': 'Thu', 'activity': 'Football'}

# # to sort lsit of dict items by a key value  >> 'order'
# sorted_activities = sorted(activities, key= lambda x : x['order'], reverse = True)
# print(f' sort by activities')
# print_nice(sorted_activities)
# # {'order': 5, 'day': 'Thu', 'activity': 'Football'}
# # {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# # {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# # {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# # {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# # {'order': 0, 'day': 'Mon', 'activity': 'Baseball'}

# # to sort lsit of dict items by a key value  >> 'day'
# sorted_activities = sorted(activities, key= lambda x : x['day'], reverse = True)
# print(f' sort by day')
# print_nice(sorted_activities)
# # {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# # {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# # {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# # {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# # {'order': 5, 'day': 'Thu', 'activity': 'Football'}

# #  to sort by more than one Key
# sorted_activities2 = sorted(activities, key = lambda x  : (x['order'] , x['activity']), reverse = True  )
# print(f" sort by \'order\' and then by \'activity\'  ")
# print_nice(sorted_activities2)
# # NOTICE how items 
# # {'order': 5, 'day': 'Thu', 'activity': 'Football'}
# # {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# # {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# # {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# # {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# # {'order': 0, 'day': 'Mon', 'activity': 'Baseball'}

# sorted_activities2 = sorted(activities, key = lambda x  : (x['activity'] , x['day']), reverse = True  )
# print(f" sort by \'activity\' and then by \'day\' >> the day sort does not do much since there are no duplicate activities ")
# print_nice(sorted_activities2)

# print(f' original ')
# print_nice(activities)


