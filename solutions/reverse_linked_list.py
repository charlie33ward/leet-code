# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative solution: T O(n), M O(n)
        prev, curr = None, head

        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev