class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        chars = {}
        res = 0
        length = 0
        for i in range(len(s)):
            if s[i] in chars and chars[s[i]]>= i-length:
                length= i - chars[s[i]]
                chars[s[i]] = i
            else:
                length+=1
                chars[s[i]] = i 
            res = max(res,length)
        return res
