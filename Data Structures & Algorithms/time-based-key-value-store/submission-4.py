class TimeMap:

    def __init__(self):
        self.timestamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        value = self.timestamps[key]
        # print(value)

        ans = ""
        l,r = 0 , len(value)-1
        while l <= r:
            m = (l+r)//2
            if value[m][1] <= timestamp:
                ans = value[m][0]
                l = m + 1
            else:
                r = m -1
        return ans

        
