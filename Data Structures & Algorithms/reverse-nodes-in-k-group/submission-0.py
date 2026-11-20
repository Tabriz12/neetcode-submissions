# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:


    def reverse(self, head, k):


        new_end = head
        new_start = None
        

        while head and k:

            frw = head.next

            head.next = new_start

            new_start = head

            head = frw

            k-=1
        

        if k:

            new_end, new_start = new_start, None

            head = new_end

            nex = None

            while head:

                frw = head.next

                head.next = new_start

                new_start = head

                head = frw
        

        return new_start, new_end, frw


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:



        frw = head

        start = None

        cur = None


        while frw:


            new_start, new_end, frw = self.reverse(frw, k)

            if not start:

                start = new_start
            
            if cur:
                cur.next = new_start

            cur = new_end
        
        return start
        



            








        