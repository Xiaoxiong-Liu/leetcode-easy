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
        if len(nums)==1:
            return nums[0]
        r = 0
        for i in nums:
            r ^= i
        return r
            
