# KAUNIK
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        if(n1==0):
            return n2
        if(n2==0):
            return n1

        dp = [[0]*(n2+1) for _ in range(n1+1)]

        # print(len(dp))

        for i in range(1,n1+1):
            dp[i][0]=i
        for j in range(1,n2+1):
            dp[0][j]=j


        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if(word1[i-1]==word2[j-1]):
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

        print(dp)

        return dp[n1][n2]






