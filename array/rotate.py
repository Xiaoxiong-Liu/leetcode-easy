class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) == 0 or len(nums) == 1:
#             return
#         k = k%len(nums)
#         self.reverse(nums, 0, len(nums))
#         self.reverse(nums, 0, k)
#         self.reverse(nums, k , len(nums))

#     def reverse(self, nums, begin, end):
#         leng = end - begin
#         if leng == 0:
#             return
#         for i in range(0, leng // 2):
#             tem = nums[begin + i]
#             nums[begin + i] = nums[end - i - 1]
#             nums[end - i - 1] = tem

#   【2018.08.07】注意边界，左移先对
    def rotate(self, nums,k):
        k = k%len(nums)
        
        self.reverse(nums,0,len(nums))  
        self.reverse(nums,0,k)
        self.reverse(nums,k,len(nums))
        
        
    def reverse(self,nums,begin,end):
    
        length = (end - begin)//2
        for i in range(0,length):
            tmp = nums[begin+i]
            nums[i+begin] = nums[end - i - 1]
            nums[end - i - 1] = tmp
