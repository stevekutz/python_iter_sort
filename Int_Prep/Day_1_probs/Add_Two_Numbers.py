"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Ex 1 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

U - The numbers are in reverse order
  - The only way to represent 0 is (0)  OR  (0 -> 0 -> 0)  to give  0 
  - Numbers will NOT be listed as  (2 -> 4 -> 0)  to give 42
  - DO NOT assume that each linked list is same length  !!! 
  - Anything that adds to 10 is represented as a 0

P - Idea #1 Iterate through each linked list, store into dict to keep track of digits placement
  - You can reverse the dict via comprehension using itemgetter or lambda function
  - knowing length ahead of time would be nice, but since we are iterating through already, may be 
  - overkill
  
    Idea #2 Create function to iterate through each linked list and save string, 
            read string chars in reverse
            convert to int, 
            store numbers

            Add numbers:
            add paying attention to values that add to 10, 
            after building each build each num value,
            return sum

"""