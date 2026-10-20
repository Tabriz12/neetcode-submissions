class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if not n: return True
        
        fb = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)+1):

            if fb[i] == 0 and fb[i-1] == 0 and fb[i+1] == 0:

                n -=1
                fb[i] = 1

                if n == 0:
                    return True
        
        return False
            

            

