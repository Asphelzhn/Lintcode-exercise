'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

题解：使用哈希表对值和索引做映射，以空间换时间。时间复杂度O（n)
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict={}
        for i in range(len(nums)):
           nums_dict[nums[i]]=i
        for j in range(len(nums)):
            if (target-nums[j]) in nums_dict:
                if (j == nums_dict[target-nums[j]]):
                    continue
                return [j,nums_dict[target-nums[j]]] 

