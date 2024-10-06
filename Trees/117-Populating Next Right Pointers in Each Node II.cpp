//https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
//117. Populating Next Right Pointers in Each Node II


class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*>q;
        if(root == NULL) return NULL;
        q.push(root);
        while(!q.empty())
        {
            int s = q.size();
            for(int i=0; i<s; i++){
                Node* curr = q.front();
                q.pop();
                //IMP
                if(i<s-1)
                    curr->next = q.front();
                    
                if(curr->left)
                    q.push(curr->left);
                if(curr->right)
                    q.push(curr->right);
            }
            
        }
        return root;
    }
};