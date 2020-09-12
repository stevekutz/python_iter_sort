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

for i in range(8):
    print(f' bit at pos {i} is {bit_set(bit_p2, i)}')   # bit_p2 =0b01010100

print(f' 0b010 {0b0000010}')