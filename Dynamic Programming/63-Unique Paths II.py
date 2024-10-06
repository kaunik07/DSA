#https://leetcode.com/problems/unique-paths-ii/
#63. Unique Paths II
#Difficulty: Medium

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if(grid[0][0]):
            return 0
        m,n = len(grid),len(grid[0])


        dp = [[0]*n for _ in range(m)]

        dp[0][0]=1

        for i in range(1,n):
            if(dp[0][i-1]==1):
                if(grid[0][i]==0):
                    dp[0][i]=1
                else:
                    dp[0][i]=0
            else:
                dp[0][i]=0

        for i in range(1,m):
            if(dp[i-1][0]==1 and grid[i][0]==0):
                dp[i][0]=1
            elif(grid[i][0]==1 or dp[i-1][0]==0):
                dp[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if(grid[i][j]==0):
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0

        # print(dp)

        return dp[m-1][n-1]
        