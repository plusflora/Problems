class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # building out our stuff
        b, s = 0, 1 
        m = 0 #

        while s < len(prices):
            if prices[b] < prices [s]:
                p = prices[s] - prices[b]
                m = max(m, p)
            else:
                b = s
            s += 1
        return m
                

        # so we need to have 4 variables (b)uy, (s)ell, (m)ax profit, (p)rofit
        # we check to see if the (b) is lower than (s) - find the profit there and check if it's larger than (m) with max(m, p) setting (m) to whichever is larger
        # if b isn't lower than s we set b to s, increment s and try again
        # finally we return the max profit