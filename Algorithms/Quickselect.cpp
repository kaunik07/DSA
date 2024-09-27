#include <iostream>
#include <vector>
#include <cstdlib>  
#include <algorithm>

using namespace std;

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        // Adjust k to be the index of the k-th largest element
        return quickSelectWithSpaceOptimization(nums, 0, nums.size() - 1, nums.size() - k);
    }

    // Simple and easy to understand method
    int quickSelect(vector<int>& nums, int k) {

        int pivot = nums[rand() % nums.size()]; // can take the last element as pivot also for simplicity
         
        vector<int> left;
        vector<int> mid;
        vector<int> right;
        
        for (int num: nums) {
            if (num > pivot) {
                left.push_back(num);
            } else if (num < pivot) {
                right.push_back(num);
            } else {
                mid.push_back(num);
            }
        }
        
        if (k <= left.size()) {
            return quickSelect(left, k);
        }
        
        if (left.size() + mid.size() < k) {
            return quickSelect(right, k - left.size() - mid.size());
        }
        
        return pivot;
        
    }



    // This function is space optimized, no need to create 3 vectors
    int quickSelectWithSpaceOptimization(std::vector<int>& nums, int left, int right, int k) {
        if (left == right) {
            return nums[left];  // If the list contains only one element
        }

        // Choose a random pivot index between left and right
        int pivotIndex = left + rand() % (right - left + 1); // or can simply take last value as pivot
        int pivotValue = nums[pivotIndex];

        // Move pivot to the end
        std::swap(nums[pivotIndex], nums[right]);

        // Partitioning
        int storeIndex = left;
        for (int i = left; i < right; ++i) {
            if (nums[i] < pivotValue) {
                std::swap(nums[storeIndex], nums[i]);
                storeIndex++;
            }
        }

        // Move pivot to its final place
        std::swap(nums[storeIndex], nums[right]);

        // Recursion: we can now determine the position of the pivot
        if (k == storeIndex) {
            return nums[storeIndex];
        } else if (k < storeIndex) {
            return quickSelect(nums, left, storeIndex - 1, k);
        } else {
            return quickSelect(nums, storeIndex + 1, right, k);
        }
    }

};

int main() {
    Solution solution;
    std::vector<int> nums = {3, 2, 1, 5, 6, 4};
    int k = 2; // Looking for the 2nd largest element
    std::cout << "The " << k << "th largest element is: " << solution.findKthLargest(nums, k) << std::endl;
    return 0;
}