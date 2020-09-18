"""
Given an array nums of n integers, are there elements a, b, c 
in nums such that a + b + c = 0? Find all unique triplets in the 
array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Ex 1
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Ex2
Input: nums = []
Output: []

Ex3
Input: nums = [0]
Output: []


"""

##### IMPORT THIS !!!!
from typing import Dict, List, Tuple


nums = [-1,0,1,2,-1,-4]


class Solution:
    # def threeSum(self, nums):
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        result = []
        res = set()
        seen = set()
        three_sum = 0    # target sum value
        for i, val1 in enumerate(nums):   # val1 is currently enumerated
            if val1 in seen:
                continue
            seen.add(val1)
            
            two_sum = three_sum - val1  # value needed  for `two+sum` for three_sum = val1 + two_sum
            val2_set = set() 
            for val3 in nums[i+1:]:  # run search though values after index  of currently enumerated val1
                    # FROM   val3 = two_sum - val2
                    val2 = two_sum - val3   # val2 needed to find two_sum value
                    if val2 in val2_set:
                        res.add(tuple(sorted((val1, val2, val3))))
                        # res.update(sorted((val1, val2, val3)))   #  extra => finds all values in nums that are used in solution
                    val2_set.add(val3)   # add val3 as solution to two_sum using current val1
        
        ########## return as list of tuples
        return list(res)   # [(-1, 0, 1), (-1, -1, 2)]

        # ########## return as set of tuples
        # return res   # {(-1, 0, 1), (-1, -1, 2)}


        # ########## returns list of lists
        # for item in res:
        #     result.append(list(item))
        # return result    # [[-1, 0, 1], [-1, -1, 2]]  

s = Solution()
print(s.threeSum(nums))  # [(-1, 0, 1), (-1, -1, 2)]
