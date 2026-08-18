# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        routes: dict[Node] = {}


        cur = None
        

        while head:

            if cur:

                cur.next = Node(head.val)

                cur = cur.next
            
            else:


                cur = Node(head.val)
                st = cur
            

            routes[head] = cur

            head = head.next
        

        for k, v in routes.items():

            
            v.random = routes.get(k.random, None)
        
        return st
        










        