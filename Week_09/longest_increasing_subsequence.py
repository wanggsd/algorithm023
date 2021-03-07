class Solution:
  def lengthOfLIS(self, nums):
    # tail_min[i]: min of tails of increasing subsequences with length i + 1
    tail_min = [0] * len(nums)
    res = 0
    for n in nums:
      start, end = 0, res
      # find the position to insert newly encountered number
      while start != end:
        mid = (start + end) // 2
        if tail_min[mid] < n:
          start = mid + 1
        else:
          end = mid
      tail_min[start] = n
      res = max(res, start + 1)
    return res


if __name__ == "__main__":
  assert Solution.lengthOfLIS(None, [10, 9, 2, 5, 3, 7, 101, 18]) == 4
  assert Solution.lengthOfLIS(None, [0, 1, 0, 3, 2, 3]) == 4
  assert Solution.lengthOfLIS(None, [7, 7, 7, 7, 7, 7, 7]) == 1
