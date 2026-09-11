class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res+= str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':      # find the delimiter
                j += 1
            length = int(s[i:j])     # length can be any number of digits
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length       # move past this word
        return res
