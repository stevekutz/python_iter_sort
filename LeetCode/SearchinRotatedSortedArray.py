"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you 
beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

"""
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         all_nums = set()
#         all_nums.update(nums)
        
#         if target not in all_nums:
#             return -1
        
#         for i in enumerate()

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [1, 3]
# target = 3


def search_ra(nums, target):
    # all_nums = set()
    # all_nums.update(nums)
    
    # if target not in all_nums:
    #     return -1
    


    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i


    # n_dict = dict( (k,v) for k,v in enumerate(nums))

    # if target not in n_dict.values():
    #     return -1

    # for k,v in n_dict.items():
    #     if n_dict[k] == target:
    #         return k


    if target in nums:
        return nums.index(target)
    else:
        return -1


print(search_ra(nums, target))            