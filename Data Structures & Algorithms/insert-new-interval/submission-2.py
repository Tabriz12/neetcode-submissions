class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        '''

        [2, 4] [7, 8] [10, 12]

        [1,3] [0,1] [5,6] [3,11]

        '''
        

        l = 0
        r = len(intervals)

        s, e = newInterval

        while l < r:

            mid = (l+r) // 2

            if intervals[mid][0] > e:

                r = mid
            
            elif intervals[mid][1] < s:

                l = mid + 1
            
            else:
                
                lj = mid
                rj = mid
                while rj+1 < len(intervals) and e >= intervals[rj+1][0] :

                    rj+=1
                
                while lj-1 >= 0 and s <= intervals[lj-1][1]:

                    lj-=1
                
                res = []
                if lj > 0:
                    res.extend(intervals[:lj])
                res.append([min(s, intervals[lj][0]), max(e, intervals[rj][1])])
                
                if rj + 1 < len(intervals):
                    res += intervals[rj+1:]
                
                return res
        
        intervals.insert(l, newInterval)

        return intervals
            
            

            





