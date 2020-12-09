"""
307. Range Sum Query - Mutable
Medium

Given an integer array nums, find the sum of the elements between indices 
i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index 
i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Constraints:

    The array is only modifiable by the update function.
    You may assume the number of calls to update and sumRange function is distributed evenly.
    0 <= i <= j <= nums.length - 1


"""


class NumArray:
    
    def __init__(self, nums: List[int]):
        

    def update(self, i: int, val: int) -> None:
        

    def sumRange(self, i: int, j: int) -> int:
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


"""
# 2D Immutableclass NumMatrix:    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = []
        for row in self.matrix[row1:row2+1]:
            result.append(sum(row[col1:col2+1]))        
            
            return sum(result)
"""