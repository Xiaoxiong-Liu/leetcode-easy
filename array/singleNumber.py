“”“
只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
    
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/25/
    
“”“


class Solution:
    def singleNumber(self, nums):
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        
        
        惊为天人的算法
        在这里需要返回的是数字不是位置，所以可以想到这种算法，通过整体计算（交换律结合率的方法）直接得到结果
        更厉害的：https://blog.csdn.net/ns_code/article/details/27649027
        
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r ^= i
        return r
            
# 2018.09.25 精简了一下代码。
