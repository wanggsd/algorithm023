#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void moveZeroes(vector<int>& nums) {
    int nonzero_idx = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] != 0) {
        if (i != nonzero_idx) {
          nums[nonzero_idx] = nums[i];
          nums[i] = 0;
        }
        nonzero_idx++;
      }
    }
  }
};

/*
int main() {
  vector<int> nums = {0, 1, 0, 3, 12};
  Solution sol;
  sol.moveZeroes(nums);
  for (int& n : nums)
    cout << n << ", ";
  cout << endl;
}
*/
