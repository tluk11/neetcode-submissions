class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg,end = 0,len(numbers)-1

        while numbers[beg] + numbers[end] != target:
            if numbers[beg] + numbers[end] < target:
                beg+=1
            if numbers[beg] + numbers[end] > target:
                end-=1
        return [beg+1,end+1]