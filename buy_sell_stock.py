class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices) 
        if n!=0:
            lowest=prices[0]
            for i in range(1,n):
                if lowest> prices[i]:
                    lowest=prices[i]
                elif prices[i]-lowest>profit:
                    profit=prices[i]-lowest
        return profit                 