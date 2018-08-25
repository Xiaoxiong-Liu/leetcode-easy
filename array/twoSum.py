"""
两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        双指针
        """
        nums1 = sorted(nums)
        i = 0
        j = len(nums1)-1
        while(i < j):
            if nums1[i]+nums1[j] > target:
                j -= 1
            elif nums1[i]+nums1[j] < target:
                i += 1
            elif nums1[i]+nums1[j] == target:
                break
        result = []
        for x in range(len(nums)):
            if nums[x] == nums1[i] or nums[x] == nums1[j]:
                result.append(x)
        return result
