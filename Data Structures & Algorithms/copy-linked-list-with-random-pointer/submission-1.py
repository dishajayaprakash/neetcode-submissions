"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        copy = Node(head.val) # copy the current node
        self.map[head] = copy # store it in the map
        copy.next = self.copyRandomList(head.next) # recursively copy its next so we move through the list
        copy.random = self.map.get(head.random) # link its random using the map
        return copy
        
        

    