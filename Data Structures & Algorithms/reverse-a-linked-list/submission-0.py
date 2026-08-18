# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head


        st = head

        head = head.next

        st.next = None

        while head:

            t = head

            head = head.next

            t.next = st

            st  = t
        
        return st