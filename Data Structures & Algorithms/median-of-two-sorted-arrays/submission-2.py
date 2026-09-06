class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):

            nums1, nums2 = nums2, nums1
        
        tot = len(nums1) + len(nums2)
        half = tot // 2
        
        
        '''

        [1,4,5]

        [7,8,10]

        '''

        l1, r1 = 0, len(nums1)-1


        while True:

            m1  = (l1 + r1) // 2

            m2 = half  - (m1 + 1) -1

            lb1 = nums1[m1] if m1 >= 0 else -1e+7

            rb1 = nums1[m1+1] if m1 < len(nums1) - 1 else 1e+7

            lb2 = nums2[m2] if m2 >= 0 else -1e+7

            rb2 = nums2[m2+1] if m2 < len(nums2) - 1 else 1e+7

            if lb1 <= rb2 and lb2 <= rb1:

                if tot % 2 == 1:

                    return min(rb2, rb1)
                
                else:

                    return (min(rb2, rb1) + max(lb1, lb2)) / 2
            
            elif lb1 > rb2:

                r1 = m1-1
            
            else:

                l1 = m1 + 1




        












        





        