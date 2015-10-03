class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minbuy, maxprofit = min(prices[0], prices[1]), max(0, prices[1]-prices[0])
        for i in range(2, len(prices)):
            if prices[i]-minbuy > maxprofit:
                maxprofit = prices[i]-minbuy
            if prices[i] < minbuy:
                minbuy = prices[i]

        return maxprofit


prices = [102, 105, 103, 106, 107, 100, 105, 110]
print Solution().maxProfit(prices)
