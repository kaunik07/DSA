// https://leetcode.com/problems/maximum-sum-circular-subarray/description
// 918. Maximum Sum Circular Subarray

// KAUNIK
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
        int n = nums.size();

        int res_max = nums[0];
        int curr_max = 0;
        int curr_min = 0;
        int res_min = nums[0];
        int sum = 0;

        for(int i=0;i<n;i++){

            curr_max = max(curr_max+nums[i],nums[i]);
            curr_min = min(curr_min+nums[i],nums[i]);

            res_max = max(res_max,curr_max);
            res_min = min(res_min,curr_min);

            sum += nums[i];

        }

        if(sum==res_min){
            return res_max;
        }

        return max(sum-res_min,res_max);

    }
};