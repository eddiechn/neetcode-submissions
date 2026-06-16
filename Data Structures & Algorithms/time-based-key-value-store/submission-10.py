class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not key:
            return ""

        res = ""
        values = self.store[key]
        values.sort()

        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1

            else:
                r = m - 1

            



        return res
        
