#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    // count each value
    unordered_map<int, int> count;
    for (auto n : nums)
      count[n]++;

    // convert the hashmap to a vector
    vector<pair<int, int>> num_count;
    for (auto kv : count)
      num_count.push_back({kv.first, kv.second});

    // Hoare's selection algorithm
    kselection(num_count, 0, num_count.size() - 1, k);

    // get first k elements as the result
    vector<int> res;
    for (int i = 0; i < k && i < num_count.size(); i++)
      res.push_back(num_count[i].first);
    return res;
  }

  void kselection(vector<pair<int, int>>& data, int start, int end, int k) {
    if (start >= end) return;
    auto rec = data[end];
    int i = start;
    int j = start;
    while (i < end) {
      if (data[i].second > rec.second)
        swap(data[i++], data[j++]);
      else
        i++;
    }
    // put pivot into the right position
    swap(data[j], data[end]);
    int n = j - start + 1;
    if (n == k)
      return;
    else if (n < k)
      kselection(data, j + 1, end, k - n);
    else
      kselection(data, start, j - 1, k);
  }
};

//int main() {
//  Solution sol;
//  vector<int> nums = {1, 1, 1, 2, 2, 3};
//  for (auto n : sol.topKFrequent(nums, 2))
//    cout << n << ", ";
//  cout << endl;
//}
