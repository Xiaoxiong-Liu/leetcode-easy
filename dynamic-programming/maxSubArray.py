"""
这篇博客讲得很好。
https://blog.csdn.net/miaoqiucheng/article/details/78181670

最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumNow = 0
        maxSum = 0
        for num in nums:
            sumNow += num
            if sumNow > maxSum:
                maxSum = sumNow
            if sumNow < 0:
                sumNow = 0
        if maxSum == 0:                 #全部都是负数的情况，只要挑一个最大的就好
            maxSum = max(nums)
        return maxSum
