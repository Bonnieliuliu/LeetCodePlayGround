/*
 Definition for singly-linked list.
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        if (!headA || !headB) {return NULL;}
        int lenA = GetLength(headA);
        int lenB = GetLength(headB);
        if (lenA > lenB)
        {
            int cnt = lenA - lenB;
            while(cnt > 0){cnt--; headA = headA->next;}
        }
        else
        {
            int cnt = lenB-lenA;
            while(cnt>0){cnt--; headB = headB->next;}
        }
        while (headA!=headB)
        {
            headA = headA->next;
            headB = headB->next;
        }
        if (headA == NULL){return headA;}
        return headA;
        
    }
public:
    int GetLength(ListNode *node)
    {
        if (!node){return 0;}
        int cnt = 0;
        while(node)
        {
            node = node->next;
            cnt++;
        }
        return cnt;
    }
};