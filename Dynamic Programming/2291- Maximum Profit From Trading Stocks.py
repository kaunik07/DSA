#https://leetcode.com/problems/maximum-profit-from-trading-stocks/description/
#2291. Maximum Profit From Trading Stocks
#Difficulty: Medium

class Solution:

    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:

        n = len(present)

        dp = [[0]*(budget+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(0,budget+1):
                profit = future[i-1]-present[i-1]
                if(profit>0):
                    if( present[i-1] <= j):
                        dp[i][j]=max(dp[i-1][j-present[i-1]]+profit, dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                
        return dp[n][budget]
