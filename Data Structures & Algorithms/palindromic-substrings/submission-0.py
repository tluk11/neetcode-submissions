class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def isPal(beg, end):
            nonlocal res
            while beg >= 0 and end < len(s) and s[beg] == s[end]:
                res += 1
                beg -= 1
                end += 1

        for i in range(len(s)):
            # Odd length palindromes (center at i)
            isPal(i, i)
            # Even length palindromes (center between i and i+1)
            isPal(i, i+1)

        return res
