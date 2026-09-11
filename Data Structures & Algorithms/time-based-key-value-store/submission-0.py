class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            values = self.store[key]
            values.append([value,timestamp])
        else:
            self.store[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            left,right = 0,len(self.store[key])-1
            l1 = self.store[key]
            l2 = l1[0]
            if l2[1] > timestamp:
                return ""
            while left<=right:
                mid = (left+right)//2
                l2 = l1[mid]
                if  l2[1] > timestamp:
                    right = mid-1
                elif l2[1] < timestamp:
                    left = mid+1
                elif l2[1] == timestamp:
                    return l2[0]
            return l1[right][0]
        else:
            return ""
