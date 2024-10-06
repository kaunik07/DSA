//https://leetcode.com/problems/sum-root-to-leaf-numbers/description
//129. Sum Root to Leaf Numbers

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
// KAUNIK
class Solution {
public:

    int find(TreeNode* root, int num){
        
        num = num*10 + root->val;

        if(root->left==NULL && root->right==NULL)
            return num;

        

        int left=0,right=0;
        if(root->left)
            left = find(root->left,num);
        if(root->right)
            right = find(root->right,num);

        return left+right;
    }

    int sumNumbers(TreeNode* root) {
        return find(root,0);
    }
};