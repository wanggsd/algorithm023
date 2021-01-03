struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode* mergeTwoLists(ListNode *l1, ListNode *l2) {
    ListNode sentinel = ListNode();
    ListNode *current = &sentinel;
    while (l1 != nullptr && l2 != nullptr) {
      if (l1->val < l2->val) {
        current->next = l1;
        l1 = l1->next;
      } else {
        current->next = l2;
        l2 = l2->next;
      }
      current = current->next;
    }
    current->next = l1 == nullptr ? l2 : l1;
    return sentinel.next;
  }
};
