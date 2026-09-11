class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mh = []  
        for point in points:
            distance = math.sqrt(point[0]*point[0]+point[1]*point[1])
            heapq.heappush(mh,(-distance,point))
            if len(mh) > k:
                heapq.heappop(mh)
            
        res = []
        for dist,point in mh:
            res.append(point)

        return res