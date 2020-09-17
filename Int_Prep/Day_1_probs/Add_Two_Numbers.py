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
            return sum AS LINKED LIST
E - Syntax to call other method from within method requires stating instances
  - Returning Linked List required adding self.head variable
  - inserting at head makes reversing easier
R - Could make linked list creation into its own function
  - Not seeing how LeetCode builds Linked List requried building my own Linked List class 
    for debugging
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head  # init to head
        llstr = ''
        while itr:
            llstr += str(itr.val) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_head(self, val):
        # this approach also works
        new_node = ListNode(val) # create new node
        new_node.next = self.head # .next points to orig head & list of value, pointers
        self.head = new_node  # reset head to new node



class Solution:
    # function to read linked list values into a str, reverse str, & conver to int
    def __init__(self):
        self.head = None
    
    def str_num(self, link_list):
        str_num = ''
        num_val = 0

        current = link_list.head

        # check if linked list is empty, return 0
        if current == None:
            return num_val
        
        while current:
            # build string
            str_num += str(current.val)
            
            # increment linked list 
            current = current.next

        # reverse the string & convert to int
        num_val = int(str_num[::-1])
        print(f' num_val is {num_val}')
        return num_val

    def addTwoNumbers(self, l1, l2):
        # get int values from each linked list
        # num1 = Solution.str_num(Solution, l1)
        # num2 = Solution.str_num(Solution, l2)

        num1 = Solution.str_num(self, l1)
        num2 = Solution.str_num(self, l2)
        sol_ll = (ListNode)

        # return sum as Linked List
        print(f' sum is {num1 + num2}')
        sum_str = str(num1 + num2)
        for ch in sum_str:
            sol_ll = ListNode(int(ch))
            sol_ll.next = self.head
            self.head = sol_ll
        
        return sol_ll 





ll_1 = Linked_List()
ll_1.insert_at_head(3)    
ll_1.insert_at_head(4)       
ll_1.insert_at_head(2)      
ll_1.print()  # 2 --> 4 --> 3 -->

ll_2 = Linked_List()
ll_2.insert_at_head(4)
ll_2.insert_at_head(6)
ll_2.insert_at_head(5)
ll_2.print()  # 5 --> 6 --> 4 --> 

sol = Solution()
sol.addTwoNumbers(ll_1, ll_2)
#  num_val is 342
#  num_val is 465
#  sum is 807
print()



ll_3 = Linked_List()
ll_3.insert_at_head(0)
ll_3.insert_at_head(0)
sol.addTwoNumbers(ll_1, ll_3)
#  num_val is 342
#  num_val is 0
#  sum is 342

