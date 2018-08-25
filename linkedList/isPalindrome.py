"""
回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/45/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思路：做一个逆转链表出来
        不够，因为空间
        https://www.cnblogs.com/HorribleMe/p/4878833.html
        一半，然后逆转比较
        """
        plen = head
        length = 0
        while plen != None:
            length += 1
            plen = plen.next
        
        pre = None
        r = head
        for i in range(length//2):
            t = r.next
            r.next = pre
            pre = r
            r = t
        
        if length%2 == 1:
            r = r.next
        
        for i in range(length//2):
            if pre.val != r.val:
                return False
            pre = pre.next
            r = r.next
        return True

        
