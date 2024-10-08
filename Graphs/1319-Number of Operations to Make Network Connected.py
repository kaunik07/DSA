#https://leetcode.com/problems/number-of-operations-to-make-network-connected
#1319. Number of Operations to Make Network Connected
#Difficulty: Medium
#Takeaways: Union Find, Connected Components, Graphs

# KAUNIK
class UnionFind :
    parent=[]
    size=0

    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n

    def find(self,a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]

    
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if(pa!=pb):
            if( self.size[pa] > self.size[pb]):
                self.parent[pb] = pa
                self.size[pa] += self.size[pb]

            else:
                self.parent[pa] = pb
                self.size[pb] += self.size[pa]

    def connected(self,a,b):
        return self.find(a)==self.find(b)



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if(len(connections)<n-1):
            return -1


        uf = UnionFind(n)
        extras=0
        needed=0

        for a, b in connections:
            if uf.connected(a, b):
                extras += 1 
            else:
                uf.union(a, b)
                needed += 1
                

        print(extras)
        print(needed)

        return n - needed-1

        