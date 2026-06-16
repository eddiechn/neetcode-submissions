class TimeMap:

    def __init__(self):
        self.dic = {} # -> key -> [(value, timestamp)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((value, timestamp))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        values = [(v, t) for v, t in self.dic[key] if t <= timestamp]
        if not values:
            return ""

        return values[-1][0]

        

        
