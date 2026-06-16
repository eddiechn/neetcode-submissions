class TimeMap:

    def __init__(self):
        self.dic = {} # -> key -> [(value, timestamp)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((value, timestamp))
        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key, [])

        l = 0
        r = len(values) -1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l += 1

            else:
                r -= 1

        return res
        

        
