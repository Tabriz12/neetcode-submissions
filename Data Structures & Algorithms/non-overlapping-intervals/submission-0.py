class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        '''

        [1,9] [2, 6] [3,6] [4,5]


        [1,3] [2,4] [3,8] [4,6]

        '''


        intervals.sort(key = lambda x: x[-1])
        res = 0

        end = intervals[0][-1]
        for i in range(1, len(intervals)):

            if intervals[i][0] < end:
                res+=1
            
            else:
                end = intervals[i][-1]

        return res