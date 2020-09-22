"""
Given an array nums, write a function to move all 0's to the end 
of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""
nums = [0,1,0,3,12]


for i in nums:
    if i == 0:

        nums.remove(i)
        nums.append(i)
    

print(f' nums  {nums}')        