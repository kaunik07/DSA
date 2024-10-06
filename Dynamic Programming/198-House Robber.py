# https://leetcode.com/problems/house-robber
# 198. House Robber
# Difficulty: Medium




# KAUNIK
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        opt=[0]*n
        if(n==1):
            return nums[0]
        elif(n==2):
            return max(nums[0],nums[1])

        opt[0]=nums[0]
        opt[1]=max(nums[1],nums[0])

        for i in range(2,n):
            opt[i]=max(opt[i-2]+nums[i],opt[i-1])

        return opt[n-1]
    
    def dp(self,nums,i):
        if(i<0):
            return 0

        return max(self.dp(nums,i-2)+nums[i],self.dp(nums,i-1))
