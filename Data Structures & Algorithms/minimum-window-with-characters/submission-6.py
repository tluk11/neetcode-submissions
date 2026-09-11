class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        reslen = float('inf')
        if len(s)<len(t):
            return res

        l = 0
        dictt = defaultdict(int)
        for cha in t:
            dictt[cha]+=1
        values=0
        for _ in dictt.values():
            values+=1

        dicts = defaultdict(int)

        for r in range(len(s)):
            cha = s[r]
            if cha in dictt:
                dicts[cha]+=1
                if dicts[cha] == dictt[cha]:
                    values-=1
            while values == 0:
                if r-l+1 < reslen:
                    res=s[l:r+1]
                    reslen = r-l+1
                temp = s[l]
                if temp in dictt:
                    dicts[temp]-=1
                    if dicts[temp] < dictt[temp]:
                        values+=1
                l+=1

        return res