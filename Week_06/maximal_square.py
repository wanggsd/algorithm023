class Solution:
  def maximalSquare(self, matrix):
    m, n = len(matrix), len(matrix[0])
    # dp[c]: longest side length of square whose right bottom corner
    #   is at (r - 1, c - 1) where r the current row #
    dp = [0] * (n + 1)
    max_len = 0
    prev = 0
    for r in range(1, m + 1):
      for c in range(1, n + 1):
        if matrix[r - 1][c - 1] == "1":
          prev_new = dp[c]
          # dp[c] = min(dp[c] of last row, dp[c-1], dp[c-1] of last row) + 1
          # where dp[c - 1] of last row is recorded in prev
          dp[c] = min(dp[c], dp[c - 1], prev) + 1
          max_len = max(max_len , dp[c])
          prev = prev_new
        else:
          # no square exists
          dp[c] = 0
    return max_len ** 2

if __name__ == "__main__":
  m1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  print(Solution.maximalSquare(None, m1))
  m2 = [["0","1"],["1","0"]]
  print(Solution.maximalSquare(None, m2))
  m3 = [["0"]]
  print(Solution.maximalSquare(None, m3))
