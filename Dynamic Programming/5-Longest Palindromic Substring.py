#https://leetcode.com/problems/longest-palindromic-substring
#5. Longest Palindromic Substring
#Difficulty: Medium

# KAUNIK
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        
        res=""

        def find(i,j,s):
            l=i
            r=j
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l=l-1
                r=r+1

            return s[l+1:r]

        for i in range(n):
            odd = find(i,i,s)
            if(len(odd)>len(res)):
                res=odd

            even = find(i,i+1,s)
            if(len(even)>len(res)):
                res=even

        return res
        