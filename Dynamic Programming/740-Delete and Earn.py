#https://leetcode.com/problems/delete-and-earn/description
#740. Delete and Earn
#Difficulty: Medium
#Takeaways: Dynamic Programming

# KAUNIK
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = defaultdict(int)

        for x in nums:
            points[x]=points[x]+x
        
        n = len(nums)
        
        maxnum = max(points.values())

        dp = [0]*(maxnum+1)

        dp[0]=0
        dp[1] = points[1]

        for i in range(2,maxnum+1):
            dp[i]=max(dp[i-1],dp[i-2]+points[i])

        # print(dp)

        return dp[maxnum]

