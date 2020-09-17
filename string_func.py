str1 = '145'

print(f' type(str1)')

num = int(str1)

print(f' num is {num}  {type(num)}')

list = [1, 4, 7]

num_str = ''
for item in list:
    num_str += str(item)

print(f' num_str  {num_str} type {type(num_str)}')

str1 = '342'
split_str = str1.split()
for ch in str1:
    print(f' ch is {ch}')