//https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description
// 106. Construct Binary Tree from Inorder and Postorder Traversal

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
    int postindx;

    TreeNode* build(vector<int>& inorder, vector<int>& postorder,unordered_map<int,int> &inpos,int lindx, int rindx){

        if(lindx > rindx){
            return NULL;
        }
        int root_val = postorder[postindx];
        TreeNode* root = new TreeNode(root_val);
        int index = inpos[root->val];
        postindx--;
        root->right = build(inorder,postorder,inpos,index+1,rindx);
        root->left = build(inorder,postorder,inpos,lindx,index-1);
        return root;

    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
        unordered_map<int,int> inpos;
        int n = postorder.size();

        for(int i=0;i<postorder.size();i++){
            inpos[inorder[i]]=i;
        }
        postindx=n-1;
        return build(inorder,postorder,inpos,0,n-1);

    }
};