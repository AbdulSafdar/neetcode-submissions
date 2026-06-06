class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0
        R = 0
        max = 0
        max_calc = 0 

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
                min = prices[R]
                
            calc = prices[R] - prices[L]

            if calc > max:
                max = calc

        return(max)
        