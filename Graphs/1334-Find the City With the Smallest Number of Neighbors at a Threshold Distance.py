#https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
#1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
#Difficulty: Medium
#Takeaways: Graphs, Floyd Warshall, Dijkstra

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = defaultdict(list)

        dp = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=0

        for u,v,dist in edges:
            graph[u].append([dist,v])
            graph[v].append([dist,u])
            dp[u][v]=dist
            dp[v][u]=dist
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if(i==j):
                        continue
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
                    # if(dp[i][k] + dp[k][j] < dp[i][j]):
                    #     dp[i][j] = dp[i][k] + dp[k][j]
        
        # print(dp)
        node = -1
        minReach=float('inf')
        for i in range(n):
            canReach = 0
            for j in range(n):

                if(i==j):
                    continue

                if(dp[i][j]<=distanceThreshold):
                    canReach+=1

            if (canReach<=minReach):
                minReach=canReach
                node=i

        return node