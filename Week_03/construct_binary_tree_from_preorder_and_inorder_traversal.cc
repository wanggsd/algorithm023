class Solution {
public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    int root_idx = 0;
    return build(preorder, inorder, root_idx, 0, inorder.size() - 1);
  }

  TreeNode* build(vector<int>& preorder, vector<int>& inorder, int& root_idx, int start, int end) {
    // stop building when running out of nodes
    if (start > end) return nullptr;

    // find root in inorder
    int pivot = start;
    while (inorder[pivot] != preorder[root_idx]) pivot++;

    // create current root node and set root idx for subtree
    TreeNode* new_node = new TreeNode(preorder[root_idx++]);

    // build left subtree
    new_node->left = build(preorder, inorder, root_idx, start, pivot - 1);

    // build right subtree
    new_node->right = build(preorder, inorder, root_idx, pivot + 1, end);
    return new_node;
  }
};
