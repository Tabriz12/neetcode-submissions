class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 2:
            return min(cost)

        res = cost[:2] + (len(cost)-2) * [0]

        for i in range(2, len(cost)):

            res[i] = cost[i] + min(res[i-1], res[i-2])

        

        return min(res[i], res[i-1])













        