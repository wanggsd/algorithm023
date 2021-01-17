class Solution {
public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    // terminate when find q/p or run out of nodes
    if (root == nullptr || root == p || root == q) return root;

    // search p, q in left subtree
    TreeNode* left_res = lowestCommonAncestor(root->left, p, q);

    // search p, q in right subtree
    TreeNode* right_res = lowestCommonAncestor(root->right, p, q);

    // only found p/q in right subtree
    if (left_res == nullptr) return right_res;
    // only found p/q in left subtree
    else if (right_res == nullptr) return left_res;
    // found p in one subtree, and q in another
    return root;
  }
};
