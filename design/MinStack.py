class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.min=-9999999999999999999999999

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.l.append(x)
        self.min = min(self.l)            # 这里可以和最小值比较

    def pop(self):
        """
        :rtype: void
        """
        x = self.l.pop()
        if len(self.l)!=0:
            self.min = min(self.l)       # for循环也行

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
