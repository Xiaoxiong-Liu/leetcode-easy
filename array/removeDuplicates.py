class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]>nums[j]:
                j = j+1
                nums[j] = nums[i]
        return j+1
