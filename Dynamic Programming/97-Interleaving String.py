#https://leetcode.com/problems/interleaving-string
#97. Interleaving String
#Difficulty: Medium - Hard

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m = len(s1),len(s2)
        if(n+m != len(s3)):
            return False

        dp = [[False]*(m+1) for _ in range((n+1))]

        # dp[0][0]=True

        for i in range(n+1):
            for j in range(m+1):
                k = i+j-1
                if(i==0 and j==0):
                    dp[i][j]=True
                elif i==0:
                    dp[i][j] = dp[i][j-1] and s2[j-1]==s3[k]
                elif(j==0):
                    dp[i][j] = dp[i-1][j] and s1[i-1]==s3[k]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[k]) or (dp[i][j - 1] and s2[j - 1] == s3[k])


        return dp[n][m]

