#https://leetcode.com/problems/map-sum-pairs/description
#677. Map Sum Pairs
#Difficulty: Medium
#Takeaways: Trie, Prefix Sum

class TrieNode:
    def __init__(self):
        self.child={}
        self.last=False
        self.val=0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.track = {}

    def insert(self, key: str, val: int) -> None:

        curr = self.root
        curr_val = self.track.get(key,0)
        delta = val - curr_val
        self.track[key]=val
        for c in key:
            if c not in curr.child:
                curr.child[c]=TrieNode()
            curr=curr.child[c]
            curr.val+=delta
        curr.last=True



    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return 0
            curr=curr.child[c]
        return curr.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)