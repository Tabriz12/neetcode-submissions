# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self):
        self.cnt = 0


    def rec(self, head, n):

        if not head:
            return None
        
        
        head.next = self.rec(head.next, n)

        self.cnt+=1

        if n == self.cnt:

            return head.next
        
        return head





    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        return self.rec(head, n)
        