class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        
        def max_profit(ind, is_buy, cnt):
            # base case
            if ind == len(prices) or k == cnt:
                return 0

            if dp[is_buy][cnt][ind] != -1:
                return dp[is_buy][cnt][ind]

            profit = 0
            # we can buy the stock when is_buy is true
            if is_buy:
                # buy, skip
                profit = max(prices[ind]*-1 + max_profit(ind+1, 1 - is_buy, cnt), max_profit(ind+1, is_buy, cnt))

            else:
                # selling
                profit = max(prices[ind] + max_profit(ind+1, 1 - is_buy, cnt+1), max_profit(ind+1, is_buy, cnt))

            dp[is_buy][cnt][ind] = profit
            return dp[is_buy][cnt][ind]


        n = len(prices)

        if n == 1:
            # if only one day of stock data
            return 0

        dp = [[[-1]*(n) for _ in range(k)] for _ in range(2)]
        return max_profit(0, 1, 0)
    


""" Tabulation """

