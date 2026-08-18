class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        


        intervals.sort(key=lambda x: x[0])


        s, e = intervals[0]

        res = []


        for i in range(1, len(intervals)):


            if intervals[i][0] > e:

                res.append([s,e])

                s, e = intervals[i]

            else:

                e = max(e, intervals[i][-1])
        

        res.append([s,e])

        return res