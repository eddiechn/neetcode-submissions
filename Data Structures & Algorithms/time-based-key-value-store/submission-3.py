class TimeMap:

    def __init__(self):
        self.dictionary = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        
        self.dictionary[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.dictionary:
            arr = self.dictionary[key]
        else:
            arr = []

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1

            else:
                r = mid - 1

        return res
                
        
