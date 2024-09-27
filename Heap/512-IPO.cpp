// https://leetcode.com/problems/ipo/description


class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        
        vector<pair<int,int>> p;

        for(int i=0;i<profits.size();i++){
            p.push_back({capital[i],profits[i]});
        }

        sort(p.begin(),p.end());

        priority_queue<int> q;
        int c=0;
        for(int i=0;i<k;i++){
            while(c<profits.size() && p[c].first<=w){
                q.push(p[c].second);
                c++;
            }
            if(q.empty()){
                break;
            }
            w += q.top();
            q.pop();
        }

        return w;

    }
};

