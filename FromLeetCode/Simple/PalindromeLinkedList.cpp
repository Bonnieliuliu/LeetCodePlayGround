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
    bool isPalindrome(ListNode* head) {
        if(head == nullptr){
            return true;
        }//if
        // 中点位置
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }//while
        slow = slow->next;
        // 翻转
        ListNode* q = ReverseList(slow);
        // 判断是否是回文串
        ListNode* p = head;
        while(p && q){
            if(p->val != q->val){
                return false;
            }//if
            p = p->next;
            q = q->next;
        }//while
        return true;
    }
private:
    // 翻转
    ListNode* ReverseList(ListNode* head){
        if(head == nullptr){
            return head;
        }//if
        // 头结点
        ListNode* dummy = new ListNode(-1);
        ListNode* p = head;
        ListNode* nextNode = p->next;
        while(p){
            nextNode = p->next;
            p->next = dummy->next;
            dummy->next = p;
            p = nextNode;
        }//while
        return dummy->next;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

ListNode* stringToListNode(string input) {
    // Generate list from the input
    vector<int> list = stringToIntegerVector(input);

    // Now convert that list into linked list
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        ListNode* head = stringToListNode(line);
        
        bool ret = Solution().isPalindrome(head);

        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}