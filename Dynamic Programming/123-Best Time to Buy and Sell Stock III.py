#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#123. Best Time to Buy and Sell Stock III
#Difficulty: Hard

# KAUNIK
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if(n==1):
            return 0

        buy = [[0] * n for _ in range(2)]
        sell = [[0] * n for _ in range(2)]

        buy[0][0]=-prices[0]
        sell[0][0]=0
        buy[1][0]=-prices[0]
        sell[1][0]=0
        
        
        # Main logic is like single transaction, but we need to consider 2 transactions, 
        # so next transcaction is dependent on the previous transaction
        
        for k in range(2):
            for i in range(1,n):
                # k=0 for first transaction
                if(k==0):
                    buy[k][i]=max(buy[k][i-1],-prices[i])
                    sell[k][i]=max(sell[k][i-1],buy[k][i-1]+prices[i])
                # k>0 , depending on the value of k, we can buy and sell based on the previous transaction
                else:
                    buy[k][i]=max(buy[k][i-1],sell[k-1][i] - prices[i])
                    sell[k][i]=max(sell[k][i-1],buy[k][i-1]+prices[i])

        return sell[1][n-1]