class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        

        res = 0

        summy = sum(arr[:k])

        n = k
        if summy / k >= threshold:
            res+=1
        
        while n < len(arr):

            summy = summy - arr[n-k] + arr[n]

            if summy / k >= threshold:
                res+=1
            n+=1
        
        return res

            








        