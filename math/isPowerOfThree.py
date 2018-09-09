"""
3的幂
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n>=3:
            n = n / 3
        if n!=1:
            return False
        else:
            return True
        
# 迭代解
#         if n==1:
#             return True
#         if n<3:
#             return False
#         if n%3!=0:
#             return False
#         return self.isPowerOfThree(n/3)

# 不循环也不迭代解法
#         return n>0  and 3**19%n == 0
