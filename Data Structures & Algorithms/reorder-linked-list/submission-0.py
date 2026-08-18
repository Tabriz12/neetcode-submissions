# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # [2, 3, 5, 7, 8]
        # 2,4,6,8

        def rec(f, s):


            if not s:
                return
            
            if s.next:
            
                f = rec(f, s.next)
            
            if not f:
                return None

            
            if f.next == s or f==s:

                s.next = None
                return



            tmp = f.next # 4,

            f.next = s # 8,

            s.next = tmp # 2-8-4-6



            return tmp
        
        head = rec(head, head.next)



            



            
            







        
        

        



        