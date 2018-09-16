"""
验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/48/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst(root,-9999999999999,99999999999)
        
    def bst(self, root, mi, ma):
        if root == None:
            return True
        if root.val>= ma or root.val<=mi:                   #这个等号很关键
            return False

        l = self.bst(root.left,mi,root.val)                 #认定了左节点值小于根即：root.left.val<root.val,mi只是传递作用
        r = self.bst(root.right,root.val,ma)                #同理
        return l and r 
    
    
    """
            root                        |--------------------------取值范围-----------------------|
            /   \                       |----左树取值范围-----|(左根节点值传下去其实是为了下面的子树)      
        root.l  root.r                                                  |--------右树取值---------|
    
    
    
    
    
    """
    
    # 2018.09.16 review
    def isBST2(self,root,left,right):
        if root == None:                    #这里我开始用的是left和right的判断，情况比较多。
            return True        
        return root.val<right and self.isBST(root.right,root.val,right) and left<root.val and self.isBST(root.left,left,root.val)

