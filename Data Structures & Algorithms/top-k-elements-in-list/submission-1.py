class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            if num in myMap:
                count = myMap[num]
                count+=1
                myMap[num] = count
            else:
                myMap[num] = 1

        sorted_keys = [k for k, v in sorted(myMap.items(), key=lambda item: item[1],reverse=True)]
        result = []
        count = 0
        for key in sorted_keys:
            if count < k:
                result.append(key)
                count+=1

        return result