/* 
    Time Complexity
    - Average Case: O(n), where n is the number of elements in the array. This is because, on average, each partition reduces the size of the problem significantly (about half).
    - Worst Case: O(n²), which occurs when the smallest or largest element is consistently chosen as the pivot (like in sorted or reverse-sorted arrays). This can be mitigated by using a random pivot or other strategies.

    How Quickselect Works
        Selection of Pivot:
            - Just like Quicksort, Quickselect begins by selecting a pivot element from the array. This pivot can be chosen randomly or using some heuristic (like the median of medians). The choice of pivot affects performance, but Quickselect is designed to work efficiently on average.
        
        Partitioning:
            The array is then partitioned into three segments relative to the pivot:
            -   Left: Elements less than the pivot.
            -   Right: Elements greater than the pivot.
            -   Middle: Elements equal to the pivot.
            After partitioning, the pivot element will be in its final sorted position.
        
        Recursive Search:
            Depending on the position of the pivot after partitioning:
            -   If the pivot’s position matches the desired k-th index, return the pivot.
            -   If the k-th index is less than the pivot's position, recursively call Quickselect on the left partition.
            -   If the k-th index is greater than the pivot's position, recursively call Quickselect on the right partition, adjusting k accordingly.
*/

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
    // Choose the last element as the pivot
        int pivot = nums[right];
        int partitionIndex = partition(nums, left, right, pivot);

        // If the partition index matches k, we found the kth element
        if (partitionIndex == k) {
            return nums[partitionIndex];
        }
        // If k is less than the partition index, search left side
        else if (k < partitionIndex) {
            return quickSelect(nums, left, partitionIndex - 1, k);
        }
        // If k is greater than the partition index, search right side
        else {
            return quickSelect(nums, partitionIndex + 1, right, k);
        }
    }

    int partition(std::vector<int>& nums, int left, int right, int pivot) {
        int i = left;
        for (int j = left; j < right; j++) {
            if (nums[j] < pivot) {
                std::swap(nums[i], nums[j]);
                i++;
            }
        }
        // Place the pivot in its correct position
        std::swap(nums[i], nums[right]);
        return i; // Return the index of the pivot
    }

};

int main() {
    Solution solution;
    std::vector<int> nums = {3, 2, 1, 5, 6, 4};
    int k = 2; // Looking for the 2nd largest element
    std::cout << "The " << k << "th largest element is: " << solution.findKthLargest(nums, k) << std::endl;
    return 0;
}