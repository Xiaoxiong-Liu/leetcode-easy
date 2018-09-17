"""
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/49/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root == None:
#             return True
#         return self.issym(root.left,root.right)
    
#     def issym(self, left, right):
#         if left == None and right == None:
#             return True
#         if left==None or right == None:
#             return False
#         return left.val == right.val and self.issym(left.left,right.right) and self.issym(left.right, right.left)

#   2018.08.25    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
            
        return self.issym(root.left,root.right)
    
    def issym(self,l,r):
        if l == None and r == None:
            return True
        elif l == None or r == None:
            return False
        if l.val !=r.val:
            return False
        
        return self.issym(l.left,r.right) and self.issym(l.right,r.left)
    
    # 2018.09.16 review
    
    # 2018.09.17 review
    def isSymmetric2(self, root):
        if root == None:
            return True
        return self.isSym2(root.left,root.right)
        
    def isSym2(self, left,right):
        if left ==None and right == None:
            return True
        if left==None or right ==None:
            return False
        return left.val == right.val and self.isSym2(left.left,right.right) and self.isSym2(left.right,right.left)
    
