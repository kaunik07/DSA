#https://leetcode.com/problems/network-delay-time
#743. Network Delay Time
#Difficulty: Medium

# KAUNIK
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        paths = dict()
        cost = {i: float('inf') for i in range(1, n+1)}

        for u, v, w in times:
            if u not in paths:
                paths[u] = []
            paths[u].append((v, w))

        cost[k]=0

        heap = []
        heapq.heappush(heap, (0, k))

        while(len(heap)):
            currtime, node = heapq.heappop(heap)
            
            if currtime > cost[node]:
                continue

            if node in paths:
                for neighbor, time in paths[node]:
                    new_time = currtime + time
                    if new_time < cost[neighbor]:
                        cost[neighbor] = new_time
                        heapq.heappush(heap, (new_time, neighbor))
        

        max_time = max(cost.values())

        return max_time if max_time < float('inf') else -1


            




