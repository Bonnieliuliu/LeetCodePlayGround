
//  Definition for singly-linked list.
  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head)
    {
        if (!head || !head->next){return head;}
        ListNode *start = head;
        while(start && start->next)
        {
            if (start->next->val == start->val)
            {
                ListNode* temp = start->next;
                start->next = start->next->next;
                delete temp;
            }
            else{start = start->next;}
        }
    return head;
    }

};