#https://leetcode.com/problems/maximum-star-sum-of-a-graph/description
#2497. Maximum Star Sum of a Graph
#Difficulty: Hard
#Takeaways: Graphs, Greedy, Prefix Sum

# KAUNIK
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        graph = defaultdict(list)
        n = len(vals)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)
        
        res=float('-inf')

        for i in range(n):
            q = []
            costsum = vals[i]

            for x in graph[i]:
                heappush(q,vals[x])
                if (len(q)>k):
                    heappop(q)
                
            while(q):
                if(q[0]>0):
                    costsum = costsum + q[0]
                heappop(q)

            # print(costsum)
            res = max(res,costsum)
        
        return res

        
        