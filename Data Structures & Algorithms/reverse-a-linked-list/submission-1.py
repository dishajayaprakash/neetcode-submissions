# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        prev, curr = None, head
        # curr → the current node we are processing
        # prev → the node that should come after curr once reversed
        # temp → the original next node
        while curr:
            temp = curr.next # Save the next node
            curr.next = prev # Reverse the pointer of the current node to point to the previous node
            prev = curr # Move prev to curr because that will be the node the next curr will have to point to in order to be reversed
            curr = temp # Move curr to temp (aka the original next node)
        return prev