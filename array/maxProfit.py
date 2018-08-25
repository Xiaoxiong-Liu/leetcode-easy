class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # j = 0
        # count = 0
        # if len(prices) == 0:
        #     return 0
        # for i in range(len(prices)-1):
        #     if(prices[i]<prices[j]):
        #         j = i
        #     if(prices[i]>prices[j] and prices[i+1]<prices[i]):          #卖出
        #         count = count + prices[i]-prices[j]
        #         j = i
        # if prices[j] < prices[-1]:
        #         count = count + prices[-1]-prices[j]
        # return count
    
        # 2018.08.06
        # j = 0
        # length = len(prices)
        # count = 0
        # if length == 0:
        #     return 0
        # for i in range(length - 1):
        #     if prices[j] > prices[i] :
        #         j = i
        #     if prices[j] < prices[i] and prices[i + 1] < prices[i]:
        #         count += (prices[i] - prices[j])
        #         j = i                                                 # 细心，不要忘了这步
        # if prices[length-1] > prices[j]:
        #     count += (prices[length-1] - prices[j])
        # return count
    
        # 2018.08.21
        if len(prices) == 0 or len(prices) == 1:
            return 0
            
        num = 0 
        for i in range(len(prices) - 1): 
            if prices[i+1] > prices[i]:
                num += (prices[i+1] - prices[i])
        return num 
