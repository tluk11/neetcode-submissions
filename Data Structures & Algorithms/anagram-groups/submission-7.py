class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char)-ord('a')]+=1
            map[tuple(letters)].append(string)

        

        return list(map.values())