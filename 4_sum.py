"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? 

Find all unique quadruplets in the array which gives the sum of target.

Ex 1
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""





##### IMPORT THIS !!!!
from typing import Dict, List, Tuple


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)


nums = [1, 0, -1, 0, -2, 2, -2, 0, 0, 2]
target = 0

sol = Solution()
print(sol.fourSum(nums, target))   # [[-2, -2, 2, 2], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1], [0, 0, 0, 0]]

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums, target))   # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]



from typing import List
class Solution_2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def k_sum(nums, k, target):
            if not nums or nums[0] * k > target or nums[-1] * k < target:
                return []
            if k == 2:
                return two_sum(nums, target)
            result = set()
            for index, num in enumerate(nums):
                complement = target - num
                for sub_result_tuple in k_sum(nums[index+1:], k-1, complement):
                    result.add((num, )+sub_result_tuple)
            return list(result)
        def two_sum(nums, target):
            result = set()
            hash_table = {}
            for index, num in enumerate(nums):
                hash_table[num] = index
            for index, num in enumerate(nums):
                complement = target - num
                if complement in hash_table and index < hash_table[complement]:
                    result.add((num, complement))
            return list(result)
        nums.sort()
        return k_sum(nums, 4, target) if nums else [