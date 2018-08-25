"""
颠倒整数
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        
        rev = rev*10 + x % 10
        ################################
        
        result = 0
        if x >= 0 : 
            result =  int(str(x)[::-1])
        else:
            x = -x
            result =  0 - int(str(x)[::-1])
        
        if result > 2**31 - 1 or result < 0 
        :
            return 0
        return result
        
        """
        
#         isNeg = False
#         if x < 0:
#             isNeg = True
#             x = -x
#         num = int(str(x)[::-1])

#         if num>2**31-1 or isNeg and -num < -2**31:
#             return 0
#         if isNeg:
#             return -num
#         return num
    # 2018.08.09
    def reverse(self,x):
        isNeg = False
        if x<0:
            x = -x
            isNeg = True
            
        result = 0
        while x !=0:
            result = 10*result + x%10
            x = x//10
        if result> (2**31-1):
            return 0
        elif isNeg:
            return -result
        else:
            return result
