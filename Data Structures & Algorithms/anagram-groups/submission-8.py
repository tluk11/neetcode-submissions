class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for st in strs:
            letters = [0]*26
            for s in st:
                letters[ord('a')-ord(s)]+=1
            hashmap[tuple(letters)].append(st)

        return list(hashmap.values())
            