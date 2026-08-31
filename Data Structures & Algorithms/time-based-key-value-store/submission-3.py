from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.states = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.states[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.states:
            return ""

        values = self.states[key]

        l, r = 0, len(values)

        while l < r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid

        return values[l - 1][1] if l > 0 else ""