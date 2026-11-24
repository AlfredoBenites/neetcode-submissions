"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d = {}
        curr = head

        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next

        for key, val in d.items():
            val.next = d.get(key.next)
            val.random = d.get(key.random)

        return d[head]