/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
       ListNode* rh = nullptr;
        ListNode* prev = nullptr;
        ListNode* cur = nullptr;
        
        int carry = 0;
        while (l1 != nullptr && l2 != nullptr)
        {
            int r_i = l1->val + l2->val + carry;
            
            l1 = l1->next;
            l2 = l2->next;
            
            carry = r_i / 10;            
            cur = new ListNode(r_i % 10);
            
            if (prev == nullptr)
            {
                rh = cur;
            }
            else
            {
                prev->next = cur;
            }
            prev = cur;
        }        
        while (l1 != nullptr)
        {
            int r_i = l1->val + carry;
            l1 = l1->next;
            carry = r_i / 10;
            cur = new ListNode(r_i % 10);
            
            prev->next = cur;
            prev = cur;
        }
        while (l2 != nullptr)
        {
            int r_i = l2->val + carry;
            l2 = l2->next;
            carry = r_i / 10;
            cur = new ListNode(r_i % 10);
            
            prev->next = cur;
            prev = cur;
        }
        if (carry != 0)
        {
            cur = new ListNode(carry);
            
            prev->next = cur;
            prev = cur;
        }
        return rh;

    }
};