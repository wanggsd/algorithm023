class Solution:
  def canJump(self, nums):
    # the largest reachable index
    reach = 0
    for i, n in enumerate(nums):
      # return False if i can never be reached, so does len(nums) - 1
      if i > reach:
        return False
      # update reachable index
      reach = max(reach, i + n)
      # return True if len(nums) - 1 is already reachable
      if reach >= len(nums) - 1:
        return True
    return True
