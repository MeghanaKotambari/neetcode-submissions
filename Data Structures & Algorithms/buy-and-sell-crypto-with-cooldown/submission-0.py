
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = 0
        rest = 0

        for price in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)

        