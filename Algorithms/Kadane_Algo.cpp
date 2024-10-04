//https://leetcode.com/problems/maximum-subarray

// KAUNIK
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int n = nums.size();
        int res = nums[0];
        int global = nums[0];
        for(int i=1;i<n;i++){
            res = max(res+nums[i],nums[i]);
            global = max(global,res);

        }

        return global;
        
    }
};