class Solution:
  def minMutation(self, start, end, bank):
    # edge case
    if end not in bank: return - 1

    # init
    bank = set(bank)
    if start in bank: bank.discard(start)
    if end in bank: bank.discard(end)
    front, back = {start}, {end}
    res = 0

    # BFS
    while front:
      # all possible mutations from front
      front = {g[:i] + c + g[i + 1:] for g in front for i in range(len(g)) for c in "ACGT"}
      res += 1

      # searches from 2 directions meet
      if front & back: return res

      # only keep mutations existing in bank
      front &= bank

      # remove used mutations from bank
      bank -= front

      # make sure front always has less branches
      if len(front) > len(back):
        front, back = back, front
    return -1


if __name__ == "__main__":
  start = "AACCGGTT"
  end = "AACCGGTA"
  bank = ["AACCGGTA"]
  assert Solution.minMutation(None, start, end, bank) == 1

  start = "AACCGGTT"
  end = "AAACGGTA"
  bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
  assert Solution.minMutation(None, start, end, bank) == 2

  start = "AAAAACCC"
  end = "AACCCCCC"
  bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
  assert Solution.minMutation(None, start, end, bank) == 3
