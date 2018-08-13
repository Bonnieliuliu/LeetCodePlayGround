/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head)
    {
        if (!head)return NULL;
        if(!head->next)return new TreeNode(head->val);
        ListNode * slow = head;
        ListNode * fast = head;
        ListNode * last = slow;
        while(fast->next &&fast->next->next)
        {
            last = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        fast = slow->next;//递归根节点右子树
        last->next = NULL;
        TreeNode *cur = new TreeNode(slow->val);
        if(head!=slow) cur->left = sortedListToBST(head);
        cur->right = sortedListToBST(fast);
        return cur;
    }
};