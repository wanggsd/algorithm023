from collections import defaultdict, deque
import string

def solveSudoku(board):
  # handle empty input
  if not board or not board[0]: return

  # init sets to record used numbers, and boxes to be filled
  rows, cols, triples, visit = [set() for _ in range(9)], [set() for _ in range(9)], defaultdict(set), deque([])
  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        visit.append((r, c))
        continue
      rows[r].add(board[r][c])
      cols[c].add(board[r][c])
      triples[(r//3, c//3)].add(board[r][c])

  def dfs():
    # all boxes assigned
    if not visit: return True

    # retrieve a box to fill
    r, c = visit[0]
    t = (r // 3, c // 3)

    # try each possible number for the current box
    for n in string.digits[1:]:
      if n not in rows[r] and n not in cols[c] and n not in triples[t]:
        # fill one box
        board[r][c] = n
        rows[r].add(n)
        cols[c].add(n)
        triples[t].add(n)
        visit.popleft()
        if dfs():
          # solved
          return True
        else:
          # recover and try next num
          board[r][c] = "."
          rows[r].discard(n)
          cols[c].discard(n)
          triples[t].discard(n)
          visit.appendleft((r, c))
    return False

  dfs()


if __name__ == "__main__":
  board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
  solveSudoku(board)
  for r in board: print(r)
