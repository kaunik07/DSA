#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#122. Best Time to Buy and Sell Stock II
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
            #change here from buy[i-1] to sell[i-1] as we can buy and sell on the same day
            buy[i]=max(buy[i-1],sell[i-1]-prices[i])
            sell[i]=max(sell[i-1],buy[i-1]+prices[i])

        return sell[n-1]