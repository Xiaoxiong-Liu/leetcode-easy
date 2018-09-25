"""
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""



class Solution:
    def intersect(self, nums1, nums2):
        """
        
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#         if len(nums1) == 0 or len(nums2) == 0:
#             return []
#         nums1.sort()
#         nums2.sort()
#         minlen = len(nums1) if len(nums1) < len(nums2) else len(nums2)
#         result = []
#         j = 0
#         i = 0

#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 result.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 i += 1

#         return list(result)
    
    
        # 2018.08.10
#         nums1.sort()
#         nums2.sort()

#         len1 = len(nums1)
#         len2 = len(nums2)
#         i = 0
#         j = 0
#         result = []
#         while i<len1 and j<len2:
#             if nums1[i]==nums2[j]:
#                 result.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i]>nums2[j]:
#                 j += 1
#             else :
#                 i +=1
#         return result



        # 2018.08.25
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = []
        while i<len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return  result
    
    # 2018.09.25 平淡无奇
