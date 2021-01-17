class Solution {
public:
  vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> res;
    permute(nums, 0, res);
    return res;
  }

  void permute(vector<int>& nums, int start, vector<vector<int>>& res) {
    // record when all numbers are chosen
    if (start >= nums.size()) {
      res.push_back(nums);
      return;
    }

    for (int i = start; i < nums.size(); i++) {
      // choose one number
      swap(nums[start], nums[i]);
      // choose the rest number
      permute(nums, start + 1, res);
      // reset the number chosen b4
      swap(nums[start], nums[i]);
    }
  }
};
