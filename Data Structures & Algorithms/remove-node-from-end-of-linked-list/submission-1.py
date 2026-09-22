# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy
        # move right n steps ahead so we always have a gap of n between right and left
        for _ in range(n):
            right = right.next
        # move right all the way to end and left will be right before the nth node from end
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


        
        
        