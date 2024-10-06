//https://leetcode.com/problems/flatten-binary-tree-to-linked-list
//114. Flatten Binary Tree to Linked List

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

// GENERAL SOLUTION

class Solution {
public:

    TreeNode* preorder(TreeNode* root){
        if (root == NULL) {
            return NULL;
        }

        if(root->left==NULL && root->right==NULL){
            return root;
        }

        TreeNode* left = preorder(root->left);
        TreeNode* right = preorder(root->right);

        if(left!=NULL){
            left->right=root->right;
            root->right=root->left;
            root->left=NULL;
        }

        return right == NULL ? left : right;

    }


    void flatten(TreeNode* root) {
        
        if(root==NULL)
            return;
        TreeNode* head = preorder(root);
        root=head;
    }


// SPACE OPTIMIZED
class Solution {
public:
    void flatten(TreeNode* root) {
        
        if(root==NULL)
            return;
        TreeNode* node = root;
        while(node!=NULL){
            if(node->left!=NULL){
                TreeNode* rightmost = node->left;
                while(rightmost->right!=NULL){
                    rightmost=rightmost->right;
                }

                rightmost->right = node->right;
                node->right = node->left;
                node->left = NULL;
            }

            node = node->right;
        }


    }
};