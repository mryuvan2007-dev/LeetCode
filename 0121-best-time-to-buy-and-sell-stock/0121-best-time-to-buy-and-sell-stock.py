class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice=float('inf')
        maxprofit=0
        for p in prices:
            if p<minprice:
                minprice=p
            currentprofit=p-minprice
            if currentprofit>maxprofit:
                maxprofit=currentprofit
        return maxprofit