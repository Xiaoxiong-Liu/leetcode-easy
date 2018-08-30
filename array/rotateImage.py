"""
旋转图像
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/31/
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        """
        # 顺时针方向旋转
        
        
        # 转置再对称翻转
        length = len(matrix[0])
        
        for i in range(0,length):
            for j in range(i,length):
                self.swap(matrix,i,j)
        for i in range(0,length):
            matrix[i].reverse()
        
    def swap(self,matrix,i,j):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = tmp
        
# 2018.08.30 review
