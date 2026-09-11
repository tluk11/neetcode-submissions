class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for word in strs:
            wordCount = ''.join(sorted(word))

            if wordCount in myMap:
                list = myMap[wordCount]
                list.append(word)
                myMap[wordCount] = list
            else:
                myMap[wordCount] = [word]
        result = []
        for val in myMap.values():
            result.append(val)

        return result 