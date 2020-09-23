"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# #####################################################   INCLUDE THIS !!!!
# from typing import ListNode

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

class Solution(object):
    def __init__(self):
        self.head = None
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = None

        # l1 = l1.head
        # l2 = l2.head

        # check if l1 empty
        if l1 == None:
            return l2
        # check if l2 empty
        if l2 == None:
            return l1              
        

        if l1.val <= l2.val:  
            current = l1

            current.next = self.mergeTwoLists(l1.next, l2)

        elif l1.val > l2.val:
            current = l2

            current.next = self.mergeTwoLists(l1, l2.next)    

        return current


l1 = Linked_List()
l1.insert_at_head(4)
l1.insert_at_head(2)
l1.insert_at_head(1)
l1.print()     # 1 --> 2 --> 4 --> 

l2 = Linked_List()
l2.insert_at_head(4)
l2.insert_at_head(3)
l2.insert_at_head(1)
l2.print()    #  1 --> 3 --> 4 -->

sol = Linked_List()

s = Solution()

s.mergeTwoLists(l1.head, l2.head)
# print(s.mergeTwoLists(l1.head, l2.head))
# s.mergeTwoLists(l1, l2)

