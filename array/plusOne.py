"""
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        难点应该就在9的进位上
        先转化成整数（不考虑溢出先）
        """
# class Solution:
#     def plusOne(self, digits):
#         digits[-1] += 1
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] == 10:
#                 digits[i] = 0
#                 if i - 1 < 0:
#                     digits = [1] + digits
#                 else:
#                     digits[i - 1] += 1
#             else:
#                 break
#         return digits
# s = Solution()
# print(s.plusOne([9,9,9]))


#         第一次 2018.08.03
#         length = len(digits)
#         num = 0
#         is99 = True
#         for i in range(length):
#             num = num + digits[length-i-1]*10**i
#             if digits[length-i-1] != 9:
#                 is99 = False
#         num += 1
        
#         if is99 :
#             length += 1         # 全部9要进位
        
#         result = [0]*length
#         for i in range(length):
#             result[length-i-1] = (num % 10)
#             num = num//10
#         return result    


#       第二次 2018.08.04
#         length = len(digits)
#         for i in range(length-1,-1,-1):
#             if digits[i] == 9:
#                 digits[i] = 0
#                 if i == 0:
#                     digits = [1]+digits
#             else:
#                 digits[i] = digits[i]+1
#                 break
#         return digits
        
#         第三次 2018.08.13 注意循环条件 -1 -1
#         for i in range(len(digits) - 1, -1,-1):
#             x = digits[i]+1
#             if x < 10:
#                 digits[i] = x
#                 break
#             if x == 10:
#                 digits[i] = 0
#                 if i == 0:
#                     digits = [1]+digits
#         return digits

#       2018.08.26 思路基本一致，这一版更直观。    
        digits[len(digits)-1] = digits[len(digits)-1]+1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<10:
                break
            digits[i] = 0
            if i == 0:
                digits = [1]+digits
            else:
                digits[i-1] = digits[i-1]+1
        return digits
        
