class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlen = 1
        if not s:
            return 0

        hashmap = defaultdict(int)
        for r in range(len(s)):
            if s[r] in hashmap:
                if hashmap[s[r]] < l:
                    hashmap[s[r]] = r
                else:
                    l = hashmap[s[r]]+1
                    hashmap[s[r]] = r
                    
            else:
                hashmap[s[r]] = r
            maxlen = max(maxlen,r-l+1)

        return maxlen