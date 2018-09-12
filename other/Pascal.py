"""
帕斯卡三角形
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/26/others/67/

"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(1,numRows):
            t = [0]*(i+1)
            
            for j in range(1,i):
                t[j] = result[i-1][j-1]+result[i-1][j]
            t[0] = 1
            t[-1] = 1
            result.append(t)
        return result
