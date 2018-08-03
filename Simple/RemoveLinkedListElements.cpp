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
    ListNode* removeElements(ListNode* head, int val) 
    {
        ListNode *dummy = new ListNode(-1), *pre = dummy;
        dummy->next= head;
        while(pre->next)
        {
            if (pre->next->val == val)
            {
                ListNode *temp = pre->next;
                pre->next = temp->next;
                temp->next = NULL;
                delete temp;
            }
            else{pre=pre->next;}
            
        }
        return dummy->next;
    }
};