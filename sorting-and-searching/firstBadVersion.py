# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        二分法
        """
        return self.bad(1,n)
        
        
    def bad(self,begin,end):
            if begin>end:
            return -1
        if begin == end:
            return begin
            
        b = isBadVersion(begin)
        e = isBadVersion(end)
        mid = (begin+end)//2
        m = isBadVersion(mid)    

        if begin == end - 1 and b==False and e == True:
            return end
        
        
        
        
        
        if m != False:
            return self.bad(begin,mid)
        else:
            return self.bad(mid,end)
