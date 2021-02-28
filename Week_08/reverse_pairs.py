class BIT:
  def __init__(self, n):
    self.n = n + 1
    self.sums = [0] * self.n

  def update(self, i, delta):
    while i < self.n:
      self.sums[i] += delta
      i += i & (-i)

  def query(self, i):
    res = 0
    while i > 0:
      res += self.sums[i]
      i -= i & (-i)
    return res

class Solution:
  def reversePairs(self, nums):
    res = 0

    # init a BIT to store nums and nums * 2
    new_nums = nums + [x * 2 for x in nums]
    tree = BIT(len(new_nums))

    # ranks map a number to its BIT array index
    ranks = {n : i + 1 for i, n in enumerate(sorted(list(set(new_nums))))}

    # iterate from left to right
    for n in reversed(nums):
      # sum all nodes smaller than n, add to the final result
      res += tree.query(ranks[n] - 1)
      # insrease n * 2 by one in BIT
      tree.update(ranks[n * 2], 1)
    return res


if __name__ == "__main__":
  assert Solution.reversePairs(None, [1,3,2,3,1]) == 2
  assert Solution.reversePairs(None, [2,4,3,5,1]) == 3
