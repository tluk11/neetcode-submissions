class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0 
        res = 0 
        maxlen = 0 
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                temp = hashmap[s[i]] + 1
                hashmap[s[i]] = temp
            maxlen = max(maxlen,hashmap[s[i]])
            if i - left + 1 - maxlen > k:
                hashmap[s[left]] -= 1
                left+=1
            res = max(res, i - left + 1)

        return res
