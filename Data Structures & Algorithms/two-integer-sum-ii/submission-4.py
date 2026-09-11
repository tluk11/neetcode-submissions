class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(numbers)):
            num = numbers[i]
            need = target-num
            if need in hashmap:
                return [hashmap[need]+1,i+1]
            hashmap[num] = i
