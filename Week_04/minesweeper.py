class Solution:
  def updateBoard(self, board, click):
    # handle empty input
    if not board or not board[0]:
      return []

    # step on mine
    if board[click[0]][click[1]] == "M":
      board[click[0]][click[1]] = "X"
      return board

    moves = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
    m, n = len(board), len(board[0])
    def dfs(i, j, board):
      # only reveal recursively when the adjcent saqure is E
      if board[i][j] != "E":
        return

      # calculate # of mines around i, j
      mines = [board[i + di][j + dj] == "M" for di, dj in moves if 0 <= i + di < m and 0 <= j + dj < n]
      n_mines = sum(mines)

      if n_mines == 0:
        board[i][j] = "B"
      else:
        # stop recursive revealing if not all adjacent sqaures are E
        board[i][j] = str(n_mines)
        return
      # reveal all adjcent square recursively
      for di, dj in moves:
        i_new, j_new = i + di, j + dj
        if 0 <= i_new < m and 0 <= j_new < n:
          dfs(i_new, j_new, board)
    dfs(click[0], click[1], board)
    return board
