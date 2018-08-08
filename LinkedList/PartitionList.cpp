/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x)
    {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy, *cur = dummy;
        while(pre->next && pre->next->val >= x)pre=pre->next;
        cur = pre;
        while(cur->next)
        {
            if (cur->next->val<x)
            {
                ListNode* tmp = cur->next;
                cur->next = tmp->next;
                tmp->next = pre->next;
                pre->next = tmp;
                pre = pre->next;

            }
            else{cur = cur->next;}
        }
        return dummy->next;
    }
};