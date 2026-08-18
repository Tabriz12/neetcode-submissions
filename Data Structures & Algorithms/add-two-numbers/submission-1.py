# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        r = 0

        start = head = ListNode(val=0)


        while l1 and l2:

            tot = l1.val+l2.val + r

            s = (tot) % 10
            r = (tot) // 10
            head.next = ListNode(s)
            head = head.next

            l1 = l1.next
            l2 = l2.next
        

        standing = l1 or l2
        

        while standing:

            tot = standing.val + r

            s = (tot) % 10

            r = (tot) // 10

            head.next = ListNode(s)

            head = head.next

            standing = standing.next
        
        if r:

            head.next = ListNode(1)
        
        return start.next




            




        