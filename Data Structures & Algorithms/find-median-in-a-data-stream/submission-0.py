class MedianFinder:

    def __init__(self):
        self.lowerhalf = [] # max heap 
        self.upperhalf = [] # min heap 

    def addNum(self, num: int) -> None:
        if self.upperhalf and num > self.upperhalf[0]:
            heapq.heappush(self.upperhalf,num)
        else:
            heapq.heappush_max(self.lowerhalf,num)

        if len(self.lowerhalf) > len(self.upperhalf)+1:
            temp = heapq.heappop_max(self.lowerhalf)
            heapq.heappush(self.upperhalf,temp)
        if len(self.upperhalf) > len(self.lowerhalf)+1:
            temp = heapq.heappop(self.upperhalf)
            heapq.heappush_max(self.lowerhalf,temp)

    def findMedian(self) -> float:
        if len(self.lowerhalf)>len(self.upperhalf):
            return self.lowerhalf[0]
        elif len(self.lowerhalf)<len(self.upperhalf):
            return self.upperhalf[0]
        return (self.lowerhalf[0]+self.upperhalf[0])/2.0
        
        