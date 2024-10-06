#https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
#1665. Minimum Initial Energy to Finish Tasks
#Difficulty: Hard

# KAUNIK
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        if(n==1):
            return tasks[0][1]

        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)

        minEnergy=0
        currEnergy=0


        for x in tasks:
            if(x[1]>currEnergy):
                energy_req=x[1]-currEnergy
                minEnergy=minEnergy+energy_req
                currEnergy=currEnergy+energy_req

            currEnergy=currEnergy-x[0]


        return minEnergy
