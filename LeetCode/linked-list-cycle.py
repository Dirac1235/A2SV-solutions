# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next and head.next.next:
            fast = head.next.next
            slow = head.next
        else:
            return False
        while fast and slow:
            if fast == slow:
                return True
            if fast.next and slow.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
