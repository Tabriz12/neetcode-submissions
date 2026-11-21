# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:



        st = ListNode(val+1, head)

        dummy = st

        prev = st

        st = st.next

        

        while st:

            if st.val == val:

                prev.next = st.next

            else:

                prev = st
            
            st = st.next
        
        return dummy.next





        