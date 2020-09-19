"""
Task
Given an integer, n, and  n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of
 hast(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer,
, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple

.

Output Format

Print the result of

.

Sample Input 0

2
1 2


"""

import hashlib

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    tup = ()

    for x in integer_list:
        tup+=(x,)
    print(hash(tup))