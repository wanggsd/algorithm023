class Solution:
  def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    for r in range(m):
      for c in range(n):
        if r == 0 and c == 0:
          # sum for path to (0, 0)
          dp[r][c] = grid[r][c]
        elif r == 0:
          # sum for path to (0, c)
          dp[r][c] = dp[r][c - 1] + grid[r][c]
        elif c == 0:
          # sum for path to (r, 0)
          dp[r][c] = dp[r - 1][c] + grid[r][c]
        else:
          # normal state transition
          dp[r][c] = min(dp[r-1][c], dp[r][c - 1]) + grid[r][c]
    return dp[-1][-1]


if __name__ == "__main__":
  print(Solution.minPathSum(None, [[1,3,1],[1,5,1],[4,2,1]]))
  print(Solution.minPathSum(None, [[1,2,3],[4,5,6]]))
