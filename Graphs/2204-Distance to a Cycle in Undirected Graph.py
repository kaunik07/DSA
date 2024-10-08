#https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/
#2204. Distance to a Cycle in Undirected Graph
#Difficulty: Hard
#Takeaways: Graphs, BFS, Cycle Detection

# KAUNIK
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indeg = [0]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u]+=1
            indeg[v]+=1
        
        out_cycle = set()

        queue = []
        q = deque(queue)

        for i in range(n):
            if(indeg[i]==1):
                q.append(i)
                # out_cycle.add(i)
            
        while(q):
            node = q.popleft()
            out_cycle.add(node)

            for x in graph[node]:
                if x not in out_cycle:
                    indeg[x]-=1
                    if(indeg[x]==1):
                        q.append(x)

        in_cycle=deque([])
        for x in  range(n):
            if x not in out_cycle:
                in_cycle.append(x)

        dist=[n]*n
        step=0
        vis=set(in_cycle)
        while(in_cycle):
            for _ in range(len(in_cycle)):
                node = in_cycle.popleft()
                dist[node]=step
                for x in graph[node]:
                    if x not in vis:
                        in_cycle.append(x)
                        vis.add(x)
            step+=1

        return dist