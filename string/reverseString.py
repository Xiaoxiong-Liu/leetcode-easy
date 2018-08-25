"""
反转字符串
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/

"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = ""
        for i in range(len(s)-1,-1,-1):
            re = re + s[i]
        return re
