class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min1 = prices[0]

        for price in prices:
            if price > min1:
                ans = max(ans, price - min1)

            min1 = min(min1, price)

        return ans