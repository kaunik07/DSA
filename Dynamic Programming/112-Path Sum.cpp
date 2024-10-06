//https://leetcode.com/problems/path-sum
//112. Path Sum

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
//  KAUNIK
class Solution {
public:
    
    bool find(TreeNode* root, int targetSum, int currsum){
        currsum+=root->val;
        if(root->left==NULL && root->right==NULL){
            if(currsum==targetSum){
                return true;
            }
        }
        bool left=false,right=false;
        if(root->left)
            left = find(root->left,targetSum,currsum);
        if(root->right)
            right = find(root->right,targetSum,currsum);

        return left||right;

    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root==NULL)
            return false;
        return find(root,targetSum,0);
    }
};