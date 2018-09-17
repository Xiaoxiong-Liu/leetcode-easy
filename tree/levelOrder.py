"""
二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/50/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        队列，广度优先
        """
        queue = []
        result = []
        
        if root == None:
            return result
        
        queue.append(root)
        while len(queue) != 0:
            length = len(queue)             # 记录的是一层的节点个数
            tmp = []                        # 装载一层的节点值
            for i in range(length):
                # if queue[i].left !=None:                      # 这里犯了一个错，pop了之后i的作用就没有了，顺序会乱
                #     queue.append(queue[i].left)
                # if queue[i].right != None:
                #     queue.append(queue[i].right)
                # tmp.append(queue.pop(0).val)
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                tmp.append(node.val)
                    
            result.append(tmp)
            
        return result
    
    # 2018.08.26 默想一遍，还行。记得考虑root为空。
    # review
    
    # 2018.09.17 review
            
