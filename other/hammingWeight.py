"""
位1的个数
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 :

输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011
 

示例 2:

输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/64/

一些很厉害的解法：https://www.google.com.hk/search?q=%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0&oq=%E4%BD%8D1%E7%9A%84%E4%B8%AA%E6%95%B0&aqs=chrome..69i57j69i61l3&sourceid=chrome&ie=UTF-8

"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = n
        yu = 0
        count = 0
        while ans > 0:
            if ans % 2 ==1:
                count += 1
            ans = ans//2
        return count
        
# 2018.09.20
# 可以利用 n和n-1想与可以消去最右边的1，循环看能与多少次。
