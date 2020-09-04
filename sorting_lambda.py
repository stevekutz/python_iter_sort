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


# build list of dict items
def daily_activity(order, day, activity):
         return {'order': order, 'day': day, 'activity': activity}

mon_activity = daily_activity(0, 'Mon', 'Baseball')
tue_activity = daily_activity(1, 'Tue', 'Swim')
wed_activity = daily_activity(2, 'Wed', 'Soccer')
thu_activity0 = daily_activity(3, 'Thu', 'Basketball')
thu_activity1 = daily_activity(4, 'Thu', 'Dance')
thu_activity2 = daily_activity(5, 'Thu', 'Football')
activities = [mon_activity, tue_activity, wed_activity, thu_activity0, thu_activity1, thu_activity2]

print(f' activities type:   type(activities)')
print(activities)  # prints in one wrapable row
#  [{'order': 0, 'day': 'Mon', 'activity': 'Baseball'}, {'order': 1, 'day': 'Tue', 'activity': 'Swim'}, {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}, {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}, {'order': 4, 'day': 'Thu', 'activity': 'Dance'}, {'order': 5, 'day': 'Thu', 'activity': 'Football'}]


def print_nice(val):
     for item in val:
          print(item)

print_nice(activities)
# {'order': 0, 'day': 'Mon', 'activity': 'Baseball'}
# {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# {'order': 5, 'day': 'Thu', 'activity': 'Football'}

# to sort lsit of dict items by a key value  >> 'order'
sorted_activities = sorted(activities, key= lambda x : x['order'], reverse = True)
print(f' sort by activities')
print_nice(sorted_activities)
# {'order': 5, 'day': 'Thu', 'activity': 'Football'}
# {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# {'order': 0, 'day': 'Mon', 'activity': 'Baseball'}

# to sort lsit of dict items by a key value  >> 'day'
sorted_activities = sorted(activities, key= lambda x : x['day'], reverse = True)
print(f' sort by day')
print_nice(sorted_activities)
# {'order': 2, 'day': 'Wed', 'activity': 'Soccer'}
# {'order': 1, 'day': 'Tue', 'activity': 'Swim'}
# {'order': 3, 'day': 'Thu', 'activity': 'Basketball'}
# {'order': 4, 'day': 'Thu', 'activity': 'Dance'}
# {'order': 5, 'day': 'Thu', 'activity': 'Football'}

