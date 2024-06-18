# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        temp = head
        while(temp):
            lis.append(head.val)
            temp = temp.next
        for i in range(len(lis)//2):
            head = head.next
        return head
