class TimeMap:

    """
    {timestamp:key}

    """

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        temp = self.store[key]
        l = 0

        r = len(temp) - 1
        

        while l <= r:
            m = l + (r - l) //2
            if temp[m][1] <= timestamp:
                l = m + 1
                res = temp[m][0]

            else:
                r = m - 1


        return res
        
