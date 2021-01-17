class Solution {
public:
  vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> res;
    if (n < k) return res;
    vector<int> res_holder;
    combine(res, res_holder, 0, 0, n, k);
    return res;
  }

  void combine(vector<vector<int>>& res, vector<int>& res_holder, int start, int n_set, int n, int k) {
    // record the current result if all numbers are set
    if (n_set == k) {
      res.push_back(res_holder);
      return;
    }

    for (int i = start; i < n; i++) {
      // set one number
      res_holder.push_back(i + 1);
      // set the rest with numbers whose indices are larger 
      combine(res, res_holder, i + 1, n_set + 1, n, k);
      // reverse the number set before
      res_holder.pop_back();
    }
  }
};
