class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        还有一种利用set的实现，又不是你自己实现的
        """
        # if len(nums)==1:
        #     return False
        # nums.sort()                     # 复习时候记得加上归并，08.23没加。。。
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
        
        # 2018.08.08
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
    
