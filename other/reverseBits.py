class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(32):
            m = (m<<1) + n%2
            n =n//2
        return m
