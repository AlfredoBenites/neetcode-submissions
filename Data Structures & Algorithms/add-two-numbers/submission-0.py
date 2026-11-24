# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, prev1 = l1, None
        curr2, prev2 = l2, None

        while curr1:
            temp = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp

        while curr2:
            temp = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = temp

        num1 = []
        num2 = []

        while prev1:
            num1.append(str(prev1.val))
            prev1 = prev1.next
        
        while prev2:
            num2.append(str(prev2.val))
            prev2 = prev2.next

        final_num = int("".join(num1)) + int("".join(num2))
        final_num_str = str(final_num)
        prev = ListNode(0)
        curr = prev

        for i in range(len(final_num_str) - 1, -1, -1):
            curr.next = ListNode(int(final_num_str[i]))
            curr = curr.next
        
        return prev.next