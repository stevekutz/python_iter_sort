from collections import deque

# create an empty deque
d_1 = deque()

print(f' length deque {len(d_1)}')   # length deque 0
# print(f' length deque {maxlen(d_1)}')   # length deque 0

# append to the right side
d_1.append('a')
d_1.append('b')
d_1.append('c')

print (f' d_1 is {d_1}')   #  d_1 is deque(['a', 'b', 'c'])

d_1.appendleft('0')
d_1.appendleft('-1')
d_1.appendleft('-2')

print (f' d_1 is {d_1}')   #  d_1 is deque(['-2', '-1', '0', 'a', 'b', 'c'])

# list out contents of deque
print(f' print using `list`  {list(d_1)}')    #  print using `list`  ['-2', '-1', '0', 'a', 'b', 'c']

# add multiple items
d_1.extend('defg')
print (f' d_1 is {d_1}')  # d_1 is deque(['-2', '-1', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

d_2 = deque()
d_2.extend('123')
print(f' {d_2}\n')     # deque(['1', '2', '3'])

# d_2.rotate(1)
# print(f' {d_2}')   #  deque(['3', '1', '2'])

# d_2.rotate(1)
# print(f' {d_2}')   #  deque(['2', '3', '1'])

# d_2.rotate(1)      
# print(f' {d_2}')   #  deque(['1', '2', '3'])

# rotate right
for i in range(0, len(d_2)):
    d_2.rotate(1)
    print(f' {i} {list(d_2)}')
#  0 ['3', '1', '2']
#  1 ['2', '3', '1']
#  2 ['1', '2', '3']
