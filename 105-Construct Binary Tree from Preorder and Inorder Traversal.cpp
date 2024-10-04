//https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description
// 105. Construct Binary Tree from Preorder and Inorder Traversal

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

    unordered_map<int,int> inpos;
    int preindx;

    TreeNode* build(vector<int>& preorder, vector<int>& inorder, int l, int r){
        if(l>r){
            return NULL;
        }

        TreeNode* root = new TreeNode(preorder[preindx]);

        preindx++;

        
        root->left = build(preorder,inorder,l,inpos[root->val]-1);
        root->right = build(preorder,inorder,inpos[root->val]+1,r);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        int n = inorder.size();
        
        for(int i=0;i<n;i++){
            inpos[inorder[i]]=i;
        }
        preindx = 0;
        return build(preorder,inorder,0,n-1);

    }
};