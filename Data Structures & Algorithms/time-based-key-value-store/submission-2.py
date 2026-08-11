class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]: return ""

        l, r = 0, len(self.d[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.d[key][mid][1] == timestamp:
                return self.d[key][mid][0]
            elif self.d[key][mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if self.d[key][mid][1] < timestamp:
            return self.d[key][mid][0]
        return self.d[key][mid-1][0] if mid - 1 >= 0 else ""
