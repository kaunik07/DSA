#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#309. Best Time to Buy and Sell Stock with Cooldown
#Difficulty: Medium

# KAUNIK
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if(n==1):
            return 0

        buy=[0]*n
        sell=[0]*n

        buy[0]=-prices[0]
        sell[0]=0

        for i in range(1,n):
            # change here from sell[i-1] to sell[i-2] as we need to consider cooldown period
            buy[i]=max(buy[i-1],sell[i-2]-prices[i])  
            sell[i]=max(sell[i-1],buy[i-1]+prices[i])

        return sell[n-1]   