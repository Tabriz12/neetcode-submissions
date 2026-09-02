#Definition of Interval:
from collections import defaultdict
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):

        return f"{self.start}-{self.end}"

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        times = defaultdict(int)
        for i in intervals:

            times[i.start] += 1
            times[i.end] -= 1

        res = count = 0
        for k in sorted(times.keys()):

            count += times[k]
            res = max(res, count)
        return res



