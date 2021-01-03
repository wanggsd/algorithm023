#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> record;
    for (int i = 0; i < nums.size(); i++) {
      int remain = target - nums[i];
      if (record.find(remain) == record.end()) record[nums[i]] = i;
      else return {record[remain], i};
    }
    return {};
  }
};

/*
int main() {
  vector<int> nums = {3, 2, 4};
  Solution sol;
  vector<int> res = sol.twoSum(nums, 6);
  cout << res[0] << ", " << res[1] << endl;
}
*/
