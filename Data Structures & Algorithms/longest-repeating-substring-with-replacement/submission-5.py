class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        res = 0
        letters = defaultdict(int)
        for r in range(len(s)):
            letters[s[r]]+=1
            maxf = max(maxf,letters[s[r]])
            while r-l+1-maxf > k:
                letters[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res

        
