"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints
1 <= len(string <= 200)

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2

Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where

is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])

A range function is used to loop over some length:

range (0, 5)

Here, the range loops over
to . is excluded.

"""
S = 'ABCDCACDFCDCECDCDCAAAAB'
sub = 'CDC'


# def count_substring(string, sub_string):
    
#     def find_indices(substring, string):
#         ch = substring[:1]
    


# if __name__ == '__main__':



def find_indices(string, sub_string):
    sub_ch = sub_string[:1]

    # print(sub_ch)

    indices = []
    index = 0

    for i in range(len(string) - 1):
        print(f' at {i}  ch is string[i]')

    while index < len(string):
        ind = string.find(sub_ch, index)
        if ind == -1:
            return indices
        indices.append(ind)
        index = ind + 1    
    
    return indices

# print(find_indices(S, sub))




S = 'ABCDCACDFCDCECDCDCAAAAB'
sub = 'CDC'


def count_sub(string, sub_string):
    indices = []
    index = 0

    # for i in range(len(string) - 1):
    #     print(f' at {i}  ch is string[i]')

    while index < len(string):
        ind = string.find(sub_string, index)
        if ind == -1:
            break
        indices.append(ind)
        index = ind + 1    
    
    print(f' length of indices {len(indices)} ')
    print(f' indices are are  {indices}')


    return indices

print(count_sub(S, sub))




    
