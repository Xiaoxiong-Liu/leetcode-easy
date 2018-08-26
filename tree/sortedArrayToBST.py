"""
将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
 
 https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/51/
 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.BST(nums,0,len(nums))
        
    def BST(self,nums,begin,end):
        leng = end - begin
        
        if leng <= 0:
            return None
        root = TreeNode(nums[begin+leng//2])
        root.left = self.BST(nums,begin,begin+leng//2)
        root.right = self.BST(nums,begin+leng//2+1,end)
        return root
