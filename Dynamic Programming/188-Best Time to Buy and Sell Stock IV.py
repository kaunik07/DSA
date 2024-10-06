#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
#188. Best Time to Buy and Sell Stock IV
#Difficulty: Hard


#Same concept like 2 transactions, but we need to consider k transactions

# KAUNIK
class Solution:
    def maxProfit(self, t: int, prices: List[int]) -> int:
        n = len(prices)

        if(n==1):
            return 0
        
        if(n==2):
            return 0 if prices[0]>prices[1] else prices[1]-prices[0]

        buy = [[0] * n for _ in range(t)]
        sell = [[0] * n for _ in range(t)]

        for j in range(0, t):
            buy[j][0] = -prices[0]
            sell[j][0] = 0
        

        for k in range(t):
            for i in range(1,n):
                if(k==0):
                    buy[k][i]=max(buy[k][i-1],-prices[i])
                    sell[k][i]=max(sell[k][i-1],buy[k][i-1]+prices[i])
                else:
                    buy[k][i]=max(buy[k][i-1],sell[k-1][i] - prices[i])
                    sell[k][i]=max(sell[k][i-1],buy[k][i-1]+prices[i])


        return sell[t-1][n-1]