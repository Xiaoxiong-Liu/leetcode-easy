"""
环形链表
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/46/

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        if fast == None or fast.next == None or fast.next.next == None:
            return False
        while fast != None and fast.next != None:
            fast = fast.next
            fast = fast.next
            head = head.next
            if fast == head:
                return True
            
        return False
# review 2018.08.28   if条件注意。
