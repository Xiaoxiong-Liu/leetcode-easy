"""
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #查到非0的个数
#         count = 0
#         for num in nums:
#             if num != 0:
#                 count += 1
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j += 1
#         for x in range(count,len(nums)):
#             nums[x] = 0

#       改用更优雅的方法，只需要遍历一次
        j=0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0 
                j += 1
        return nums
    
# 2018.09.26 i和j是否相等这个判断很优雅。

            
        
