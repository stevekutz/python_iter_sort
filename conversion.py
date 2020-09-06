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
print(f' shift_right {bin(shift_right)}')


print(f' str(bin_a)[0]  {str(bin_a)[0]} {type(str(bin_a)[0])}')
print(f' int(str(bin_a)[0])  {int(str(bin_a)[0])} {type(int(str(bin_a)[0]))}')