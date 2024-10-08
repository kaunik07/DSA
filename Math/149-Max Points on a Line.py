#https://leetcode.com/problems/max-points-on-a-line/description
#149. Max Points on a Line
#Difficulty: Hard
#Takeaways: Math, Geometry

# KAUNIK
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if(n==1):
            return 1
        
        res = 2

        for i in range(n):
            count = defaultdict(int)

            for j in range(n):
                if j!=i :
                    angle = math.atan2(points[j][1]-points[i][1],points[j][0]-points[i][0])
                    count[angle] = count[angle]+1

            res = max(res, max(count.values())+1)

        return res