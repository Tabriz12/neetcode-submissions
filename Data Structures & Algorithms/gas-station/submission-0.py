class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:



        """


        """

        st = -1

        tot = 0

        for i in range(len(gas)):

            if st < 0:
                st = i
                cur = 0

            tot += (gas[i] - cost[i])

            cur += (gas[i]-cost[i])

            if cur < 0:

                st = -1


        
        if cur < 0 or tot < 0 or st < 0:
            return -1
        
        else:

            for i in range(st):

                cur += (gas[i]-cost[i])

                if cur < 0:
                    return -1
        
        return st

            
        


                






        