nums = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
str_val = 'aabbbaaaaaccaaaaaaaaaasdfaaaaaaaaaaaaaaasdfsd'


def find_largest_substring_of_val(num_list, val):

    largest_substring = ''
    current_substring = ''
    count = 0

    for i, item in enumerate(num_list):
        if num_list[i] == val:
            current_substring += str(num_list[i])   
        else:
            if current_substring > largest_substring:
                largest_substring = current_substring
                count = len(largest_substring)
            current_substring = '' 


    print(f' count {count}')
    return largest_substring

num_str = list(str_val)
print(num_str)

print(find_largest_substring_of_val(nums, 1))   # 1111
print(find_largest_substring_of_val(num_str, 'a'))