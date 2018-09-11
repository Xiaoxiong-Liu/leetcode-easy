"""
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/44/

""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        end = ListNode(-1)                 # 带头节点，等下删除，因为是新的链表，什么都没有就不知道该从哪开始了
        head = end
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                end.next = l1
                end = end.next
                l1 = l1.next
            else:
                end.next = l2
                end = end.next
                l2 = l2.next
                
        if l1 != None:
            end.next = l1
        if l2 != None:
            end.next = l2
        head = head.next

        return head
        
    # 2018.08.27 review
    # 2018.09.11 review
