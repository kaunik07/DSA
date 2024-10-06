#https://leetcode.com/problems/maximal-square
#221. Maximal Square
#Difficulty: Medium

# KAUNIK
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m,n=len(matrix),len(matrix[0])

        dp = [[0]*(n) for _ in range(m)]

        res = 0

        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=='1'):
                    if(i==0 or j==0):
                        dp[i][j]=1
                    else:
                        dp[i][j] = min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))+1
                    res = max(res,dp[i][j])
        
        print(dp)
        return res*res
        