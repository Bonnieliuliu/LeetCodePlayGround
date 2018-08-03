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
    ListNode* reverseList(ListNode* head)
    {
        if(!head||!head->next){return head;}
        ListNode *p = head;
        ListNode *dummy = new ListNode(-1);
        ListNode *nextNode = p->next;
        while(p)
        {
            nextNode = p->next;
            p->next = dummy->next;
            dummy->next = p;
            p = nextNode;
        }
        return dummy->next;
    }
};