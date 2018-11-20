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
    void deleteNode(ListNode* node) 
    {
        ListNode *temp = node->next;
        // node = temp; //wrong
        node->val = node->next->val;
        node->next = temp->next;
        temp->next = NULL;
        delete temp;
    }
};