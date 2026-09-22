# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle of the list (slow+1 is the middle since fast moves twice as fast as slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half 
        # curr points to the node after slow aka slow+1
        prev, curr = None, slow.next
        # cut off the second half from the first
        slow.next = None
        # reverse the second half
        # temp holds the original next node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            
        