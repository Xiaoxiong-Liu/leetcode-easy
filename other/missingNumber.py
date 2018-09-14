"""
缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/69/

"""


# 我的解法，用了n的空间，比较暴力
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0]*(len(nums)+1)
        for i in nums:
            a[i] = 1
        for i in range(len(a)):
            if a[i] == 0:
                return i
    # 更加聪明的解法
    def missingNumber2(self,nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
