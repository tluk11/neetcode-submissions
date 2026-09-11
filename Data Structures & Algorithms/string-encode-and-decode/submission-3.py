class Solution:

    def encode(self, strs: List[str]) -> str: # write length of word at beginning for each word
        res = ""
        for word in strs:
            length = len(word)
            res+= str(length)+ '#' + word # 4word
        return res
    def decode(self, s: str) -> List[str]: # reads number and jumps to next index 
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res