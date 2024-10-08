#https://leetcode.com/problems/cherry-pickup/description
#741. Cherry Pickup
#Difficulty: Hard
#Takeaways: This problem is a good example of how to use dynamic programming

#Tabulation
class Solution:
    def cherryPickup(self, grid):
        N = len(grid)
        maxDiag = 2 * N - 2
        dp = [[-1] * N for _ in range(N)]
        dp[0][0] = grid[0][0]  # Pick (0, 0), diag = 0

        # Diagonal indicates the number of steps to get to that point
        for diag in range(1, maxDiag + 1):
            # Each diagonal has its range of valid row number
            rowMax = min(diag, N - 1)
            rowMin = max(0, diag - N + 1)
            # i, j means the ending row numbers of two routes after "diag" steps
            # Iterate backwards since we need left/top values to update dp[i][j]
            for i in range(rowMax, rowMin - 1, -1):
                # By symmetry, we can make i >= j
                for j in range(i, rowMin - 1, -1):
                    # Set to -1 for unreachable points
                    if grid[i][diag - i] == -1 or grid[j][diag - j] == -1:
                        dp[i][j] = -1
                        continue

                    # Maximum values from four possible previous directions
                    prev = dp[i][j]
                    if i > 0:
                        prev = max(prev, dp[i - 1][j])
                    if j > 0:
                        prev = max(prev, dp[i][j - 1])
                    if i > 0 and j > 0:
                        prev = max(prev, dp[i - 1][j - 1])
                    
                    # None of the four directions is valid
                    if prev == -1:
                        dp[i][j] = -1
                        continue

                    # If two routes end at the same point, only calculate once
                    dp[i][j] = prev + grid[i][diag - i] + (grid[j][diag - j] if i != j else 0)

        return max(dp[N - 1][N - 1], 0)


#Memoization
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(r1, c1, c2):

            r2 = r1 + c1 - c2        # calculate r2 := r1 + c1 - c2

            # base; infeasible
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            # person 1 reached the bottom right, return its cell value
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # person 2 reached the bottom right, return its cell value
            if r2 == n - 1 and c2 == n - 1:
                return grid[r2][c2]

            # seen before
            if (r1, c1, c2) in memo:
                return memo[(r1, c1, c2)]

            # otherwise compute memo[(r1, c1, c2)]

            # case 1; find answer for current state (r1, c1, r2, c2)]
            # make sure it cells get counted once
            curr_move = grid[r1][c1] + grid[r2][c2] if r1 != r2 and c1 != c2 else grid[r1][c1]

            # case 2; find answer for next state
            down_down = dfs(r1 + 1, c1, c2)
            down_right = dfs(r1 + 1, c1, c2 + 1)
            right_down = dfs(r1, c1 + 1, c2)
            right_right = dfs(r1, c1 + 1, c2 + 1)
            next_move = max(down_down, down_right, right_down, right_right)

            # aggregate curr_move and next_move answers
            memo[(r1, c1, c2)] = curr_move + next_move

            return memo[(r1, c1, c2)]

        n = len(grid)

        # memo[(r1, c1, c2)] := maximum number of cherries can be picked
        # starting at (r1, c1) for person1 and (r2, c2) for person2 s.t r2 := r1 + c1 - c2
        memo = dict()

        # both persons starts at (0, 0)
        res = dfs(0, 0, 0)

        return res if res != float('-inf') else 0
