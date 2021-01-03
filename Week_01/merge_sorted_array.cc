#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int idx1 = m - 1;
    int idx2 = n - 1;
    int end = m + n - 1;
    while (idx2 >= 0) {
      nums1[end--] = (idx1 >= 0 && nums1[idx1] > nums2[idx2]) ? nums1[idx1--] : nums2[idx2--];
    }
  }
};

/*
int main() {
  vector<int> nums1 = {1, 2, 3, 0, 0, 0};
  vector<int> nums2 = {2, 5, 6};
  Solution sol;
  sol.merge(nums1, 3, nums2, 3);
  for (int& n : nums1)
    cout << n << ", ";
  cout << endl;
}
*/
