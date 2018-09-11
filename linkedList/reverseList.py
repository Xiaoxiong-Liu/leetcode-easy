"""
反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
            
        if head.next != None:
            h = self.reverseList(head.next)
            # 这里可以改进
            # ht = h
            # while ht.next != None:
            #     ht = ht.next
            # ht.next = head                          # h的尾巴
            head.next.next = head                     #这个写得就很好 上面获取的ht其实就是head.next    
                        
            head.next = None                        #之前一直忽略的问题！！！！
            return h
        
        
    # 迭代解法 2018.08.27
    def reverseList2(self, head):
        if head == None or head.next == None:
            return head
        p = None
        q = head
        while q!=None:
            t = q.next
            q.next = p
            p = q
            q = t
        return p
    
    # 2018.09.11 重写 迭代解
