# https://leetcode.com/problems/longest-increasing-subsequence
# 300. Longest Increasing Subsequence
# Difficulty: Medium


# DP Method
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
# Array sorted method without Binary Search Method 
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [nums[0]]

        for x in nums[1:]:
            if x > s[-1]:
                s.append(x)
            
            else:
                for i in range(len(s)):
                    if(s[i]>=x):
                        s[i]=x
                        break

        return len(s)
    
# Array sorted method with Binary Search Method 
class Solution(object):
    
    def bs(self,nums,target):
        l=0
        r=len(nums)-1

        while(l<=r):
            mid = l + (r-l)/2
            if(nums[mid]>=target):
                r=mid-1
            else:
                l=mid+1
        
        return l
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = [nums[0]]

        for x in nums[1:]:
            if x > s[-1]:
                s.append(x)
            
            else:
                i = self.bs(s,x)
                s[i]=x

        return len(s)