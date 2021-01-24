class Solution:
  def findMin(self, nums):
    start, end = 0, len(nums) - 1
    while start < end:
      # avoid potential overflow of start + end
      mid = start + (end - start) // 2

      if nums[mid] > nums[end]:
        # right half is unordered, which must includes min val
        # mid cannot be min val since nums[end] < nums[mid]
        start = mid + 1
      else:
        # right half is ordered, min val is not on the right of mid
        # mid and all elements on its left can be the min val
        end = mid
    # binary search stops when start == end, where nums[start] is min val
    return nums[start]
