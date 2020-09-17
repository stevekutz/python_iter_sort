"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Ex 1
Input: [1,2,3,1]
Output: true

Ex2
Input: [1,2,3,4]
Output: false

Ex 3
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true


UPER
U - Boolean True result if any number appears more than once in list,
    Boolean False result if all elements distinct 

P - Idea #1  - Use Set, cannot add mutable elements to set directly, for loop or comprehension
             - length set == length orig list >> elements distinct, list length > set length duplicates are present

    Idea #2  - Use Set, immediately exit adding to set if value already in set  >> return False
               Able to iterate through entire list while adding to set >> return True          
E - Passes initial test runs in VS Code
R - Worst Case runtime is length of nums, set method allows exiting of loop without iterating through entire list
R - Using update to immediately process all of iterables in list requires running through entire list
R - Sorting values and then looking for consecutive nums is another approach but this mutates input, copy should be made  
R - Counter within collections could also be used but uses memory to count all keys, result needed only when count exceeds 1 on any key 
"""

nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,1]


class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_nums = set()

        for item in nums:
            if item in set_nums:
                return True        
            set_nums.add(item)
        return False
        


c = Solution()
print(c.containsDuplicate(nums))        