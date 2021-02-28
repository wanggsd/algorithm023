class Solution:
  def merge(self, intervals):
    res = []
    # sort intervals based on start time
    intervals.sort(key=lambda x:x[0])

    for inter in intervals:
      if res and res[-1][1] >= inter[0]:
        # merge if two intervals overlap
        res[-1][1] = max(res[-1][1], inter[1])
      else:
        # add interval if no overlap
        res.append(inter)
    return res


if __name__ == "__main__":
  assert Solution.merge(None, [[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
  assert Solution.merge(None, [[1,4],[4,5]]) == [[1, 5]]
