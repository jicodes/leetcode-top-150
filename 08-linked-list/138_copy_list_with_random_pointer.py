# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        # Dictionary to hold the mapping from original nodes to their copies
        dic = {}

        # Step 1: Create copies of all nodes and store the mapping in the dictionary
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        # Step 2: Assign next and random pointers to the copied nodes
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        # Step 3: Return the head of the copied list
        return dic[head]
