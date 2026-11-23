# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        first = second = temp

        for i in range(n + 1):
            first = first.next # will become the node before last nth's (makes a gap of size n)

        while first: # loop will end when second is the node right before last nth's
            first = first.next
            second = second.next

        second.next = second.next.next

        return temp.next