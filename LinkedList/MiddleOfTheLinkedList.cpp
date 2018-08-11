//  # Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode* middleNode(ListNode* head)
    {
        ListNode* tmp = head;
        vector<int> buf;
        while(tmp)
        {
            buf.push_back(tmp->val);
            tmp = tmp->next;
        }
        int index = ceil((float)(buf.size()-1.0)/2);
        int i = 0;
        ListNode* tmp2 = head;
        while(i<index)
        {
            tmp2=tmp2->next;
            i++;
        }
        return tmp2;
    }
};