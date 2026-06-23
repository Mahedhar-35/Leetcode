class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        mprice=float('inf')
        for price in prices:
            if price<mprice:
                mprice=price
            elif price-mprice>profit:
                profit=price-mprice
        return profit        
                    