"""
计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/61/

"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <2:
            return 0
        
        yes = [1] * (n )
        yes[0] = 0
        yes[1] = 0

        for i in range(1, n ):
            if yes[i] == 0:            #这样很多不进入下一次循环
                continue

            p = i
            while p + i < n:
                p = p + i
                yes[p] = 0
        return sum(yes)
            
