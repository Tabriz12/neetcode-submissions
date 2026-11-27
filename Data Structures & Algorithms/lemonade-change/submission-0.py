class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:



        cnt = {5:0, 10:0}


        for b in bills:

            if b == 5:

                cnt[5]+=1
            
            elif b == 10:

                cnt[10]+=1

                cnt[5]-=1

                if cnt[5] < 0: return False
            
            else:

                if cnt[10] > 0 and cnt[5] > 0:

                    cnt[10]-=1
                    cnt[5] -=1
                
                elif cnt[5] > 2:

                    cnt[5] -=3
                
                else: return False
        return True

        