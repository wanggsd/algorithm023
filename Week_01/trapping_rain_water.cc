#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int trap(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int h_max = 0;
    int res = 0;
    while (left < right) {
      int lower_bound = height[height[left] < height[right] ? left++ : right--];
      h_max = max(lower_bound, h_max);
      res += h_max - lower_bound;
    }
    return res;
  }
};

/*
int main() {
  Solution sol;
  vector<int> height = {4, 2, 0, 3, 2, 5};
  cout << sol.trap(height) << endl;
}
*/
