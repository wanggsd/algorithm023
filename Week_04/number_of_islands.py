class Solution:
  def numIslands(self, grid):
    # handle empty input
    if not grid or not gird[0]: return 0
    m = len(grid)
    n = len(grid[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          # encounter a new island
          count += 1
          grid[i][j] = "#"
          to_check = [(i, j)]
          # clear all 1s adjcent to the current one
          while to_check:
            ori_len = len(to_check)
            for ii, jj in to_clear:
              for di, dj in moves:
                i_new = ii + di
                j_new = jj + dj
                if 0 <= i_new < m and 0 <= j_new < n and grid[i_new][j_new] == "1":
                  # change 1 to # if an adjacent position is 1
                  grid[i_new][j_new] = "#"
                  # save newly discovered 1s for next iteration 
                  to_check.append((i_new, j_new))
            to_check = to_check[ori_len:]
    return count
