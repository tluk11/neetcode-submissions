class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res+="#"+str(len(st))+"#"+st
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i< len(s):
            length = ""
            if s[i:i+1] == "#":
                i+=1
                while s[i:i+1] != "#":
                    length+=s[i:i+1]
                    i+=1
                nlength = int(length)
            res.append(s[i+1:i+nlength+1])
            i+=nlength+1
        return res

