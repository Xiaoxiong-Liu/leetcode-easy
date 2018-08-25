"""
验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/

"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        re = ""
        for w in s:
            if w.isalnum():
                re += w  
        re = re.lower()
        # for i in range(len(re)//2):
        #     if re[i] != re[len(re)-1-i]:
        #         return False
        # return True
        if re[::-1] == re:
            return True
        return False
            
