#include <vector>
#include <stack>

class Solution {
public:
  vector<int> inorderTraversal(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> frontline;
    while (root || !frontline.empty()) {
      while (root) {
        frontline.push(root);
        root = root->left;
      }
      root = frontline.top();
      frontline.pop();
      res.push_back(root->val);
      root = root->right;
    }
    return res;
  }
};
