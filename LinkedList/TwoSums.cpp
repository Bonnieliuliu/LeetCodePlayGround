struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        ListNode* dummy = new ListNode(0);
        ListNode* tmp = dummy;
        int flag = 0;
        while(l1 || l2)
        {
            int n1 = l1?l1->val:0;
            int n2 = l2?l2->val:0;
            int sum = n1+n2+flag;
            flag = sum / 10;
            tmp->next = new ListNode(sum%10);
            tmp = tmp->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        if (flag)
        {
            tmp->next = new ListNode(1);
        }
        return dummy->next;  
    }
};