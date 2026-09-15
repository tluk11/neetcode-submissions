class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key]:
            return ""
        l = self.hashmap[key]
        left,right = 0,len(l) - 1
        
        while left<= right:
            mid = (left+right)//2
            if l[mid][1] == timestamp:
                return l[mid][0]
            elif l[mid][1] < timestamp:
                left = mid+1
            else:
                right = mid-1
        return l[right][0] if right >= 0 else ""
