"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first
letters of Lilah's infinite string.

For example, if the string s = `abbcac`and n = 10, the substring we consider is abcacabcac (notice abcac|abcac), the first characters of her infinite string. 
There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length n
in the infinitely repeating string.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

Input Format

The first line contains a single string,
.
The second line contains an integer,

.

Constraints

For of the test cases,

    .

Output Format

Print a single integer denoting the number of letter a's in the first
letters of the infinite string created by repeating

infinitely many times.

Sample Input 0

aba
10

Sample Output 0

7

Explanation 0
The first
letters of the infinite string are abaabaabaa. Because there are a's, we print

on a new line.

Sample Input 1

a
1000000000000

Sample Output 1

1000000000000

Explanation 1
Because all of the first
letters of the infinite string are a, we print on a new line.

"""
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

# find number of 'a' in single s string
    num_a_in_s = 0
    for char in s:
        if char == 'a':
            num_a_in_s += 1
    
    # Find number of time s appears in n         
    complete_rep_of_s = n // len(s)
    
    # find the extra value of 'a' in the remainder
    num_a_in_remainder = 0   # initialize
    
    remainder_length = n % len(s) 

    # remainder_str = s[:remainder_length]

    # just count the 'a' in remainder string
    for ch in s[:remainder_length]:
        if ch == 'a':
            num_a_in_remainder += 1

    # return # of complete rep * num of a in s    +  num a in remainder        
    return complete_rep_of_s * num_a_in_s + num_a_in_remainder


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()    