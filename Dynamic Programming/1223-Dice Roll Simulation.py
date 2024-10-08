#https://leetcode.com/problems/dice-roll-simulation/description
#1223. Dice Roll Simulation
#Difficulty: Hard
#Takeaways: Dynamic Programming


#Tabulation
class Solution:
    
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        cumm = len(rollMax)

        dp = [[0]*(cumm+1) for _ in range(n+1)]

        dp[0][cumm]=1


        for i in range(cumm):
            dp[1][i]=1

        dp[1][cumm]=6

        for roll in range(2,n+1):
            for face in range(cumm):

                for k in range(1,rollMax[face]+1):
                    if(roll - k < 0):
                        break
                    
                    dp[roll][face] += dp[roll-k][cumm] - dp[roll-k][face]

            dp[roll][cumm] = sum(dp[roll])

        
        return dp[n][cumm]%1000000007



# Memoization
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)  # Number of faces on the die (6 for a standard die)

        # Memoization table, initialized to None (uncomputed states)
        memo = [[[None for _ in range(16)] for _ in range(7)] for _ in range(n + 1)]
        
        # Recursive function with memoization
        def dfs(i, lastFace, count):
            # Base case: if no rolls left, return 1 (one valid sequence: the empty sequence)
            if i == 0:
                return 1
            
            # Check if the result is already computed
            if memo[i][lastFace][count] is not None:
                return memo[i][lastFace][count]
            
            # Total number of valid sequences for this state
            total = 0
            
            # Try rolling each face from 1 to 6 (or faces in general)
            for face in range(1, faces + 1):
                if face == lastFace:
                    # If the face is the same as the previous one, only roll if it doesn't exceed rollMax
                    if count < rollMax[face - 1]:
                        total += dfs(i - 1, face, count + 1)
                        total %= MOD
                else:
                    # If it's a different face, reset the count for consecutive rolls to 1
                    total += dfs(i - 1, face, 1)
                    total %= MOD
            
            # Store the result in memo table
            memo[i][lastFace][count] = total
            return total
        
        # Start the recursion with all possible faces, no previous face, and 0 consecutive rolls
        return dfs(n, 0, 0)