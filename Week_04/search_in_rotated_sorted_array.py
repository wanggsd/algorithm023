class Solution:
  def search(self, nums, target):
    # handle empty input
    if not nums:
      return -1
    start, end = 0, len(nums) - 1
    while start < end:
      # avoid overflow of start + end
      mid = start + (end - start) // 2
      # found target
      if nums[mid] == target:
        return mid
      if target < nums[mid]:
        if nums[start] <= nums[mid] and target < nums[start]:
          # target is only in right half if left side is ordered and target < nums[start]
          start = mid + 1
        else:
          end = mid - 1
      else:
        if nums[mid] <= nums[end] and target > nums[end]:
          # target is only in left half if right half is ordered and target > nums[end]
          end = mid - 1
        else:
          start = mid + 1
    return -1 if nums[start] != target else start
