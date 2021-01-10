#include <vector>
#include <stack>

class Solution {
public:
  vector<int> preorderTraversal(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> frontline;
    while (root || !frontline.empty()) {
      if (root) {
         res.push_back(root->val);
         if (root->right) frontline.push(root->right);
         root = root->left;
      } else {
        root = frontline.top();
        frontline.pop();
      }
    }
    return res;
  }
};
