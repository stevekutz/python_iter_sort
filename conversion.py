my_str= " my string"
print(f' my_str[2] {my_str[2]} ')
str_split = my_str.split()
print(f' str_split {str_split}')

str_num_10 = '10'
str_num_100 = '100'

# concatenate string
str_combine = str_num_10 + str_num_100
print(f' str_combine {str_combine}')

num_10 = int(str_num_10)
num_100 = int(str_num_100)
sum = num_10 + num_100
print(f' sum  {sum}')

f_num = 2.005
sum = num_10 + f_num
print(f' sum {sum}') #  sum 12.004999999999999

f_10 = float(num_10)

sum = f_10 + f_num
print(f' sum {sum}') #  sum 12.004999999999999

sum = 2.005 + 10.0
print(f' sum {sum}') #  sum 12.004999999999999

print(f' bin(10)  {bin(10)}')  # 0b1010
print(f' hex(10)  {hex(10)}')  # 0xa

bin_a = 0b10001001
shift_right = bin_a >> 1
print(f' orig {bin(bin_a)}  shift_right {bin(shift_right)} \n')
print(f' orig {bin(bin_a)}')

print(f' str(bin_a)[0]  {str(bin_a)[0]} {type(str(bin_a)[0])}')
print(f' int(str(bin_a)[0])  {int(str(bin_a)[0])} {type(int(str(bin_a)[0]))}')

print(f' bin(bin_a)  {bin(bin_a)} {type(str(bin_a))}')


bit_p = 0b10000111
bit_p2 =0b01010100

def bit_set(bin_val, position = None):
    pos = [1, 2, 4, 8, 16, 32, 64, 128]

    if position != None:
        if bin_val & pos[position] != 0:
            return 1
        else:
            return 0    


    else:
        for i in range(8):
            if bin_val & pos[i] != 0:
                print(f' bit {i} is set to 1 ')  
            else:
                print(f' bit {i} is set to 0')          


# for i in range(8):
#     print(f' bit at pos {i} is {bit_set(bit_p, i)}')   # bit_p = 0b10000111
# bit at pos 0 is 1
# bit at pos 1 is 1
# bit at pos 2 is 1
# bit at pos 3 is 0
# bit at pos 4 is 0
# bit at pos 5 is 0
# bit at pos 6 is 0
# bit at pos 7 is 1

# for i in range(8):
#     print(f' bit at pos {i} is {bit_set(bit_p2, i)}')   # bit_p2 =0b01010100

# print(f' 0b010 {0b0000010}')

###################################################
###################   binary ops

x = 0b01010101
y = 0b11111111
print(f' y is {y}  x is {x}  ')   # y is 255  x is 85


############## bitshift LEFT <<      like mult by 2 for each position
y = y << 1
x = x << 1
print(f' y is now {y}   & x is {x}')   # y is now 510   & x is 170

# ANDing by b11111111   keeps y within 255 range of max value of 8-bit bin number
y = 0b11111111
y =  (y << 1) & y
print(f' y is now {y}')  #   y is now 254


############## bitshift right    like div by 2, takes floor of result
x = 0b01010101
y = 0b11111111
print(f' y is {y}  x is {x}  ')   # y is 255  x is 85


y = y >> 1      # would be exactly 127.5
x = x >> 1      # would be exactly 42.5
print(f' y is now {y}   & x is {x}')    #  y is now 127   & x is 42


##############  bitwise AND
x = 0b01100001
y = 0b11111111
z = 0b11001100
print(f' y is {y}  x is {x}  z is {z}')   #  y is 255  x is 97  z is 204

and_result = x & y
print(f' and result {and_result}')   #  and result 97


def find_set_indices(bin_val):
    pos = [1, 2, 4, 8, 16, 32, 64, 128]
    result = []

    for i  in range(8):
        if bin_val & pos[i] != 0:
            result.append(i)

    return result        

print(find_set_indices(x))  # [0, 5, 6]
print(find_set_indices(z))  # [2, 3, 6, 7] 


###############  bitwise OR
x = 0b01100001
y = 0b11111111
z = 0b11001100
print(f' y is {y}  x is {x}  z is {z}')   #  y is 255  x is 97  z is 204


# list_ones = [val for val in find_set_indices(x)].extend(val for val in find_set_indices(z))  # returns None

list_ones = [val for val in find_set_indices(x)]
list_ones.extend(val for val in find_set_indices(z))
set_list = set()
[set_list.add(s) for s in list_ones]

list_ones_sorted = sorted(set_list, reverse = True)
# list_ones_sorted = sorted(list(set_list.add(s) for s in list_ones), reverse = True)     # Nope

print(f' list_ones    {list_ones}')               # list_ones    [0, 5, 6, 2, 3, 6, 7]
print(f' list_ones_sorted \t\t {list_ones_sorted}')    # list_ones_sorted   [7, 6, 6, 5, 3, 2, 0]

or_vals = x | z
find_set_indices(or_vals)
print(f' \t\t bin(or_vals) {bin(or_vals)}   ')
print(f' find_set_indices(or_vals)       {sorted(find_set_indices(or_vals), reverse = True)}  ')
